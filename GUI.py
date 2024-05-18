from tkinter import *
from multiprocessing import Process, Queue
from configparser import ConfigParser
from src.principal_button_command import get_sub_total, convert_bs_dollars
from src.delete_module import delete
from src.about import open_about
import os, time, datetime



inicio = time.time()
# TODO work on how to handle exceptions
# ///TODO Reasign functions on GUI.py to indivual modules.
# TODO Rename GUI.py to main.py (If necessary).
# TODO Create dictionaries to use them for localization (EN & ES).
# ///TODO Create menu list, to display language, and more utilities. 
# ///TODO Create module to calculate the total of a retention bill using the amount pay by the client.
# TODO Create module to calculate what price an item should had dependeding in how many items the order has to obtain a total given by the payer.
# TODO Check if it is necessary to add those modules to the IGTF-Calc or make them independet, or have 2 versions. 
#// TODO Show selected options (agent_of_retention, main_question)
#// TODO Show BCV Price with date.
# Variables
#// TODO Look for a way to get the value of the thread or look video on multitasking.
config = ConfigParser()
file = 'src\\config.ini'
config.read(file)

now = datetime.datetime.now()
date_actual = now.strftime('%d-%m-%y')
user_name = os.getlogin()
result_height = 14 # Used into the height of the Labels.

def update():
    # window.after(1000, update) #Constanly updates the config of the price label and change_rate_button. 
    # print('HOla') Debbuger 
    
    # Scrap code
    # Queue to find the result on the scraping of the BCV price when is done.
    if config['Date']['date_now'] == date_actual:
        # Takes the values from the src\config.ini because is the same date and it doesnt need the scraped value.
        BCV_Price = float(config['BCV_Price']['bcv_price'])
        
        # Update labels with scrap BCV Price.
        price.config(text=f'Date: {date_actual} BCV: {BCV_Price:.5f}', font=('Roboto', 10, 'bold'))
        
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
        price.config(text=f'Date: {date_actual} BCV: {BCV_Price}', font=('Roboto', 10, 'bold'))
        change_rate_button.config(command=lambda: convert_bs_dollars(BCV_Price, total_result_label, change_rate_button))  


# Windows entity  
window = Tk()

# Menu config
def donothing():
    pass

menubar = Menu(window)

file_menu =  Menu(menubar, tearoff=0)
help_menu = Menu(menubar, tearoff=0)
operation_menu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="New", command=donothing)
file_menu.add_command(label="Open", command=donothing)
file_menu.add_separator()
file_menu.add_command(label="Save", command=donothing)
file_menu.add_command(label="Save as...", command=donothing)
file_menu.add_separator()
file_menu.add_command(label="Close", command=donothing)

menubar.add_cascade(label='Operations', menu=operation_menu)
operation_menu.add_checkbutton(label='IGTF Calculation', command=donothing)
operation_menu.add_checkbutton(label='Payment of Agent of retention Calculation', command=donothing)

menubar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About', command=open_about)

# Config of window
icon = PhotoImage(file='src\\icon.png')
window.title('IGTF Calculator')
window.iconphoto(True, icon)
window.geometry('800x370') # Default size of the window
window.minsize(800, 370) # Minimun size of the window
window.maxsize(800, 370) # Maximun size of the window
window.config(menu=menubar)

# Creating Labels
question = Label(window, 
                text='Please how much is the sub total on $?:',
                font=('Roboto', 14),
                justify='left',
                width=35)
sub_total_entry = Entry(window, 
                  font=('Arial', 18),
                  width=20,
                  bg='yellow',
                  justify='center')
result = Label(window, 
                text='result',
                font=('Roboto', 14),
                relief='raised',
                justify='left',
                anchor='w',
                bg='red',
                width=50  )
agent_of_retention_label = Label(window, text='AGENT OF RETENTION: ', font=('Roboto', 11))
agent_of_retention_label_answer = Label(window, text='', font=('Roboto', 12, 'bold') )
igtf_label = Label(window, text='IGTF: ', font=('Roboto', 11) )
igtf_label_answer = Label(window, text='', font=('Roboto', 12, 'bold'))
principal_result_label = Label(window, text='', font=('Roboto', 10), justify=RIGHT, borderwidth=1,width=60, height=result_height, relief='solid' )
total_result_label = Label(window, text='', font=('Roboto', 10), justify=RIGHT, borderwidth=1,width=70, height=result_height, relief='solid', bg='yellow')
user = Label(window, 
             text=user_name, 
             font=('Roboto', 24), 
             activebackground='blue')
version = Label(window, text='Version: alpha-2.0')
price = Label(window, text='Loading...')

# Creating Buttons
calculate_button = Button(window, text='Calculate', command=lambda: get_sub_total(principal_result_label, total_result_label, agent_of_retention_label_answer, igtf_label_answer, change_rate_button ,sub_total_entry.get()), width=10)
delete_button = Button(window, text='Delete', command=lambda: delete(change_rate_button, sub_total_entry,principal_result_label, total_result_label),width=10)
export_button = Button(window, text='Export') # TODO Make a way to expor the calculation into a pdf or txt file.
change_rate_button = Button(window, text='Bs', font=('Roboto', 12),command='' , width=5, state=DISABLED) #// TODO Make changable values between BS/$

# Position of Widgets
question.grid(row=0 , column=0, sticky='nwse')
sub_total_entry.grid(row=1, column=0, pady=5,sticky='ns')

agent_of_retention_label.grid(row=0, column=1,sticky='w')
agent_of_retention_label_answer.grid(row=0, column=1, padx=173, sticky='w' )
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

final = time.time()
if __name__ == '__main__':
    # Debugger timer to calc init of the mainloop
    print("Ejecucion del GUI: ")
    print(final - inicio)

    # Update price label with the scraped BCV Price.
    window.after(1000, update)

    #Runs window.
    window.mainloop()