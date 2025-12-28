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
from dotenv import load_dotenv
import colored

load_dotenv()
option_type = option.option_generator()
option.check_installation_sherlock()
print("Vérification de l'installation de Sherlock terminée.") 

  
if option_type == "email":
    email = input("Entrez l'email à rechercher: ")
    
    
elif option_type == "username":
    username = input("Entrez le username à rechercher: ")
    sherlock.search_username_sherlock(username)
    
 


