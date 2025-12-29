import requests
import os
from dotenv import load_dotenv

load_dotenv()

def update_option():
    url = requests.get(os.getenv("RELEASES_API_GITHUB")).url
    response = requests.get(url)
    if response.status_code == 200:
        releases = response.json()
        latest_release = releases[0]
        latest_version = latest_release['tag_name']
        current_version = os.getenv("VERSION")  # Remplacez par la version actuelle de votre application
        if latest_version != current_version:
            print(f"Nouvelle version disponible: {latest_version} Vous utilisez la version: {current_version}")
            print(f"Veuillez mettre à jour l'application depuis le dépôt GitHub. Disponible ici: {latest_release['html_url']}")
        else:
            print("Vous utilisez la dernière version de l'application.")
        
    else:
        print("Erreur lors de la récupération des options depuis GitHub.")
