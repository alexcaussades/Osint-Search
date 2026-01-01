from base64 import b64encode, b64decode
import string
import random
from subprocess import Popen, PIPE
import os
import sys
import time
import hashlib
import json
import smtplib
import socket
from modules.option import option
from modules.username import sherlock
from modules.username import maigret
from dotenv import load_dotenv
from colorama import just_fix_windows_console
from termcolor import colored
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

configpref = config['Search']['Search_preference_active']

just_fix_windows_console()

load_dotenv()

if (len(sys.argv) > 1 and sys.argv[1] == "--all"):
    print("Recherche avec toutes les options activées.")
    option.option_generator()
    option.ouverture_directory_output()
    print("Ouverture du répertoire de sortie...")
    option.fermeture_application()
    sys.exit()
elif (len(sys.argv) > 1 and sys.argv[1] == "--help"):
    print("Utilisation: python main.py [--all] [--help]")
    print("--all : Recherche avec toutes les options activées.")
    print("username <username> : Recherche du username spécifié.")
    print("email <email> : Recherche de l'email spécifié.")
    print("--help : Affiche ce message d'aide.")
    sys.exit()
elif (len(sys.argv) > 1 and sys.argv[1] == "username" or 'u' and sys.argv[2]):
    username = sys.argv[2]
    print(f"Recherche du username: {username}")
    sherlock.search_username_sherlock(username)
    maigret.search_username_maigret(username)
    option.ouverture_directory_output()
    sys.exit()
elif (len(sys.argv) > 1 and sys.argv[1] == "email" or 'e' and sys.argv[2]):
    email = sys.argv[2]
    print(f"Recherche de l'email: {email}")
    print("Fonction de recherche d'email non encore implémentée.")
    sys.exit()

option.check_installation_sherlock()
option.check_installation_maigret()
print("Vérification de l'installation de Sherlock terminée.")

if(configpref == "true"):
    print ("Recherche avec préférences activées.")
    option.option_generator_minimal()
    
    
option.ouverture_directory_output()
print("Ouverture du répertoire de sortie...")

option.fermeture_application()
 


