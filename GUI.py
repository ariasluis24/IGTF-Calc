from tkinter import *
from tkinter import simpledialog
from multiprocessing import Process, Queue
from configparser import ConfigParser
import tkinter.messagebox, os, time, datetime
import src.calculations as calculations

inicio = time.time()
# TODO work on how to handle exceptions. 
#// TODO Show selected options (agent_of_retention, igtf_question)
#// TODO Show BCV Price with date. check
# Variables
#// TODO Look for a way to get the value of the thread or look video on multitasking.
config = ConfigParser()
file = 'src\\config.ini'
config.read(file)

now = datetime.datetime.now()
date_actual = now.strftime('%d-%m-%y')
user_name = os.getlogin()
result_height = 14 # Used into the height of the Labels.
converted = False
# WIP make the sub_total Entry work only if a valid value.
# Try to use Try and Exception ValueError.
def get_sub_total():
    """
    # This function works in the next way.\n
   
    Is called on the button command of 'calculate_button'.\n
    
    Create 3 global variables (my_list, igtf_question, agent_of_retention).\n
    
    Gets the value of the entry 'sub_total'. Converts the value into float and storage it into the 'sub_total_float' variable.\n
    
    Calls the module 'calculations' to use 'principal_Calculation' function and calculate
    the main values using 'sub_total_float' as an argument and storage the result, into 2 separate variables (IVA, total).\n
     
    Calls the module 'calculations' to use 'GUI_principal_Calculation' function and storage the returned 
    text value on the 'principal_calculation' variable, using as arguments the previous variables 'sub_total_float', 'IVA', 'total'.\n
    
    Creates a Label to print in the window the 'GUI_principal_Calculation' returned text, and then storage into 'principal_calculation' variable.
    The label contains its own configuration such as font, border, width, height, relief. And its put it into the window 
    using grid.\n
    
    2 tkinter.messageboxes, asking a yes/no question are created saving their return values into the 2 global variables (igtf_question, agent_of_retention) for further use.\n
    
    Depending on the values of the tkinter.messageboxes (igtf_question, agent_of_retention), the program would ask using a simpledialog for a value, which is goin
    to be saved into the variable 'pay_cash' as a float.\n
    
    Then we again call the calculations module this time to use the 'calc_IGTF' function, and save its value into the variable 'IGTF'.\n
    
    We call again the calculations module, this time to calculate the retention of the values using the 'calc_Retention' function.
    And save the return values into 'reten_IVA' & 'reten_Total'.\n

    With those 2 values we then call again the calculations module, to use the 'GUI_print_Reten_Bill' function, using as arguments 
    the previous variables (sub_total_float, reten_IVA, pay_cash, IGTF, reten_Total), saving the return text value into 'reten_result'.\n
     
    Then the variables used as arguments on the 'calculations.GUI_print_Reten_Bill' are saved into the global variables 'my_list'.\n
    
    Now the value saved into 'reten_result' variable, is used into a Label to print the result into the main window. Using again grid.\n
    
    After the label is shown into the window the state of the 'change_rate_button' is change from: DISABLE into 'normal'.\n

    The rest of the function is the same but, depending on the values of the 'igtf_question' & 'agent_of_retention' tkinter.messageboxes.
    It would use the module calculations 'GUI_print_Reten_Bill' or 'GUI_print__Bill'.\n
    Saving an individual 'my_list' for each case, to be use later into the function 'convert_bs_dollars'.

    """

    global my_list, igtf_question, agent_of_retention, principal_result_label, total_result_label
    sub_total_float = float(sub_total.get())
    
    IVA, total = calculations.principal_Calculation(sub_total_float)
    principal_calculation = calculations.GUI_principal_Calculation(sub_total_float, IVA, total)
    
    principal_result_label.config(text=principal_calculation)
    principal_result_label.grid(column=0, row=5)
    
    igtf_question = tkinter.messagebox.askquestion('',"This bill is going to be cancel with $?")
    agent_of_retention = tkinter.messagebox.askquestion('', "Do you wanna calculate the retention?")
    
    if igtf_question == 'yes' and agent_of_retention == 'yes':
        agent_of_retention_label_answer.config(text='YES', bg='green')
        igtf_label_answer.config(text='YES', bg='green')

        pay_cash = simpledialog.askfloat("Input", "Please how much is going to be cancel on $?:")
        
        IGTF = calculations.calc_IGTF(pay_cash)
        reten_IVA, reten_Total = calculations.calc_Retention(sub_total_float, IVA)
        reten_result = calculations.GUI_print_Reten_Bill(sub_total_float, reten_IVA, pay_cash, IGTF, reten_Total)
        my_list = [sub_total_float, IVA, pay_cash, IGTF, total]

        total_result_label.config(text=reten_result)
        total_result_label.grid(row= 5, column=1)
        
        change_rate_button.config(state='normal')
        
    elif igtf_question == 'yes' and agent_of_retention == 'no':
        agent_of_retention_label_answer.config(text='NO', bg='red')
        igtf_label_answer.config(text='YES', bg='green')

        pay_cash = simpledialog.askfloat("Input", "Please how much is going to be cancel on $?:")

        IGTF = calculations.calc_IGTF(pay_cash)
        result = calculations.GUI_print_Bill(sub_total_float, IVA, pay_cash, IGTF, total) 
        my_list = [sub_total_float, IVA, pay_cash, IGTF, total]

        total_result_label.config(text=result)
        total_result_label.grid(row= 5, column=1)

        change_rate_button.config(state='normal')
    
    elif igtf_question == 'no' and agent_of_retention == 'yes':
        agent_of_retention_label_answer.config(text='YES', bg='green')
        igtf_label_answer.config(text='NO', bg='red')

        reten_IVA, reten_Total = calculations.calc_Retention(sub_total_float, IVA)
        reten_result = calculations.GUI_print_Reten_Bill(sub_total_float,reten_IVA,0,0,reten_Total)
        my_list = [sub_total_float, IVA, 0, 0, total]

        total_result_label.config(text=reten_result)
        total_result_label.grid(row= 5, column=1)
        
        change_rate_button.config(state='normal')
    
    elif igtf_question == 'no' and agent_of_retention == 'no':
        agent_of_retention_label_answer.config(text='NO', bg='red')
        igtf_label_answer.config(text='NO', bg='red')

        result = calculations.GUI_print_Bill(sub_total_float, IVA, 0, 0, total)
        my_list = [sub_total_float, IVA, 0, 0, total]

        total_result_label.config(text=result)
        total_result_label.grid(row= 5, column=1)
        
        change_rate_button.config(state='normal')

# WIP Fix documentation of the function.
#/// TODO Investigate bug symbol displayed on convertion button when a convertion has already been done.
def convert_bs_dollars(BCV_Price): 
    """ 
    This function works in the next way. 
    Is called on the button command of 'chang_rate_button'.
    Check the value of the global variable 'agent_of_retention'.
    Depending on the value of 'agent_of_retention' it would take a 'my_list' of the previous function and do the next:

    Case 1 'agent_of_retention' == 'no':
        It would call the calculations module 
        to use the 'convert_to_bolivars' function using the variables 'my_list' & 'BCV_Price' as arguments,
        ('my_list' values would depend on the selection of 'igtf_question' & 'agent_of_retention' on the previous function).
        saving the return values into a separate variables (sub_total_BS,  IVA_BS, pay_cash_BS, IGTF_BS, total_BS).
        
        Then calling again the calculations module we would use the 'GUI_print_Bill'. Using as arguments the separate variables
        (sub_total_BS,  IVA_BS, pay_cash_BS, IGTF_BS, total_BS)
        Saving the returned text into a variable called 'result_BS'.
        Then created a Label similiar to the previous function, replacing those values with the converted ones.
         

    Case 2 'agent_of_retention' == 'yes':
        It would call the calculations module 
        to use the 'convert_to_bolivars' function using the variables 'my_list' & 'BCV_Price' as arguments,
        ('my_list' values would depend on the selection of 'igtf_question' & 'agent_of_retention' on the previous function).
        saving the return values into a separate variables (sub_total_BS,  IVA_BS, pay_cash_BS, IGTF_BS, total_BS).
        
        Then calling again the calculations module we would use the 'GUI_print_Reten_Bill'. Using as arguments the separate variables
        (sub_total_BS,  IVA_BS, pay_cash_BS, IGTF_BS, total_BS)
        Saving the returned text into a variable called 'result_reten_BS'.
        Then created a Label similiar to the previous function, replacing those values with the converted ones.
    
    """
    global converted, total_result_label

    if agent_of_retention == 'no' and converted == False:
        change_rate_button.config(text='$')
        
        converted = True
        
        sub_total_BS,  IVA_BS, pay_cash_BS, IGTF_BS, total_BS = calculations.convert_to_Bolivars(my_list, BCV_Price)
        results_BS = calculations.GUI_print_Bill(sub_total_BS ,IVA_BS, pay_cash_BS, IGTF_BS, total_BS)
        
        total_result_label.config(text=results_BS)
        total_result_label.grid(row= 5, column=1)
        

    elif agent_of_retention == 'yes' and converted == False:
        change_rate_button.config(text='$')
        
        converted = True
        
        sub_total_BS,  IVA_BS, pay_cash_BS, IGTF_BS, total_BS = calculations.convert_to_Bolivars(my_list, BCV_Price)
        results_reten_BS = calculations.GUI_print_Reten_Bill(sub_total_BS ,IVA_BS, pay_cash_BS, IGTF_BS, total_BS)
        
        total_result_label.config(text=results_reten_BS)
        total_result_label.grid(row= 5, column=1)
        
    
    elif agent_of_retention == 'no' and converted == True:
        change_rate_button.config(text='Bs')
        
        converted = False
        
        sub_total,  IVA, pay_cash, IGTF, total = my_list 
        results = calculations.GUI_print_Bill(sub_total ,IVA, pay_cash, IGTF, total)
        
        total_result_label.config(text=results)
        total_result_label.grid(row= 5, column=1)
        

    
    elif agent_of_retention == 'yes' and converted == True:
        change_rate_button.config(text='Bs')
        
        converted = False
        
        sub_total,  IVA, pay_cash, IGTF, total = my_list
        results_reten = calculations.GUI_print_Reten_Bill(sub_total ,IVA, pay_cash, IGTF, total)
        
        total_result_label.config(text=results_reten)
        total_result_label.grid(row= 5, column=1)

  
def delete():
    global converted, total_result_label
    
    sub_total.delete(0,END)
    # total_result_label.config(text='', borderwidth=0, bg='#f1f1f0')
    principal_result_label.grid_forget()
    total_result_label.grid_forget()

    change_rate_button.config(text='Bs', state='disabled')
    
    converted = False

def update():
    # window.after(1000, update) #Constanly updates the config of the price label and change_rate_button. 
    # print('HOla') Debbuger 
    
    # Scrap code
    # Queue to find the result on the scraping of the BCV price when is done.
    if config['Date']['date_now'] == date_actual:
        # Takes the values from the src\config.ini because is the same date and it doesnt need the scraped value.
        BCV_Price = float(config['BCV_Price']['bcv_price'])
        
        # Update labels with scrap BCV Price.
        price.config(text=f'Date: {date_actual} BCV: {BCV_Price:.5f}', font=('Roboto', 10, 'bold'))
        
        # Adds function to the change rate button.
        change_rate_button.config(command=lambda: convert_bs_dollars(BCV_Price))  
    
    else:
        # Starts the scrap from the BCV webpage.
        Q = Queue()
        import src.scrap_price_BCV as BCV
        scrap = Process(target=BCV.scraping_BCV, args=(Q,))
        scrap.start()
        BCV_Price = Q.get()
        scrap.kill()
        
        # Update labels with scrap BCV Price.
        price.config(text=f'Date: {date_actual} BCV: {BCV_Price}', font=('Roboto', 10, 'bold'))
        change_rate_button.config(command=lambda: convert_bs_dollars(BCV_Price))  


# Windows entity  
window = Tk()

# Config of window
icon = PhotoImage(file='src\\icon.png')
window.title('IGTF Calculator')
window.iconphoto(True, icon)
window.geometry('800x370') # Default size of the window
window.minsize(800, 370) # Minimun size of the window
window.maxsize(800, 370) # Maximun size of the window

# Creating Labels
question = Label(window, 
                text='Please how much is the sub total on $?:',
                font=('Roboto', 14),
                justify='left',
                width=35)
sub_total = Entry(window, 
                  font=('Arial', 18),
                  width=20,
                  bg='yellow',
                  justify='center')
result = Label(window, 
                text='result',
                font=('Roboto', 14),
                relief='raised',
                justify='left',
                anchor='w',
                bg='red',
                width=50  )
agent_of_retention_label = Label(window, text='AGENT OF RETENTION: ', font=('Roboto', 11))
agent_of_retention_label_answer = Label(window, text='', font=('Roboto', 12, 'bold') )
igtf_label = Label(window, text='IGTF: ', font=('Roboto', 11) )
igtf_label_answer = Label(window, text='', font=('Roboto', 12, 'bold'))
principal_result_label = Label(window, text='', font=('Roboto', 10), justify=RIGHT, borderwidth=1,width=60, height=result_height, relief='solid' )
total_result_label = Label(window, text='', font=('Roboto', 10), justify=RIGHT, borderwidth=1,width=70, height=result_height, relief='solid', bg='yellow')
user = Label(window, 
             text=user_name, 
             font=('Roboto', 24), 
             activebackground='blue')
version = Label(window, text='Version: alpha-1.020')
price = Label(window, text='Loading...')

# Creating Buttons
calculate_button = Button(window, text='Calculate', command=get_sub_total, width=10)
delete_button = Button(window, text='Delete', command=delete,width=10)
export_button = Button(window, text='Export') # TODO Make a way to expor the calculation into a pdf or txt file.
change_rate_button = Button(window, text='Bs', font=('Roboto', 12),command='' , width=5, state=DISABLED) # TODO Make changable values between BS/$

# Position of Widgets
question.grid(row=0 , column=0, sticky='nwse')
sub_total.grid(row=1, column=0, pady=5,sticky='ns')

agent_of_retention_label.grid(row=0, column=1,sticky='w')
agent_of_retention_label_answer.grid(row=0, column=1, padx=173, sticky='w' )
igtf_label.grid(row=1, column=1, sticky='w')
igtf_label_answer.grid(row=1, column=1, padx=45, sticky='w')

calculate_button.grid(row=2, column=0, padx=110,sticky='es')
delete_button.grid(row=2, column=0, padx=110,sticky='ws')

change_rate_button.grid(row=6, column=1, padx= 2, pady=2, sticky='se')
version.grid(row=6, column=0, sticky='ws', )
price.grid(row=6, column=0, sticky='es')

# Config Grid of the window
sub_total.focus_set() # Focus the entry on the window to instanly put a value.
window.columnconfigure((0,1), weight= 1, uniform= 'a')
window.rowconfigure(4, weight= 10, uniform= 'a')
# window.rowconfigure(0, weight=1, uniform='b')
# window.rowconfigure(1, weight=1, uniform='b')
# window.rowconfigure(2, weight=3, uniform='b')

final = time.time()
if __name__ == '__main__':
    # Debugger timer to calc init of the mainloop
    print("Ejecucion del GUI: ")
    print(final - inicio)

    # Update price label with the scraped BCV Price.
    window.after(1000, update)

    #Runs window.
    window.mainloop()