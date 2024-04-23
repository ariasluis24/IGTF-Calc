from tkinter import *
from tkinter import simpledialog
import tkinter.messagebox, os, threading
import src.calculations as calculations
from src.scrap_price_BCV import scraping_BCV
# Variables
x = threading.Thread(target=scraping_BCV, args=())
BCV_Price = scraping_BCV() 
x.start()
user_name = os.getlogin()
result_height = 14 # Used into the Labels.

# WIP make the sub_total Entry work only if a valid value.
# Try to use Try and Exception ValueError.
def get_sub_total():
    """
    # This function works in the next way.\n
   
    Is called on the button command of 'calculate_button'.\n
    
    Create 3 global variables (my_list, main_question, agent_of_retention).\n
    
    Gets the value of the entry 'sub_total'. Converts the value into float and storage it into the 'sub_total_float' variable.\n
    
    Calls the module 'calculations' to use 'principal_Calculation' function and calculate
    the main values using 'sub_total_float' as an argument and storage the result, into 2 separate variables (IVA, total).\n
     
    Calls the module 'calculations' to use 'GUI_principal_Calculation' function and storage the returned 
    text value on the 'principal_calculation' variable, using as arguments the previous variables 'sub_total_float', 'IVA', 'total'.\n
    
    Creates a Label to print in the window the 'GUI_principal_Calculation' returned text, and then storage into 'principal_calculation' variable.
    The label contains its own configuration such as font, border, width, height, relief. And its put it into the window 
    using grid.\n
    
    2 tkinter.messageboxes, asking a yes/no question are created saving their return values into the 2 global variables (main_question, agent_of_retention) for further use.\n
    
    Depending on the values of the tkinter.messageboxes (main_question, agent_of_retention), the program would ask using a simpledialog for a value, which is goin
    to be saved into the variable 'pay_cash' as a float.\n
    
    Then we again call the calculations module this time to use the 'calc_IGTF' function, and save its value into the variable 'IGTF'.\n
    
    We call again the calculations module, this time to calculate the retention of the values using the 'calc_Retention' function.
    And save the return values into 'reten_IVA' & 'reten_Total'.\n

    With those 2 values we then call again the calculations module, to use the 'GUI_print_Reten_Bill' function, using as arguments 
    the previous variables (sub_total_float, reten_IVA, pay_cash, IGTF, reten_Total), saving the return text value into 'reten_result'.\n
     
    Then the variables used as arguments on the 'calculations.GUI_print_Reten_Bill' are saved into the global variables 'my_list'.\n
    
    Now the value saved into 'reten_result' variable, is used into a Label to print the result into the main window. Using again grid.\n
    
    After the label is shown into the window the state of the 'change_rate_button' is change from: DISABLE into 'normal'.\n

    The rest of the function is the same but, depending on the values of the 'main_question' & 'agent_of_retention' tkinter.messageboxes.
    It would use the module calculations 'GUI_print_Reten_Bill' or 'GUI_print__Bill'.\n
    Saving an individual 'my_list' for each case, to be use later into the function 'clicked'.

    """

    global my_list, main_question, agent_of_retention
    sub_total_float = float(sub_total.get())
    
    IVA, total = calculations.principal_Calculation(sub_total_float)
    principal_calculation = calculations.GUI_principal_Calculation(sub_total_float, IVA, total)
    Label(window, text=principal_calculation, font=('Roboto', 10), justify=RIGHT, borderwidth=1,width=60, height=result_height, relief='solid' ).grid(row=3)
    main_question = tkinter.messagebox.askquestion('',"This bill is going to be cancel with $?")
    agent_of_retention = tkinter.messagebox.askquestion('', "Do you wanna calculate the retention?")
    
    if main_question == 'yes' and agent_of_retention == 'yes':
        pay_cash = simpledialog.askfloat("Input", "Please how much is going to be cancel on $?:")
        
        IGTF = calculations.calc_IGTF(pay_cash)
        reten_IVA, reten_Total = calculations.calc_Retention(sub_total_float, IVA)
        reten_result = calculations.GUI_print_Reten_Bill(sub_total_float, reten_IVA, pay_cash, IGTF, reten_Total)
        my_list = [sub_total_float, IVA, pay_cash, IGTF, total]

        Label(window, text=reten_result, font=('Roboto', 10), justify=RIGHT, borderwidth=1,width=70, height=result_height, relief='solid', bg='yellow').grid(row= 3, column=1)
        change_rate_button.config(state='normal')
        
    elif main_question == 'yes' and agent_of_retention == 'no':
        pay_cash = simpledialog.askfloat("Input", "Please how much is going to be cancel on $?:")

        IGTF = calculations.calc_IGTF(pay_cash)
        result = calculations.GUI_print_Bill(sub_total_float, IVA, pay_cash, IGTF, total) 
        my_list = [sub_total_float, IVA, pay_cash, IGTF, total]

        Label(window, text=result, font=('Roboto', 10), justify=RIGHT, borderwidth=1,width=70, height=result_height, relief='solid', bg='yellow').grid(row= 3, column=1)
        change_rate_button.config(state='normal')
    
    elif main_question == 'no' and agent_of_retention == 'yes':
        reten_IVA, reten_Total = calculations.calc_Retention(sub_total_float, IVA)
        reten_result = calculations.GUI_print_Reten_Bill(sub_total_float,reten_IVA,0,0,reten_Total)
        my_list = [sub_total_float, IVA, 0, 0, total]

        Label(window, text=reten_result, font=('Roboto', 10), justify=RIGHT, borderwidth=1,width=70, height=result_height, relief='solid', bg='yellow').grid(row= 3, column=1)
        change_rate_button.config(state='normal')
    
    elif main_question == 'no' and agent_of_retention == 'no':
        result = calculations.GUI_print_Bill(sub_total_float, IVA, 0, 0, total)
        my_list = [sub_total_float, IVA, 0, 0, total]

        Label(window, text=result, font=('Roboto', 10), justify=RIGHT, borderwidth=1,width=70, height=result_height, relief='solid', bg='yellow').grid(row= 3, column=1)
        change_rate_button.config(state='normal')

# WIP Fix documentation of the function.
def clicked(): 
    """ 
    This function works in the next way. 
    Is called on the button command of 'chang_rate_button'.
    Check the value of the global variable 'agent_of_retention'.
    Depending on the value of 'agent_of_retention' it would take a 'my_list' of the previous function and do the next:

    Case 1 'agent_of_retention' == 'no':
        It would call the calculations module 
        to use the 'convert_to_bolivars' function using the variables 'my_list' & 'BCV_Price' as arguments,
        ('my_list' values would depend on the selection of 'main_question' & 'agent_of_retention' on the previous function).
        saving the return values into a separate variables (sub_total_BS,  IVA_BS, pay_cash_BS, IGTF_BS, total_BS).
        
        Then calling again the calculations module we would use the 'GUI_print_Bill'. Using as arguments the separate variables
        (sub_total_BS,  IVA_BS, pay_cash_BS, IGTF_BS, total_BS)
        Saving the returned text into a variable called 'result_BS'.
        Then created a Label similiar to the previous function, replacing those values with the converted ones.
         

    Case 2 'agent_of_retention' == 'yes':
        It would call the calculations module 
        to use the 'convert_to_bolivars' function using the variables 'my_list' & 'BCV_Price' as arguments,
        ('my_list' values would depend on the selection of 'main_question' & 'agent_of_retention' on the previous function).
        saving the return values into a separate variables (sub_total_BS,  IVA_BS, pay_cash_BS, IGTF_BS, total_BS).
        
        Then calling again the calculations module we would use the 'GUI_print_Reten_Bill'. Using as arguments the separate variables
        (sub_total_BS,  IVA_BS, pay_cash_BS, IGTF_BS, total_BS)
        Saving the returned text into a variable called 'result_reten_BS'.
        Then created a Label similiar to the previous function, replacing those values with the converted ones.
    
    """

    if agent_of_retention == 'no':
        sub_total_BS,  IVA_BS, pay_cash_BS, IGTF_BS, total_BS = calculations.convert_to_Bolivars(my_list, BCV_Price)
        results_BS = calculations.GUI_print_Bill(sub_total_BS ,IVA_BS, pay_cash_BS, IGTF_BS, total_BS)
        Label(window, text=results_BS, font=('Roboto', 10), justify=RIGHT, borderwidth=1,width=70, height=result_height, relief='solid', bg='yellow').grid(row= 3, column=1)

    if agent_of_retention == 'yes':
        sub_total_BS,  IVA_BS, pay_cash_BS, IGTF_BS, total_BS = calculations.convert_to_Bolivars(my_list, BCV_Price)
        results_reten_BS = calculations.GUI_print_Reten_Bill(sub_total_BS ,IVA_BS, pay_cash_BS, IGTF_BS, total_BS)
        Label(window, text=results_reten_BS, font=('Roboto', 10), justify=RIGHT, borderwidth=1,width=70, height=result_height, relief='solid', bg='yellow').grid(row= 3, column=1)

# Windows entity  
window = Tk()

# Config of window
icon = PhotoImage(file='src\\icon.png')
window.title('IGTF Calculator')
window.iconphoto(True, icon)
window.geometry('800x360')

# Creating Labels
question = Label(window, 
                text='Please how much is the sub total on $?:',
                font=('Roboto', 14),
                justify='left',
                width=35)
sub_total = Entry(window, 
                  font=('Arial', 18),
                  width=20,
                  bg='red',
                  justify='center')
result = Label(window, 
                text='result',
                font=('Roboto', 14),
                relief='raised',
                justify='left',
                anchor='w',
                bg='red',
                width=50  )
user = Label(window, 
             text=user_name, 
             font=('Roboto', 24), 
             activebackground='blue')
version = Label(window, text='Version: alpha-1.01')

# Creating Buttons
calculate_button = Button(window, text='Calculate', command=get_sub_total, width=15)
delete_button = Button(window, text='Deleted')
export_button = Button(window, text='Export')
change_rate_button = Button(window, text='$ / BS', font=('Roboto', 12), command=clicked, state=DISABLED)

# Position of Widgets
question.grid(row=0 , column=0, sticky='nwse')
sub_total.grid(row=1, column=0, sticky='nwe')
sub_total.focus_set() # Focus the entry on the window to instanly put a value.
calculate_button.grid(row=2, column=0, sticky='nwse')
change_rate_button.grid(row=5, column=1, padx= 2, pady=2, sticky='se')
version.grid(row=5, column=0, sticky='ws')

# Config Grid of the window
window.columnconfigure((0,1), weight= 1, uniform= 'a')
window.rowconfigure(4, weight= 10, uniform= 'a')
# window.rowconfigure(0, weight=1, uniform='b')
# window.rowconfigure(1, weight=1, uniform='b')
# window.rowconfigure(2, weight=3, uniform='b')

# Run
window.mainloop()