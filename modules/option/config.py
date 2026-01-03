# Genere le config.ini s'il n'existe pas
import os
import configparser

config = configparser.ConfigParser()

dictionary_default_config = {
    'Search': {
        'Search_preference_active': 'True',
        'Search_preference': 'username',
        'backup_enabled': 'True'
    }
}

dictionary_disabled_config = {
    'Search': {
        'Search_preference_active': 'False',
        'Search_preference': '',
        'backup_enabled': 'True'
    }
}

def activate_default_preference_config():
    
    if not os.path.exists('config.ini'):
        # ecrire le fichier config.ini avec les paramètres par défaut comme dans dictionary_default_config
        config['Search'] = dictionary_default_config['Search']
        with open('config.ini', 'w') as configfile:
            config.write(configfile)    
        print("Fichier config.ini créé avec les paramètres par défaut.")
        print("Vous pouvez modifier les paramètres dans config.ini selon vos préférences.")
        
    elif os.path.exists('config.ini'):
        os.remove('config.ini')
        config['Search'] = dictionary_default_config['Search']
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    else:
        config.read('config.ini')
        print("Fichier config.ini trouvé et chargé.")
        

def désactiver_preference_config():
    if os.path.exists('config.ini'):
        config['Search'] = dictionary_disabled_config['Search']
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        print("Préférences désactivées dans config.ini.")
        
    elif os.path.exists('config.ini'):
        os.remove('config.ini')
        config['Search'] = dictionary_disabled_config['Search']
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    else:
        print("Le fichier config.ini n'existe pas. Aucune modification apportée.")





