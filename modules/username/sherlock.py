import os



def search_username_sherlock(username: str):
    print(f"Recherche du username '{username}' avec Sherlock...")
    os.system("sherlock --version")  # Vérifier que Sherlock est installé
    os.system("sherlock "+username + " --output output/" + username + ".txt") 
    print(f"Recherche terminée. Résultats sauvegardés dans '{username}.txt'.")


if __name__ == "__main__":
    test_username = "exampleuser"
    search_username_sherlock(test_username)