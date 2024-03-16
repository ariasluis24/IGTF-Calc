# Import to set the locale system for de decimal(,) and thousand(.) separators.
import locale
locale.setlocale(locale.LC_ALL, 'en_DE')

def principal_Calculation(sub_total):

    IVA = sub_total * 0.16
    total = sub_total + IVA
    print(f'\nSub-Total:    {round(sub_total,2):n}')
    print(f' IVA(16%):     {round(IVA,2):n}')
    print(f'    Total:    {round(total,2):n}\n')
    return total

def calc_Retention(sub_total, iva ):
    iva_25 = iva * 0.25
    total_reten = sub_total + iva_25
    print("\n************************************")
    print(f'\nThe total of bill with retention is: {total_reten:n}')
    print("\n************************************")
    return total_reten

def dollars_Calculation(pay_Cash):
    IGTF = pay_Cash * 0.03
    print("\n************************************")
    print(f'\nThe IGTF is:    {IGTF:n}')
    print("\n************************************")
    return IGTF

def show_Reten_Bill_Details(sub_total, iva, igtf):
    print("THE DETAILS OF THE RETENTION BILL")
    print(f'Sub-Total:        {round(sub_total,2):n}')
    print(f' IVA(25%):          {round(iva,2)*0.25:n}')
    print(f'Retention Total:  {round(sub_total + iva,2):n}')
    print(f'IGTF: {pay_Cash} (3%): {round(igtf,2):n}')
    print("\n************************************\n")
    print(f'Retention Total + IGTF:  {round(total + igtf,2):n}')
    print("\n************************************")

def show_Total_Bill_Details(sub_total,iva,total,igtf):
    print("THE DETAILS OF THE TOTAL BILL")
    print(f'Sub-Total:    {round(sub_total,2):n}')
    print(f' IVA(16%):    {round(iva,2):n}')
    print(f'    Total:    {round(total,2):n}')
    print(f'IGTF: {pay_Cash}(3%): {round(igtf,2):n}')
    print("\n************************************")
    print(f'Total + IGTF: {round(total + igtf,2):n}')
    print("\n************************************")
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

        if len(agent_of_retention) == 1 and agent_of_retention.lower() == 'y':
            # iva_retention = calc_Retention(sub_total, IVA) / 1.25
            calc_Retention(sub_total, IVA)
            show_Reten_Bill_Details(sub_total, IVA,IGTF)
            break
        elif len(agent_of_retention) == 1 and agent_of_retention.lower() == 'n':
            print('Calculation of retention pass')
        pass

        show_Total_Bill_Details(sub_total,IVA,total,IGTF)
        pass

    elif len(main_Question) == 1 and main_Question.lower() == 'n':
        print('This bill is going to be cancel with Bolivars.')
        pass
    else:
        print('Please select a valid option...')
        pass
