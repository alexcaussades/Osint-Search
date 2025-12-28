import requests
from termcolor import colored

def proton_mail(email: str) -> str:
    r = requests.request("GET", "https://api.protonmail.ch/pks/lookup?op=index&search=" + email + "@protonmail.com")    
    #print(r.text)
    if "info:1:0" in r.text:
        print(colored(f"[!] No public E-mail found for protonmail.com", "red"))
    else:
        print(colored(f"[+] Public E-mail found for {email}@protonmail.com:", "green"))
    if r.json is True:
        print(colored(f"[!] Rate limit exceeded for protonmail.com API. Please try again later.", "grey"))
        
def proton_ch(email: str) -> str:
    r = requests.request("GET", "https://api.protonmail.ch/pks/lookup?op=index&search=" + email + "@protonmail.ch")    
    #print(r.text)
    if "info:1:0" in r.text:
        print(colored(f"[!] No public E-mail found for protonmail.ch", "red"))
    else:
        print(colored(f"[+] Public E-mail found for {email}@protonmail.ch:", "green"))
    if r.json is True:
        print(colored(f"[!] Rate limit exceeded for protonmail.ch API. Please try again later.", "grey"))
        
def proton_me(email: str) -> str:
    r = requests.request("GET", "https://api.protonmail.ch/pks/lookup?op=index&search=" + email + "@proton.me")    
    #print(r.text)
    if "info:1:0" in r.text:
        print(colored(f"[!] No public E-mail found for proton.me", "red"))
    else:
        print(colored(f"[+] Public E-mail found for {email}@proton.me:", "green"))
    if r.json is True:
        print(colored(f"[!] Rate limit exceeded for proton.me API. Please try again later.", "grey"))
        
def proton_pm(email: str) -> str:
    r = requests.request("GET", "https://api.protonmail.ch/pks/lookup?op=index&search=" + email + "@pm.me")    
    #print(r.text)
    if "info:1:0" in r.text:
        print(colored(f"[!] No public E-mail found for pm.me", "red"))
    else:
        print(colored(f"[+] Public E-mail found for {email}@pm.me:", "green"))
    if r.json is True:
        print(colored(f"[!] Rate limit exceeded for pm.me API. Please try again later.", "grey"))
        
def proton(email: str) -> None:
    print(colored(f"[*] Searching Proton for {email}...", "blue"))
    proton_mail(email)
    proton_ch(email)
    proton_me(email)
    proton_pm(email)
    print(colored(f"[*] Finished searching Proton for {email}.", "blue"))
    
# Example usage:
# proton("exampleuser")

