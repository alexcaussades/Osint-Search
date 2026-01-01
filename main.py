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

#print(config['Search']['Search_preference'])

just_fix_windows_console()

load_dotenv()

option_type = option.option_generator()
option.check_installation_sherlock()
option.check_installation_maigret()
print("Vérification de l'installation de Sherlock terminée.")

if(config["Search"]["Search_preference_active"] == "true"):
    option.option_generator_minimal()

    
if option_type == "exit":
    option.fermeture_application()
    
    
option.ouverture_directory_output()
print("Ouverture du répertoire de sortie...")

option.fermeture_application()
 


