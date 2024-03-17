# Import to set the locale system for de decimal(,) and thousand(.) separators.
import locale
locale.setlocale(locale.LC_ALL, 'en_DE')

def principal_Calculation(sub_total):
    IVA = sub_total * 0.16
    total = sub_total + IVA
    print(f'\nSub-Total:    {round(sub_total,3):n}')
    print(f' IVA(16%):     {round(IVA,2):n}')
    print(f'    Total:    {round(total,2):n}\n')
    return IVA, total

def calc_IGTF(pay_Cash):
    IGTF = pay_Cash * 0.03
    # print("\n************************************")
    # print(f'\nThe IGTF is:    {IGTF:n}')
    # print("\n************************************")
    return IGTF

def calc_Retention(sub_total, iva ):
    iva_25 = iva * 0.25
    total_reten = sub_total + iva_25
    # print("\n************************************")
    # print(f'\nThe total of bill with retention is: {total_reten:n}')
    # print("\n************************************")
    return iva_25, total_reten


def rest_to_Pay(pay_cash,total):
    # print(f'The resto to pay is:{}')
    pass

def main_Function(main_Question, agent_of_retention, sub_total, IVA,total):
    if len(main_Question) == 1 and main_Question.lower() == 'y' and agent_of_retention.lower() == 'y':
        reten_Results = calc_Retention(sub_total,IVA)
        reten_IVA, reten_Total = reten_Results
        pay_Cash = float(input('Please how much is going to be cancel on $?: '))
        IGTF = calc_IGTF(pay_Cash)
        print_Reten_Bill(sub_total, reten_IVA, pay_Cash, IGTF, reten_Total)

    elif len(main_Question) == 1 and main_Question.lower() == 'y' and agent_of_retention.lower() == 'n':
        pay_Cash = float(input('Please how much is going to be cancel on $?: '))
        IGTF = calc_IGTF(pay_Cash)
        print_Bill(sub_total, IVA, pay_Cash,IGTF,total)
    elif len(main_Question) == 1 and main_Question.lower() == 'n' and agent_of_retention.lower() == 'y':
        
        reten_Results = calc_Retention(sub_total,IVA)
        reten_IVA, reten_Total = reten_Results
        print_Reten_Bill(sub_total, reten_IVA, 0,0,reten_Total)

    elif len(main_Question) == 1 and main_Question.lower() == 'n' and agent_of_retention.lower() == 'n':
        print_Bill(sub_total, IVA, 0,0,total)

def print_Bill(sub_total, IVA, pay_Cash,IGTF, total):
    print(f'\nSub-Total:    ${round(sub_total,3):n}')
    print(f' IVA(16%):     ${round(IVA,2):n}')
    print(f'$ Payment:    ${round(pay_Cash,2):n}')
    print(f' IGTF(3%):     ${round(IGTF,2):n}')
    print(f'    Total:    ${round(total+ IGTF,2):n}\n')

def print_Reten_Bill(sub_total, reten_IVA, pay_Cash,IGTF,reten_Total):
    print(f'\n        Sub-Total:     ${round(sub_total,3):n}')
    print(f' Retenied IVA 75%:      ${round(reten_IVA,2):n}')
    print(f'        $ Payment:      ${round(pay_Cash,2):n}')
    print(f'         IGTF(3%):      ${round(IGTF,2):n}')
    print(f'            Total:     ${round(reten_Total+ IGTF,2):n}\n')
