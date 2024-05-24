# Import to set the locale system for the decimal(,) and thousand(.) separators.
import locale
from decimal import Decimal
from configparser import ConfigParser
locale.setlocale(locale.LC_ALL, 'en_DE')

def principal_Calculation(sub_total):
    IVA = sub_total * 0.16
    total = sub_total + IVA
    return IVA, total

def GUI_principal_Calculation(sub_total, IVA, total):
    config = ConfigParser()
    file = 'src\\config.ini'
    config.read(file)
        
    if config['Language']['lang'] == 'es':
        from src.lang.language import spanish
        lang = spanish

    elif config['Language']['lang'] == 'en':
        from src.lang.language import english
        lang = english

    return f'''
    ***************{lang['Normal Bill']}********************
    {lang['Sub Total']}:    {round(Decimal(sub_total),2):n}
    {lang['IVA 1']}:      {round(Decimal(IVA),2):n}
        {lang['Total']}:    {round(Decimal(total),2):n}

    ***************{lang['Retained Bill']}******************
    {lang['Sub Total']}:    {round(Decimal(sub_total),2):n}
    {lang['IVA 1']}:      {round(Decimal(IVA),2):n}
    {lang['IVA Retained']}:      {round(Decimal(IVA*0.75),2):n}
    {lang['Total to Pay']}:       {round(Decimal(sub_total) + Decimal(IVA*0.25),2):n}
    '''
    
def txt_Bill(sub_total, IVA, total):
    from main import date # Test import for further work WIP.
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

def GUI_print_Bill(sub_total, IVA, pay_Cash,IGTF, total):
    config = ConfigParser()
    file = 'src\\config.ini'
    config.read(file)
        
    if config['Language']['lang'] == 'es':
        from src.lang.language import spanish
        lang = spanish

    elif config['Language']['lang'] == 'en':
        from src.lang.language import english
        lang = english
    
    return f"""
    ***************{lang['Final Normal Bill']}********************
    {lang['Sub Total']}:         ${round(Decimal(sub_total),2):n}
     {lang['IVA 1']}:             ${round(Decimal(IVA),2):n}
     {lang['Payment $']}:              ${round(Decimal(pay_Cash),2):n}
     {lang['IGTF']}:              ${round(Decimal(IGTF),2):n}
        {lang['Total']}:          ${round(Decimal(total) + Decimal(IGTF),2):n}"""

def GUI_print_Reten_Bill(sub_total, reten_IVA, pay_Cash,IGTF,reten_Total):
    config = ConfigParser()
    file = 'src\\config.ini'
    config.read(file)
        
    if config['Language']['lang'] == 'es':
        from src.lang.language import spanish
        lang = spanish

    elif config['Language']['lang'] == 'en':
        from src.lang.language import english
        lang = english
    
    return f"""
    ***************{lang['Final Retained Bill']}********************
    {lang['Sub Total']}:     ${round(Decimal(sub_total),2):n}
    {lang['IVA 2']}:          ${round(Decimal(reten_IVA),2):n}
    {lang['Payment $']}:          ${round(Decimal(pay_Cash),2):n}
     {lang['IGTF']}:          ${round(Decimal(IGTF),2):n}
        {lang['Total']}:     ${round(Decimal(reten_Total) + Decimal(IGTF),2):n}\n"""

def convert_to_Bolivars(data, BCV_Rate):
    my_values = []
    for x in data:
        my_values.append(round(x * BCV_Rate, 2))
    return my_values  
    
# to_bolivars_lambda = lambda data, BCV_Rate: [x * BCV_Rate for x in data]