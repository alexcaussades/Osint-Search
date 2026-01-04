from unittest.util import safe_repr
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import urllib3
urllib3.disable_warnings()
from playwright.sync_api import sync_playwright
http = urllib3.PoolManager()


username = "alexcaussades"

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
        if page.locator(".error-panel").is_visible(): 
            print(f"❌ Utilisateur '{username}' introuvable sur cette instance Nitter")
            browser.close() 
            exit()
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
    if r.status_code != 200:
        return {"error": "Utilisateur introuvable ou API bloquée"}

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
    #mount_0_0_1I > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.html-div.xdj266r.x14z9mp.xat24cr.x1lziwak.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x9f619.x16ye13r.xvbhtw8.x78zum5.x15mokao.x1ga7v0g.x16uus16.xbiv7yw.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.xvc5jky.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y.x8vgawa > section > main > div > div > header > div > section.x98rzlu.xeuugli > div > div.html-div.xdj266r.x14z9mp.xat24cr.x1lziwak.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x9f619.xjbqb8w.x40hh3e.x78zum5.x15mokao.x1ga7v0g.x16uus16.xbiv7yw.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1

# utiliser la methode Search_Nitter pour Instagram
def instagram_user_info(username):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # False = voir le navigateur
        page = browser.new_page()
        page.goto(SITES["Instagram"].format(username))
        if page.title() == "Profile n’est pas disponible • Instagram": 
            print(f"❌ Utilisateur '{username}' introuvable sur Instagram")
            browser.close() 
            exit()
        
        print("Instagram User Info:")
        print(page)
        Info = { 
            "title": page.title(),
            # "publications": page.locator('span html-span xdj266r x14z9mp xat24cr x1lziwak xexx8yu xyri2b x18d9i69 x1c1uobl x1hl2dhg x16tdsg8 x1vvkbs').first.inner_text(),
            # "followers": page.locator('span html-span xdj266r x14z9mp xat24cr x1lziwak xexx8yu xyri2b x18d9i69 x1c1uobl x1hl2dhg x16tdsg8 x1vvkbs').nth(1).inner_text(),
            # "following": page.locator('span html-span xdj266r x14z9mp xat24cr x1lziwak xexx8yu xyri2b x18d9i69 x1c1uobl x1hl2dhg x16tdsg8 x1vvkbs').nth(2).inner_text(),
            "url_page": page.url
            }
        browser.close()
        print(Info)

# Search_Nitter(username),
# get_reddit_user_info(username)
instagram_user_info(username)
