# coding: utf-8
from subprocess import run
import requests
import smtplib as smtp
import time
import socket
import urllib3
from termcolor import colored
import dns.resolver
import smtplib
import dns.resolver


#Nous pensons que alexcaussades@hotmail.com n'est pas valide
# La syntaxe d'adresse email est correcte
# MX enregistrement trouvé: hotmail-com.olc.protection.outlook.com (Priorité 2)
# La connexion à hotmail-com.olc.protection.outlook.com a fonctionné
# Réponse du serveur: 550 5.5.0 Requested action not taken: mailbox unavailable (S2017062302). [SA2PEPF00003F67.namprd04.prod.outlook.com 2025-12-27T18:20:54.905Z 08DE41AB68FE2DF5]


def is_valid_email(email):
    # Séparer le nom d'utilisateur et le nom de domaine
    username, domain = email.split('@')
    print(colored(f"[*] Verifying the email address {username}...", "blue"))
    adresses_ip = run("netstat -nt | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n")
    try:
        # Vérifier le nom de domaine
        mx_records = dns.resolver.query(domain, 'MX')
        mx_record = mx_records[0].exchange.to_text()
        print(colored(f"[+] MX record found: {mx_record}", "green"))
        # Établir une connexion SMTP
        smtp = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
        smtp.connect(mx_record)
        smtp.helo()  # Envoyer la commande HELO
        smtp.starttls()  # Démarrer la connexion TLS
        smtp.helo()  # Envoyer à nouveau la commande HELO
        smtp.mail('test@test.com')  # Adresse e-mail de l'expéditeur
        print(smtp)
        code, message = smtp.rcpt(email)
        smtp.quit()
        if code == 250:
            print(colored(f"[+] The email address {email} is valid.", "green"))
        else:
            print(colored(f"[!] The email address {email} is not valid.", "red"))
    except Exception as e:
        print(colored(f"[!] An error occurred while verifying the email address: {e}", "red"))
