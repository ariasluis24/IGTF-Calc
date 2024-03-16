import locale
locale.setlocale(locale.LC_ALL, 'en_DE')

while True:
    #Variables
    BCV_Rate = 36.2760
    IGTF = 0
    Sub_total = 0
    IVA = Sub_total * 0.16
    Total = Sub_total + IVA
    Pay_Cash = 0
    
    #Program
    prompt = input('This bill is going to be cancel with $? (Y/N): ')
    if len(prompt) == 1 and prompt.lower() == 'y':
        print('This bill is going to be cancel with Dollars.')
        Sub_total = float(input('Please how much is the sub total?: '))
        IVA = Sub_total * 0.16
        Total = Sub_total + IVA
        # print(Total)
        # US_Total ='{:.2f}'.format(Total).replace('.', ',')
        # US_Total_final = float(US_Total)
        print(f'The total is {Total:n}')
        # print(type(US_Total_final))
        # print(f'The total is {format(Total,'.')}')
        pass
    elif len(prompt) == 1 and prompt.lower() == 'n':
        print('This bill is going to be cancel with Bolivars.')
        pass
    else:
        print('Please select a valid option...')
        pass
