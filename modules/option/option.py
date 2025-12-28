import os
import subprocess



def check_directory_output(path):
    if(os.path.join(path, "output")):
        return True
    else:
        os.mkdir(os.path.join(path, "output"))
        return False

def option_generator() -> str:
    print("Bienvenue dans l'outil de recherche OSINT. Version " + os.getenv("Version"))
    print("")
    print("un outil pour rechercher des emails et des usernames sur diverses plateformes en ligne.")
    print("")
    print("Contribé au developpement de cet outil sur GitHub: https://github.com/votre-repository")
    print("")
    print("Adresse du portefeuille pour les dons: " + os.getenv("WALLET_ADRESSE"))
    print("")
    option_type = input("Voulez-vous rechercher un email ou un username? (email/username): ")
    while option_type not in ["email", "username"]:
        print("Option invalide. Veuillez entrer 'email' ou 'username'.")
        option_type = input("Voulez-vous rechercher un email ou un username? (email/username): ")
    return option_type


def check_installation_sherlock():
    try:
        #  Vérifier si Sherlock est installé sur le système en utilisant 'which' sous Unix ou 'where' sous Windows
            with open(os.devnull, 'w') as devnull:
                if os.name == 'nt':
                    subprocess.check_call(['where', 'sherlock'], stdout=devnull, stderr=devnull)
                else:
                    subprocess.check_call(['which', 'sherlock'], stdout=devnull, stderr=devnull)
                    
            pass
    except FileNotFoundError:
        print("[*] Sherlock n'est pas installé. Installation en cours...")
        os.system("git clone https://github.com/sherlock-project/sherlock.git")
        install_dependencies_sherlock()
        print("[*] Installation de Sherlock terminée.")
    except subprocess.CalledProcessError:
        print("[*] Sherlock n'est pas installé. Installation en cours...")
        os.system("git clone https://github.com/sherlock-project/sherlock.git")
        install_dependencies_sherlock()
        print("[*] Installation de Sherlock terminée.")
        
def install_dependencies_sherlock():
    print("[*] Installation des dépendances de Sherlock...")
    os.system("pip install -r sherlock/requirements.txt")
    print("[*] Installation des dépendances terminée.")
