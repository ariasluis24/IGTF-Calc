from tkinter import *
import tkinter.messagebox
from tkinter import simpledialog
import src.calculations as calculations

# Variables
converted = False

# TODO WIP make the sub_total Entry work only if a valid value.
# TODO Try to use Try and Exception ValueError.

def get_sub_total(principal_result_label, total_result_label, agent_of_retention_label_answer, igtf_label_answer, change_rate_button ,sub_total):
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

    global my_list, igtf_question, agent_of_retention, converted

    sub_total_float = float(sub_total)

    IVA, total = calculations.principal_Calculation(sub_total_float)
    principal_calculation = calculations.GUI_principal_Calculation(sub_total_float, IVA, total)
    
    principal_result_label.config(text=principal_calculation)
    principal_result_label.grid(row=5)
    
    igtf_question = tkinter.messagebox.askquestion('',"This bill is going to be cancel with $?")
    agent_of_retention = tkinter.messagebox.askquestion('', "Do you wanna calculate the retention?")
    
    change_rate_button.config(text='Bs')   
    converted = False

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


# TODO Fix documentation of the function.
def convert_bs_dollars(BCV_Price, total_result_label, change_rate_button): 
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
    
    global converted

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

        
  