import calculations
while True:
    #Variables WIP
    BCV_Rate = 36.2760

    #Program WIP
    #Calculations
    sub_total = float(input('Please how much is the sub total?: '))

    IVA, total = calculations.principal_Calculation(sub_total)
    #Main Question
    main_Question = input('This bill is going to be cancel with $? (Y/N): ')

    #Agent of retention case:
    agent_of_retention = input('Do you want to calc the retention?(Y/N): ')

    calculations.main_Function(main_Question,agent_of_retention,sub_total,IVA,total)
    
    # if len(main_Question) == 1 and main_Question.lower() == 'y':
    #     #Text printed on the console
    #     print('\nTHIS BILL IS GOING TO BE CANCEL ON DOLLARS!\n')

    #     pay_Cash = float(input('Please how much is going to be cancel on $?: '))
    #     IGTF = dollars_Calculation(pay_Cash)
    #     show_Bill_Detail(agent_of_retention,sub_total,IVA,IGTF)
    #     pass

    # elif len(main_Question) == 1 and main_Question.lower() == 'n':
    #     results_reten = calc_Retention(sub_total,IVA)
    #     print('\nThis bill is going to be cancel with Bolivars.\n')
    #     print_Bill(agent_of_retention,sub_total,IVA,total)
    #     pass
    # else:
    #     print('Please select a valid option...')
    #     pass
