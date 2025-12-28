import os



def search_username_sherlock(username: str):
    print(f"Recherche du username '{username}' avec Sherlock...")
    os.system("sherlock --version")  # Vérifier que Sherlock est installé
    os.system("sherlock "+username + " --output output/" + username + ".txt") 
    #os.system(f"sherlock {username} --output sherlock_{username}.json --json")
    # exporter la sortie au format txt dans le fichier username.txt dans le répertoire courant de l'application
    print(f"Recherche terminée. Résultats sauvegardés dans '{username}.txt'.")


if __name__ == "__main__":
    test_username = "exampleuser"
    search_username_sherlock(test_username)