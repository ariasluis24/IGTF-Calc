# Import to set the locale system for the decimal(,) and thousand(.) separators.
import locale, datetime
from decimal import Decimal
from scrap_price_BCV import price_BCV
locale.setlocale(locale.LC_ALL, 'en_DE')
now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y %H-%M-%S")
BCV_Rate = price_BCV

def principal_Calculation(sub_total):
    IVA = sub_total * 0.16
    total = sub_total + IVA
    print('***************NORMAL BILL***************************RETAINED BILL******************')
    print(f'\nSub-Total:    {round(Decimal(sub_total),2):n}          *              Sub-Total:    {round(Decimal(sub_total),2):n}') 
    print(f' IVA(16%):     {round(Decimal(IVA),2):n}          *               IVA(16%):     {round(Decimal(IVA),2):n}') 
    print(f'    Total:    {round(Decimal(total),2):n}          *           Retained IVA:      {round(Decimal(IVA*0.25),2):n}')
    print(f'                              *                  Total:    {round(Decimal(sub_total) + Decimal(IVA*0.25),2):n}\n')
    return IVA, total

def txt_Bill(sub_total, IVA, total):
    return f'''                 Date:{date} Client: -
                ***************NORMAL BILL***************************RETAINED BILL******************
            Sub-Total:    {round(Decimal(sub_total),2):n}          *              Sub-Total:    {round(Decimal(sub_total),2):n}
             IVA(16%):     {round(Decimal(IVA),2):n}          *               IVA(16%):     {round(Decimal(IVA),2):n}
                Total:    {round(Decimal(total),2):n}          *           Retained IVA:     {round(Decimal(IVA*0.25),2):n}
                                          *                  Total:    {round(Decimal(sub_total) + Decimal(IVA*0.25),2):n}\n
    '''

def calc_IGTF(pay_Cash):
    IGTF = pay_Cash * 0.03
    return IGTF

def calc_Retention(sub_total, iva ):
    iva_25 = iva * 0.25
    total_reten = sub_total + iva_25
    return iva_25, total_reten

def is_Float_Loop(question):
    while True:    
        try:
            answer = float(input(question))
            float(answer)
            return answer
        except ValueError:
            print('Please enter a valid option...')
            pass

def question_Loop(question):
    while True:    
        answer = input(question)
        if len(answer) == 1 and answer.lower() == 'y':
            return 'y'
            
        elif len(answer) == 1 and answer.lower() == 'n':
            return 'n'
        else:
            print('Please select a valid option...')

def rest_to_Pay(pay_Cash, IGTF,total):
    print('******************************')
    print(f'The rest to pay is: {round((Decimal(total) + Decimal(IGTF)) - Decimal(pay_Cash),2):n}')
    print('******************************\n')
    pass

# WIP make a loop question asking for a yes or no to convert into bolivars and select a valid option if the answer is not valid.
def main_Function(main_Question, agent_of_retention, sub_total, IVA,total):

    if len(main_Question) == 1 and main_Question.lower() == 'y' and agent_of_retention.lower() == 'y':
        reten_Results = calc_Retention(sub_total,IVA)
        reten_IVA, reten_Total = reten_Results
        pay_Cash = is_Float_Loop('Please how much is going to be cancel on $?: ')
        IGTF = calc_IGTF(pay_Cash)
        print_Reten_Bill(sub_total, reten_IVA, pay_Cash, IGTF, reten_Total)
        rest_to_Pay(pay_Cash, IGTF,reten_Total)
        convert_to_bolivars = input('\nDo you wanna convert theese values to Bolivars? (Y/N): ')
        if convert_to_bolivars.lower() == 'y':
            sub_total, IVA, pay_Cash, IGTF, total = convert_to_Bolivars([sub_total,IVA, pay_Cash, IGTF, total], BCV_Rate)
            print_Bill(sub_total, IVA, pay_Cash, IGTF, total)
        elif convert_to_bolivars.lower() == 'n':
            pass
        else:
            print('Select a Valid Option...')
    elif len(main_Question) == 1 and main_Question.lower() == 'y' and agent_of_retention.lower() == 'n':
        pay_Cash = is_Float_Loop('Please how much is going to be cancel on $?: ')
        IGTF = calc_IGTF(pay_Cash)
        print_Bill(sub_total, IVA, pay_Cash,IGTF,total)
        rest_to_Pay(pay_Cash, IGTF,total)
        convert_to_bolivars = input('\nDo you wanna convert theese values to Bolivars? (Y/N): ')
        if convert_to_bolivars.lower() == 'y':
            sub_total, IVA, pay_Cash, IGTF, total = convert_to_Bolivars([sub_total,IVA, pay_Cash, IGTF, total], BCV_Rate)
            print_Bill(sub_total, IVA, pay_Cash, IGTF, total)
        elif convert_to_bolivars.lower() == 'n':
            pass
        else:
            print('Select a Valid Option...')
    elif len(main_Question) == 1 and main_Question.lower() == 'n' and agent_of_retention.lower() == 'y':
        
        reten_Results = calc_Retention(sub_total,IVA)
        reten_IVA, reten_Total = reten_Results
        print_Reten_Bill(sub_total, reten_IVA, 0,0,reten_Total)
        convert_to_bolivars = input('\nDo you wanna convert theese values to Bolivars? (Y/N): ')
        if convert_to_bolivars.lower() == 'y':
            sub_total, IVA, pay_Cash, IGTF, total = convert_to_Bolivars([sub_total,IVA, 0, 0, total], BCV_Rate)
            print_Bill(sub_total, IVA, pay_Cash, IGTF, total)
        elif convert_to_bolivars.lower() == 'n':
            pass
        else:
            print('Select a Valid Option...')
    elif len(main_Question) == 1 and main_Question.lower() == 'n' and agent_of_retention.lower() == 'n':
        print_Bill(sub_total, IVA, 0,0,total)
        convert_to_bolivars = input('\nDo you wanna convert theese values to Bolivars? (Y/N): ')
        if convert_to_bolivars.lower() == 'y':
            sub_total, IVA, pay_Cash, IGTF, total = convert_to_Bolivars([sub_total,IVA, 0, 0, total], BCV_Rate)
            print_Bill(sub_total, IVA, pay_Cash, IGTF, total)
        elif convert_to_bolivars.lower() == 'n':
            pass
        else:
            print('Select a Valid Option...')
    else:
        print('Please select a valid option...')

def print_Bill(sub_total, IVA, pay_Cash,IGTF, total):
    print(f'\nSub-Total:    ${round(Decimal(sub_total),2):n}')
    print(f' IVA(16%):     ${round(Decimal(IVA),2):n}')
    print(f'$ Payment:    ${round(Decimal(pay_Cash),2):n}')
    print(f' IGTF(3%):      ${round(Decimal(IGTF),2):n}')
    print(f'    Total:    ${round(Decimal(total) + Decimal(IGTF),2):n}\n')

# TODO Use just one format for the bill, switching the iva percentage and value, depending if the user wants to calculate the retention of the iva.
def print_Reten_Bill(sub_total, reten_IVA, pay_Cash,IGTF,reten_Total):
    print(f'\n        Sub-Total:     ${round(Decimal(sub_total),2):n}')
    print(f'        IVA (25%):       ${round(Decimal(reten_IVA),2):n}')
    print(f'        $ Payment:     ${round(Decimal(pay_Cash),2):n}')
    print(f'         IGTF(3%):      ${round(Decimal(IGTF),2):n}')
    print(f'            Total:     ${round(Decimal(reten_Total) + Decimal(IGTF),2):n}\n')

#WIP If it is needed show the values on bolivars at the BCV rate.

def convert_to_Bolivars(data, BCV_Rate):
    my_values = []
    for x in data:
        my_values.append(x * BCV_Rate)
    return my_values
# to_bolivars_lambda = lambda data, BCV_Rate: [x * BCV_Rate for x in data]