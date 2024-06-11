from tkinter import *
import src.calculations as calculations

# TODO Implement this module to main program.
# TODO Make it available when selected.


def get_payment_done(payment_done_str, result):

    BI, IVA, total = calculations.retained_pay_Calculation(payment_done_str)

    result.config(text=calculations.GUI_print_Sub_total_Bill(BI, IVA, total)) 
    result.grid(row=0, column=1, sticky= 'ns',rowspan=5 )

