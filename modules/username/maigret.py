import os




def check_username_maigret(username) -> str:
    print(f"Recherche du username '{username}' avec Maigret...")
    os.system("maigret " + username + " --pdf")
    print("Choisir Option F")
    os.system("xcopy /Y reports\\report_"+ username + ".pdf output\\" + username + "_maigret.pdf")
    print("Suppression des fichiers temporaires de Maigret...")
    os.system("rmdir /S /Q reports")
    print(f"Recherche terminée. Résultats sauvegardés dans 'output/{username}_maigret.pdf'.")
    
    
if __name__ == "__main__":
    test_username = "exampleuser"
    check_username_maigret(test_username)