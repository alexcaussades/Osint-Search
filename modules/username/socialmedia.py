from unittest.util import safe_repr
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import urllib3
urllib3.disable_warnings()
from playwright.sync_api import sync_playwright
http = urllib3.PoolManager()


username = "alexcaussades24"  # Remplacez par le nom d'utilisateur que vous souhaitez rechercher

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
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # False = voir le navigateur
        page = browser.new_page()
        page.goto(SITES["nitter"].format(username))
        print("Nitter User Info:")
        if page.text_content("body").find("error-panel") == "User "+ username + " not found.":
            print(f"❌ Utilisateur '{username}' introuvable sur cette instance Nitter")
            browser.close()
        Info = { 
            "title": page.title(), "url": page.url, 
            "bio": safe_text(page, "div.profile-bio"),
            "followers": safe_text(page, 'li.followers .profile-stat-num'),
            "following": safe_text(page, 'li.following .profile-stat-num'),
            "tweets": safe_text(page, 'li.posts .profile-stat-num'),
            "likes": safe_text(page, 'li.likes .profile-stat-num'),
            "url_page": page.url
            }
        browser.close()
        print(Info)



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
get_reddit_user_info(username)
instagram_user_info(username)
