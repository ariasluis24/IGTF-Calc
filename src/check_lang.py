from configparser import ConfigParser

config = ConfigParser()
file = 'src\\config.ini'
config.read(file)
options = ['es', 'en']

def config_language():
    lang = None
    if config['Language']['lang'] == 'es':
        from src.lang.language import spanish
        lang = spanish
        return lang

    elif config['Language']['lang'] == 'en':
        from src.lang.language import english
        lang = english
        return lang



# def change_language(selected , unselected, window):

#     selected.set(1)
#     unselected.set(0)
    

#     if config['Language']['lang'] == 'en':
#         print('Espanol')
#         config.set('Language', 'lang', 'es') 

#         with open(file, 'w') as configfile:
#             config.write(configfile)
#         for widget in window.winfo_children():
#             widget.destroy()
#         create_widgets() 




#     elif config['Language']['lang'] == 'es':
#         print('Ingles')
#         config.set('Language', 'lang', 'en')
        
#         with open(file, 'w') as configfile:
#             config.write(configfile)
#         for widget in window.winfo_children():
#             widget.destroy()
#         create_widgets() 


# def restart_program():
#   """Restarts the current Python program."""
#   python = sys.executable
#   os.execl(python, python, *sys.argv)