# Import to set the locale system for de decimal(,) and thousand(.) separators.
import locale
locale.setlocale(locale.LC_ALL, 'en_DE')

def principal_Calculation(sub_total):

    IVA = sub_total * 0.16
    total = sub_total + IVA

    print(f'Sub-Total:    {round(sub_total,2):n}')
    print(f' IVA(16%):      {round(IVA,2):n}')
    print(f'    Total:    {round(total,2):n}')

def calc_Retention(sub_total, iva ):
    iva_25 = iva * 0.25
    total_reten = sub_total + iva_25
    return print(f'The total of bill with retention is: {total_reten:n}')

def dollars_Calculation(pay_Cash):
    IGTF = pay_Cash * 0.03
    return print(f'The IGTF is: {IGTF:n}')

while True:
    #Variables WIP
    BCV_Rate = 36.2760
    sub_total = 0
    IVA = sub_total * 0.16

    #Program WIP
    main_Question = input('This bill is going to be cancel with $? (Y/N): ')
    if len(main_Question) == 1 and main_Question.lower() == 'y':
        #Text printed on the console
        print('This bill is going to be cancel with Dollars.')

        #Calculations
        sub_total = float(input('Please how much is the sub total?: '))

        principal_Calculation(sub_total)
        calc_Retention(sub_total, IVA)

        pay_Cash = float(input('Please how much is going to be cancel on $?: '))
        dollars_Calculation(pay_Cash)
        pass

    elif len(main_Question) == 1 and main_Question.lower() == 'n':
        print('This bill is going to be cancel with Bolivars.')
        pass
    else:
        print('Please select a valid option...')
        pass
