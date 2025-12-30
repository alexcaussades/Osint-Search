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

just_fix_windows_console()

load_dotenv()
option_type = option.option_generator()
option.check_installation_sherlock()
option.check_installation_maigret()
print("Vérification de l'installation de Sherlock terminée.")

  
if option_type == "email":
    email = input("Entrez l'email à rechercher: ")
    
    
elif option_type == "username":
    username = input(colored("Entrez le username à rechercher: ", "yellow"))
    sherlock.search_username_sherlock(username)
    maigret.check_username_maigret(username)
    
elif option_type == "exit":
    option.fermeture_application()
    
    
option.ouverture_directory_output()
print("Ouverture du répertoire de sortie...")

option.fermeture_application()
 


