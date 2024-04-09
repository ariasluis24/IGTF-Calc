#IGTF-Calc 
#ver: alpha-0.77 
import calculations, datetime
now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y %H-%M-%S")
while True:
    # Variables WIP
    name_file = f'Bill-{date}.txt'
    # Program WIP
    sub_total = calculations.is_Float_Loop('Please how much is the sub total on $?: ')
    # Calculations
    IVA, total = calculations.principal_Calculation(sub_total)
    # TODO Create program to create an external PDF file.
    # Write method to write file in an external txt file.
    with open(f'Bills\\Bill-{sub_total:n}$ {name_file}', 'w') as file:
        file.write(str(calculations.txt_Bill(sub_total, IVA, total)))
    # Main Question
    main_Question = calculations.question_Loop('This bill is going to be cancel with $? (Y/N): ')
    # Agent of retention case:
    agent_of_retention = calculations.question_Loop('Do you want to calc the retention?(Y/N): ')
    calculations.main_Function(main_Question,agent_of_retention,sub_total,IVA,total)
    # Convertion to Bs
    # convert_to_bolivars = calculations.to_Bolivars()