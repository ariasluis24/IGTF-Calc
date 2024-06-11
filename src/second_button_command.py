from tkinter import *
from configparser import ConfigParser
import tkinter.messagebox
import src.calculations as calculations

# TODO Implement this module to main program.
# TODO Make it available when selected.


def get_payment_done(payment_done_str, result):
    
    config = ConfigParser()
    file = 'src\\config.ini'
    config.read(file)
    
    if config['Language']['lang'] == 'es':
        from src.lang.language import spanish
        lang = spanish

    elif config['Language']['lang'] == 'en':
        from src.lang.language import english
        lang = english    

    try:
        BI, IVA, total = calculations.retained_pay_Calculation(payment_done_str)

        result.config(text=calculations.GUI_print_Sub_total_Bill(BI, IVA, total)) 
        result.grid(row=0, column=1, sticky= 'ns',rowspan=5 )
    
    except ValueError:
        tkinter.messagebox.showerror(title='Error', message=lang['Error'], detail=lang['Error Detail'] )
