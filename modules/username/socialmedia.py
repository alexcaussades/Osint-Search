from unittest.util import safe_repr
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import urllib3
urllib3.disable_warnings()
from playwright.sync_api import sync_playwright
http = urllib3.PoolManager()
from instaloader import Instaloader, Profile


username = "alexcaussades"  # Remplacez par le nom d'utilisateur que vous souhaitez rechercher

SITES = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Steam": "https://steamcommunity.com/id/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Twitter": "https://twitter.com/{}",
    "nitter": "https://nitter.net/{}",
}


# autor: alexcaussades dev: 0.5 for playwright 
def safe_text(page, selector): 
    try: 
        return page.locator(selector).inner_text() 
    except: 
        return None
    
def Search_Nitter(username):            
        url = f"{SITES['nitter'].format(username)}"
        response = requests.get(url, timeout=50000)
        if response.status_code == 404:
            print(f"❌ Utilisateur '{username}' introuvable sur Nitter")
            return
        if response.status_code != 200:
            print("❌ Impossible de récupérer les informations utilisateur Nitter.")
            return
        if response.status_code == 502:
            print("❌ Nitter est actuellement indisponible (502 Bad Gateway).")
            return
        soup = BeautifulSoup(response.text, 'html.parser')
        
        bio = soup.find("div", {"class": "profile-bio"}).text if soup.find("div", {"class": "profile-bio"}) else 'Bio non disponible'
        
        followers = soup.find("li", {"class": "followers"}).find("span", {"class": "profile-stat-num"}).text if soup.find("li", {"class": "followers"}) else 'Nombre de followers non disponible'
        
        following = soup.find("li", {"class": "following"}).find("span", {"class": "profile-stat-num"}).text if soup.find("li", {"class": "following"}) else 'Nombre de following non disponible'
        
        tweets = soup.find("li", {"class": "posts"}).find("span", {"class": "profile-stat-num"}).text if soup.find("li", {"class": "posts"}) else 'Nombre de tweets non disponible'
        
        likes = soup.find("li", {"class": "likes"}).find("span", {"class": "profile-stat-num"}).text if soup.find("li", {"class": "likes"}) else 'Nombre de likes non disponible'
        
        info = {
            "username": username,
            "bio": bio,
            "followers": followers,
            "following": following,
            "tweets": tweets,
            "likes": likes,
            "url": url
        }
        print("Nitter User Info:")
        print(info)



def get_reddit_user_info(username):
    url = f"https://www.reddit.com/user/{username}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    r = requests.get(url, headers=headers, verify=False)
    
    if r.status_code == 404:
        print(f"❌ Utilisateur '{username}' introuvable sur Reddit")
        pass
    
    if r.status_code != 200:
        print("❌ Impossible de récupérer les informations utilisateur Reddit.")
        pass
    try:
        r.raise_for_status()  
    except requests.exceptions.HTTPError as e:
        return

    data = r.json()["data"]

    print("Reddit User Info:")
    
    info=  {
        "username": data["subreddit"]["display_name"],
        "description": data["subreddit"]["description"],
        "Banned": data["subreddit"]["user_is_banned"],
        "total_karma": data["total_karma"],
        "post_karma": data["link_karma"],
        "comment_karma": data["comment_karma"],
        "url": f"https://www.reddit.com/user/{username}/"
    }  
    print(info)

# utiliser la methode Search_Nitter pour Instagram
def instagram_user_info(username):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # False = voir le navigateur
        page = browser.new_page()
        page.goto(SITES["Instagram"].format(username))
        if page.title() == "Profile isn't available • Instagram": 
            print(f"❌ Utilisateur '{username}' introuvable sur Instagram")
            browser.close() 
            return print("")
        else:
            print("Instagram User Info:")
            Info = { 
                "title": page.title(),
                "url_page": page.url
                }
        browser.close()
        print(Info)


Search_Nitter(username)
# get_reddit_user_info(username)
# instagram_user_info(username)
