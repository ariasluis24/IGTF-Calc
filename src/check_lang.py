from configparser import ConfigParser

# TODO See if there is a way to implement this function into the necesary parts of the program.
def config_language():
    config = ConfigParser()
    file = 'src\\config.ini'
    config.read(file)
    options = ['es', 'en']
    lang = None
    
    if config['Language']['lang'] == 'es':
        from lang.language import spanish
        lang = spanish
        

    elif config['Language']['lang'] == 'en':
        from lang.language import english
        lang = english
    
    return lang
