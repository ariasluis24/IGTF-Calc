from tkinter import *
from multiprocessing import Process, Queue
from configparser import ConfigParser
from src.principal_button_command import get_sub_total, convert_bs_dollars
from src.second_button_command import get_payment_done
from src.delete_module import delete, delete_second_UI
from src.about import open_about
from src.check_lang import config_language
import os, time, datetime



inicio = time.time()
# TODO work on how to handle exceptions
# // TODO Reasign functions on GUI.py to indivual modules.
# TODO Rename GUI.py to main.py (If necessary).
# // TODO Create dictionaries to use them for localization (EN & ES).
# // TODO Create menu list, to display language, and more utilities. 
# // TODO Create module to calculate the total of a retention bill using the amount pay by the client.
# TODO Create a way to change the whole UI when a operation is selected (IGTF or Calculate Subtotal with retention payment made)
# TODO Create module to calculate what price an item should had dependeding in how many items the order has to obtain a total given by the payer.
# TODO Check if it is necessary to add those modules to the IGTF-Calc or make them independet, or have 2 versions. 
# // TODO Show selected options (agent_of_retention, main_question)
# // TODO Show BCV Price with date.

# Windows entity  
window = Tk()

def donothing():
        pass

def create_principal_UI():
    
    config = ConfigParser()
    file = 'src\\config.ini'
    config.read(file)

    # Variables
    #// TODO Look for a way to get the value of the thread or look video on multitasking.
    #// TODO Find a way to change overlay language when is selected on the menu.
    # TODO Find a way to change the UI to use another operation mode selected from the menu.

    now = datetime.datetime.now()
    date_actual = now.strftime('%d-%m-%y')
    user_name = os.getlogin()
    result_height = 14 # Used into the height of the Labels.
    spanish_set = IntVar()
    english_set = IntVar()
    
    IGTF_Calc_set = IntVar()
    IGTF_Calc_set.set(1)
    sub_total_calc_set = IntVar()

    global lang
    
    if config['Language']['lang'] == 'en':
        from src.lang.language import english
        lang = english
        english_set.set(1)
        spanish_set.set(0)



    elif config['Language']['lang'] == 'es':
        from src.lang.language import spanish
        lang = spanish
        spanish_set.set(1)    
        english_set.set(0)


    def update():
        # window.after(1000, update) #Constanly updates the config of the price label and change_rate_button. 
        # lang = config_language()
        # print('hola')
        # print('HOla') Debbuger 
        
        # Scrap code
        # Queue to find the result on the scraping of the BCV price when is done.
        # TODO Find a way to use the same price if the date is different but the price is the same
        # BUG: The the scrap was done on a sunday the prices was 36.37, and the monday the price was the same but the date was differnt. Find a way to avoid the scrap if the price is the same as it was the day before.
        if config['Date']['date_now'] == date_actual:
            # Takes the values from the src\config.ini because is the same date and it doesnt need the scraped value.
            BCV_Price = float(config['BCV_Price']['bcv_price'])
            
            # Update labels with scrap BCV Price.
            price.config(text=f'{lang['Date']}: {date_actual} BCV: {BCV_Price:.5f}', font=('Roboto', 10, 'bold'))
            
            # Adds function to the change rate button.
            change_rate_button.config(command=lambda: convert_bs_dollars(BCV_Price, total_result_label, change_rate_button))  
        
        else:
            # Starts the scrap from the BCV webpage.
            Q = Queue()
            import src.scrap_price_BCV as BCV
            scrap = Process(target=BCV.scraping_BCV, args=(Q,))
            scrap.start()
            BCV_Price = Q.get()
            scrap.kill()
            
            # Update labels with scrap BCV Price.
            price.config(text=f'{lang['Date']}: {date_actual} BCV: {BCV_Price}', font=('Roboto', 10, 'bold'))
            change_rate_button.config(command=lambda: convert_bs_dollars(BCV_Price, total_result_label, change_rate_button))  
    
    # Menu config
    create_menu(spanish_set, english_set, IGTF_Calc_set, sub_total_calc_set)

    # Config of window
    icon = PhotoImage(file='src\\icon.png')
    window.title(lang['Title'])
    window.iconphoto(True, icon)
    window.geometry('800x370') # Default size of the window
    window.minsize(800, 370) # Minimun size of the window
    window.maxsize(800, 370) # Maximun size of the window
    

    # Creating Labels
    question = Label(window, text=lang['Principal Question'], font=('Roboto', 14), justify='left', width=35)
    sub_total_entry = Entry(window, font=('Arial', 18), width=20, bg='yellow', justify='center')
    
    result = Label(window, text='result',font=('Roboto', 14, 'bold'),relief='raised',justify='left',anchor='w',bg='red',width=50  )
   
    agent_of_retention_label = Label(window, text=lang['Agent of Retention'], font=('Roboto', 11))
    agent_of_retention_label_answer = Label(window, text='', font=('Roboto', 12, 'bold') )
   
    igtf_label = Label(window, text='IGTF: ', font=('Roboto', 11) )
    igtf_label_answer = Label(window, text='', font=('Roboto', 12, 'bold'))
    
    principal_result_label = Label(window, text='', font=('Roboto', 10, 'bold'), justify=RIGHT, borderwidth=1,width=60, height=result_height, relief='solid' )
    total_result_label = Label(window, text='', font=('Roboto', 10,  'bold'), justify=RIGHT, borderwidth=1,width=70, height=result_height, relief='solid', bg='yellow')
    
    user = Label(window, text=user_name, font=('Roboto', 24), activebackground='blue')
    version = Label(window, text='Version: alpha-3.0')
    price = Label(window, text=lang['Loading Label'])
    
    # Creating Buttons
    calculate_button = Button(window, text=lang['Calculate Button'], command=lambda: get_sub_total(principal_result_label, total_result_label, agent_of_retention_label_answer, igtf_label_answer, change_rate_button ,sub_total_entry.get()), width=10)
    
    dollar_button = Button(window, text='$', font=('Roboto', 12,'bold'),command=donothing, width=2, height=1)
    
    delete_button = Button(window, text=lang['Delete Button'], command=lambda: delete(change_rate_button, sub_total_entry,principal_result_label, total_result_label, agent_of_retention_label_answer, igtf_label_answer),width=10)
    
    export_button = Button(window, text=lang['Export Button']) # TODO Make a way to expor the calculation into a pdf or txt file.
    
    change_rate_button = Button(window, text='Bs', font=('Roboto', 12),command='' , width=5, state=DISABLED) #// TODO Make changable values between BS/$
    
    # # Option Menu (WIP)
    # options = [  'IGTF', 'Retained Pay']
    # option_selected = StringVar()
    # option_selected.set(options[0])

    # operation_menu = OptionMenu(window, option_selected, *options )
    # operation_menu.grid(row=0, column=0, sticky='nwse')
    
    # Position of principal_UI
    question.grid(row=0 , column=0, sticky='nwse')
    sub_total_entry.grid(row=1, column=0, pady=5,sticky='ns')
    dollar_button.grid(row=1, column=0, padx=70 ,pady=8 ,sticky='ne')

    agent_of_retention_label.grid(row=0, column=1,sticky='w')
    agent_of_retention_label_answer.grid(row=0, column=1, padx=180, sticky='e' )
    igtf_label.grid(row=1, column=1, sticky='w')
    igtf_label_answer.grid(row=1, column=1, padx=45, sticky='w')
    
    calculate_button.grid(row=2, column=0, padx=110,sticky='es')
    delete_button.grid(row=2, column=0, padx=110,sticky='ws')
    
    change_rate_button.grid(row=6, column=1, padx= 2, pady=2, sticky='se')
    version.grid(row=6, column=0, sticky='ws', )
    price.grid(row=6, column=0, sticky='es')
   
    # Config Grid of the window
    sub_total_entry.focus_set() # Focus the entry on the window to instanly put a value.
    window.columnconfigure((0,1), weight= 1, uniform= 'a')
    window.rowconfigure(4, weight= 10, uniform= 'a')
    # window.rowconfigure(0, weight=1, uniform='b')
    # window.rowconfigure(1, weight=1, uniform='b')
    # window.rowconfigure(2, weight=3, uniform='b')
    
     
    # Update price label with the scraped BCV Price.
    window.after(1000, update)
    
def create_second_UI():
    
    config = ConfigParser()
    file = 'src\\config.ini'
    config.read(file)
    

    with open(file, 'w') as configfile:
        config.write(configfile)
    for widget in window.winfo_children():
        widget.destroy()

    window.title('Calculo de Base Imponible con Pago de Agente de Retencion')
    spanish_set = IntVar()
    
    english_set = IntVar()
    
    IGTF_Calc_set = IntVar()
    IGTF_Calc_set.set(0)
    
    sub_total_calc_set = IntVar()
    sub_total_calc_set.set(2)

    global lang
    
    if config['Language']['lang'] == 'en':
        from src.lang.language import english
        lang = english
        english_set.set(1)
        spanish_set.set(0)

    elif config['Language']['lang'] == 'es':
        from src.lang.language import spanish
        lang = spanish
        spanish_set.set(1)    
        english_set.set(0)

    # Menu config
    create_menu(spanish_set, english_set, IGTF_Calc_set, sub_total_calc_set)

    # Label
    unused_label = Label(window, width=40, height=6)
    question = Label(window, text=lang['Payment Done'], font=('Roboto', 14), justify='left', width=35, height=2 , compound=TOP)
    
    result = Label(window, text='result',font=('Roboto', 12 , 'bold'), justify=RIGHT, anchor='center',bg='yellow', width=60, height=6, borderwidth=1  )
    version = Label(window, text='Version: alpha-3.0')
    # debug = result
    # debug.config(text="""
    # Factura Final
    # ***************************************
    # Base Imponible:     $330.225,00
    # ***************************************
    #       IVA (16%):          $52836,00
    #              Total:         $383.061,00\n""")
    
    # # Entry
    payment_entry = Entry(window, font=('Arial', 18), width=20,bg='yellow', justify='center')
                    
    # Buttons
    bolivars_button = Button(window, text='Bs', font=('Roboto', 9,'bold'),command=donothing, width=2, height=1)
    calculate_button = Button(window, text=lang['Calculate Button'], command=lambda: get_payment_done(payment_entry.get(), result), width=10, height=1)
    delete_button = Button(window, text=lang['Delete Button'], command=lambda: delete_second_UI(payment_entry, result),width=10, height=1)


    # debug.grid(row=3, column=1, sticky= 'ns',rowspan=2)
    unused_label.grid(row=0, column=0, sticky='nswe')
    
    question.grid(row=3 , column=0, sticky='n')
    payment_entry.grid(row=4, column=0, pady=5, sticky='n')
    bolivars_button.grid(row=4, column=0, padx=70 ,pady=8 ,sticky='ne')
   
    calculate_button.grid(row=4, column=0, pady=45 , padx=110,sticky='ne')
    delete_button.grid(row=4, column=0, pady=45 ,padx=110,sticky='nw')
    
    version.grid(row=6, column=0, sticky='ws', )
    payment_entry.focus_set()

def create_menu(spanish_set, english_set, IGTF_Calc_set, sub_total_calc_set):  

    menubar = Menu(window)

    file_menu =  Menu(menubar, tearoff=0)
    help_menu = Menu(menubar, tearoff=0)
    operation_menu = Menu(menubar, tearoff=0)
    option_menu = Menu(menubar, tearoff=0)
    lang_option = Menu(menubar, tearoff=0)    
        
        
    menubar.add_cascade(label=lang['File'], menu=file_menu)
    file_menu.add_command(label=lang['New'], command=donothing)
    file_menu.add_command(label=lang['Open'], command=donothing)
    file_menu.add_separator()
    file_menu.add_command(label=lang['Save'], command=donothing)
    file_menu.add_command(label=lang['Save As'], command=donothing)
    file_menu.add_separator()
    file_menu.add_command(label=lang['Close'], command=window.quit)
    
    menubar.add_cascade(label=lang['Operations'], menu=operation_menu)

    operation_menu.add_checkbutton(label=lang['IGTF Calc'], variable=IGTF_Calc_set, onvalue=1, offvalue=0, command= lambda: change_operation(IGTF_Calc_set, sub_total_calc_set))
    
    operation_menu.add_checkbutton(label=lang['Retention Payment'], variable=sub_total_calc_set, onvalue=2, offvalue=0, command=lambda: change_operation(sub_total_calc_set, IGTF_Calc_set))
    operation_menu.add
    menubar.add_cascade(label=lang['Options'], menu=option_menu)
    option_menu.add_cascade(label=lang['Lang'], menu=lang_option)


    # /// TODO Find a way to change the display text when a checkbox is selected.
    lang_option.add_checkbutton(label=lang['Spa'], variable=spanish_set, command=lambda: change_language(spanish_set, english_set))
    lang_option.add_checkbutton(label=lang['Eng'], variable=english_set, command=lambda: change_language(english_set, spanish_set))
    menubar.add_cascade(label=lang['Help'], menu=help_menu)
    help_menu.add_command(label=lang['About'], command=open_about)

    window.config(menu=menubar)    
  
def change_operation(selected , unselected):
        
        if selected.get() == 1:
            delete_UI()
            
            create_principal_UI()
       
        if selected.get() == 2:
            delete_UI()

            create_second_UI()     
        
        selected.set(1)
        unselected.set(0)

def change_language(selected , unselected):
        
        # TODO Find a way to reset the UI with the language selected but keeping the operation currently being used.
        config = ConfigParser()
        file = 'src\\config.ini'
        config.read(file)
        selected.set(1)
        unselected.set(0)
        
        if config['Language']['lang'] == 'en':
            
            print('Espanol')
            config.set('Language', 'lang', 'es') 

            with open(file, 'w') as configfile:
                config.write(configfile)
            for widget in window.winfo_children():
                widget.destroy()

            create_principal_UI() 


        elif config['Language']['lang'] == 'es':
            
            print('Ingles')
            config.set('Language', 'lang', 'en')
            
            with open(file, 'w') as configfile:
                config.write(configfile)
            for widget in window.winfo_children():
                widget.destroy()
                    
            create_principal_UI()

def delete_UI():
    
    config = ConfigParser()
    file = 'src\\config.ini'
    config.read(file)

    with open(file, 'w') as configfile:
        config.write(configfile)
    for widget in window.winfo_children():
        widget.destroy()


final = time.time()
if __name__ == '__main__':
    # Debugger timer to calc init of the mainloop
    print("Ejecucion del GUI: ")
    print(final - inicio)

    #Runs window.
    create_principal_UI()
    window.mainloop()