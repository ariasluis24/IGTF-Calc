# Import to set the locale system for de decimal(,) and thousand(.) separators.
import locale
locale.setlocale(locale.LC_ALL, 'en_DE')

def principal_Calculation(sub_total):

    IVA = sub_total * 0.16
    total = sub_total + IVA
    print(f'\nSub-Total:    {round(sub_total,3):n}')
    print(f' IVA(16%):     {round(IVA,2):n}')
    print(f'    Total:    {round(total,2):n}\n')
    return total, IVA

def dollars_Calculation(pay_Cash):
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
    return total_reten


def show_Reten_Bill_Details(sub_total, reten_iva, igtf):
    print("\n\nTHE DETAILS OF THE RETENTION BILL")
    print(f'Sub-Total:        ${round(sub_total,2):n}')
    print(f' IVA(25%):          ${round(reten_iva,2):n}')
    print(f'Retention Total:  ${round(sub_total + reten_iva,2):n}')
    print(f'IGTF: ${pay_Cash:n} (3%): ${round(igtf,2):n}')
    print("\n************************************\n")
    print(f'Retention Total + IGTF:  ${round(sub_total + reten_iva + igtf,2):n}')
    print("\n************************************")
    print(f"The rest to pay is: ${pay_Cash - (sub_total + reten_iva + igtf):n}")

def show_Bill_Detail(agent_of_retention,sub_total, iva, IGTF):
    if len(agent_of_retention) == 1 and agent_of_retention.lower() == 'y':
        total_retention = calc_Retention(sub_total, IVA) - sub_total
        show_Reten_Bill_Details(sub_total, total_retention,IGTF)
        pass
    elif len(agent_of_retention) == 1 and agent_of_retention.lower() == 'n':
        print('\nCalculation of retention pass\n')
        print("THE DETAILS OF THE TOTAL BILL")
        print(f'Sub-Total:    ${round(sub_total,2):n}')
        print(f' IVA(16%):    ${round(iva,2):n}')
        print(f'    Total:    ${round(total,2):n}')
        print(f'IGTF: {pay_Cash:n} (3%): ${round(IGTF,2):n}')
        print("\n************************************\n")
        print(f'Total + IGTF: ${round(total + IGTF,2):n}')
        print("\n************************************")
        print(f"The rest to pay is: ${pay_Cash - (total + IGTF):n}\n")
    pass

while True:
    #Variables WIP
    BCV_Rate = 36.2760
    sub_total = 0
    IVA = 0
    total = sub_total + IVA

    #Program WIP
    main_Question = input('This bill is going to be cancel with $? (Y/N): ')
    if len(main_Question) == 1 and main_Question.lower() == 'y':
        #Text printed on the console
        print('This bill is going to be cancel with Dollars.')

        #Calculations
        sub_total = float(input('Please how much is the sub total?: '))
         
        total = principal_Calculation(sub_total)
        IVA = total - sub_total

        #Agent of retention case:
        agent_of_retention = input('Do you want to calc the retention?(Y/N): ')

        pay_Cash = float(input('Please how much is going to be cancel on $?: '))
        IGTF = dollars_Calculation(pay_Cash)

        show_Bill_Detail(agent_of_retention,sub_total,IVA,IGTF)

        pass

    elif len(main_Question) == 1 and main_Question.lower() == 'n':
        print('This bill is going to be cancel with Bolivars.')
        pass
    else:
        print('Please select a valid option...')
        pass
