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

option.check_installation_sherlock()
option.check_installation_maigret()
print("Vérification de l'installation de Sherlock terminée.")

if(configpref == "true"):
    print ("Recherche avec préférences activées.")
    option.option_generator_minimal()
    
    
option.ouverture_directory_output()
print("Ouverture du répertoire de sortie...")

option.fermeture_application()
 


