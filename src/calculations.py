# Import to set the locale system for the decimal(,) and thousand(.) separators.
import locale, datetime
from decimal import Decimal
from src.scrap_price_BCV import price_BCV
locale.setlocale(locale.LC_ALL, 'en_DE')
BCV_Rate = price_BCV

def principal_Calculation(sub_total):
    IVA = sub_total * 0.16
    total = sub_total + IVA
    return IVA, total

def GUI_principal_Calculation(sub_total, IVA, total):
    return f'''
    ***************NORMAL BILL********************
    Sub-Total:     {round(Decimal(sub_total),2):n}
     IVA (16%):      {round(Decimal(IVA),2):n}
        Total:    {round(Decimal(total),2):n}

    ***************RETAINED BILL******************
    Sub-Total:    {round(Decimal(sub_total),2):n}
    IVA (16%):      {round(Decimal(IVA),2):n}
    Retained IVA (25%):       {round(Decimal(IVA*0.25),2):n}
    Total:    {round(Decimal(sub_total) + Decimal(IVA*0.25),2):n}
    '''
    
def txt_Bill(sub_total, IVA, total):
    return f'''                 Date:{date} Client: -
                ***************NORMAL BILL***************************RETAINED BILL******************
            Sub-Total:    {round(Decimal(sub_total),2):n}          *              Sub-Total:    {round(Decimal(sub_total),2):n}
             IVA(16%):     {round(Decimal(IVA),2):n}          *               IVA(16%):     {round(Decimal(IVA),2):n}
                Total:    {round(Decimal(total),2):n}          *           Retained IVA:     {round(Decimal(IVA*0.25),2):n}
                                          *                  Total:    {round(Decimal(sub_total) + Decimal(IVA*0.25),2):n}\n
    '''

def calc_IGTF(pay_Cash):
    IGTF = pay_Cash * 0.03
    return IGTF

def calc_Retention(sub_total:float, iva:float ):
    iva_25 = iva * 0.25
    total_reten = sub_total + iva_25
    return iva_25, total_reten

def rest_to_Pay(pay_Cash, IGTF,total):
    print('******************************')
    print(f'The rest to pay is: {round((Decimal(total) + Decimal(IGTF)) - Decimal(pay_Cash),2):n}')
    print('******************************\n')
    pass

def main_Function():
    # rest_to_Pay(pay_Cash, IGTF,reten_Total)    
    pass


# TODO Use just one format for the bill, switching the iva percentage and value, depending if the user wants to calculate the retention of the iva.

def GUI_print_Bill(sub_total, IVA, pay_Cash,IGTF, total):
    return f"""
    ***************FINAL BILL********************
    Sub-Total:         ${round(Decimal(sub_total),2):n}
     IVA(16%):             ${round(Decimal(IVA),2):n}
      Payment:              ${round(Decimal(pay_Cash),2):n}
     IGTF(3%):              ${round(Decimal(IGTF),2):n}
        Total:          ${round(Decimal(total) + Decimal(IGTF),2):n}"""

def GUI_print_Reten_Bill(sub_total, reten_IVA, pay_Cash,IGTF,reten_Total):
    return f"""
    ***************FINAL RETENTION BILL********************
    Sub-Total:      ${round(Decimal(sub_total),2):n}
    IVA (25%):         ${round(Decimal(reten_IVA),2):n}
    $ Payment:         ${round(Decimal(pay_Cash),2):n}
     IGTF(3%):         ${round(Decimal(IGTF),2):n}
        Total:    ${round(Decimal(reten_Total) + Decimal(IGTF),2):n}\n"""

def convert_to_Bolivars(data, BCV_Rate):
    my_values = []
    for x in data:
        my_values.append(round(x * BCV_Rate, 2))
    return my_values  
    
# to_bolivars_lambda = lambda data, BCV_Rate: [x * BCV_Rate for x in data]