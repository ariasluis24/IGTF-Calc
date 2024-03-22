#IGTF-Calc 
#ver: alpha-0.74 
import calculations
while True:
    #Variables WIP
    BCV_Rate = 36.2760
    #Program WIP
    sub_total = calculations.is_Float_Loop('Please how much is the sub total?: ')
    #Calculations
    IVA, total = calculations.principal_Calculation(sub_total)
    #Main Question
    main_Question = calculations.question_Loop('This bill is going to be cancel with $? (Y/N): ')
    #Agent of retention case:
    agent_of_retention = calculations.question_Loop('Do you want to calc the retention?(Y/N): ')
    calculations.main_Function(main_Question,agent_of_retention,sub_total,IVA,total)