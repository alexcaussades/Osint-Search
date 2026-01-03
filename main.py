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
from modules.option.config import activate_default_preference_config, désactiver_preference_config
from modules.username import sherlock
from modules.username import maigret
from dotenv import load_dotenv
from colorama import just_fix_windows_console
from termcolor import colored
import configparser

#activate_default_preference_config()
config = configparser.ConfigParser()
config.read('config.ini')

configpref = config['Search']['Search_preference_active']

just_fix_windows_console()

load_dotenv()
option.check_installation_sherlock()
option.check_installation_maigret()



if (len(sys.argv) > 1 and sys.argv[1] == "--all"):
    print("Recherche avec toutes les options activées.")
    option.option_generator()
    option.ouverture_directory_output()
    print("Ouverture du répertoire de sortie...")
    option.fermeture_application()
    sys.exit()
    
if (len(sys.argv) > 1 and sys.argv[1] == "--help"):
    print("Utilisation: python main.py [--all] [--help]")
    print("--all : Recherche avec toutes les options activées.")
    print("username <username> (u) : Recherche du username spécifié.")
    print("email <email> (e): Recherche de l'email spécifié.")
    print("--help : Affiche ce message d'aide.")
    sys.exit()
    
    
    
if (len(sys.argv) > 1 and sys.argv[1] == "username"):
    username = sys.argv[2] if len(sys.argv) > 2 else input("Entrez le username à rechercher: ")
    print(f"Recherche du username: {username}")
    sherlock.search_username_sherlock(username)
    maigret.search_username_maigret(username)
    option.ouverture_directory_output()
    sys.exit()
    
if (len(sys.argv) > 1 and sys.argv[1] == "u"):
    username = sys.argv[2] if len(sys.argv) > 2 else input("Entrez le username à rechercher: ")
    print(f"Recherche du username: {username}")
    sherlock.search_username_sherlock(username)
    maigret.search_username_maigret(username)
    option.ouverture_directory_output()
    sys.exit()
    
if (len(sys.argv) > 1 and sys.argv[1] == "email"):
    email = sys.argv[2] if len(sys.argv) > 2 else input("Entrez l'email à rechercher: ")
    print(f"Recherche de l'email: {email}")
    print("Fonction de recherche d'email non encore implémentée.")
    sys.exit()
    
if (len(sys.argv) > 1 and sys.argv[1] == "e"):
    email = sys.argv[2] if len(sys.argv) > 2 else input("Entrez l'email à rechercher: ")
    print(f"Recherche de l'email: {email}")
    print("Fonction de recherche d'email non encore implémentée.")
    sys.exit()
    
if (len(sys.argv) > 1 and sys.argv[1] == "--pref" and sys.argv[2] == "on"):
    activate_default_preference_config()
    print("Préférences activées.")
    print("Veuillez relancer l'application pour que les modifications prennent effet.")
    sys.exit()
    
if (len(sys.argv) > 1 and sys.argv[1] == "--pref" and sys.argv[2] == "off"):
    désactiver_preference_config()
    print("Veuillez relancer l'application pour que les modifications prennent effet.")
    sys.exit()


if(configpref == "True"):
    print (colored("Recherche avec préférences activées.", "green"))
    print("Pour désactiver les préférences, modifiez 'Search_preference_active' à 'False' dans config.ini")
    option.option_generator_minimal()
else:
    print (colored("Recherche avec préférences désactivées.", "red"))
    option.option_generator()
    
    
option.ouverture_directory_output()
print("Ouverture du répertoire de sortie...")

option.fermeture_application()
 


