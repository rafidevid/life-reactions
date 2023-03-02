import requests
import re
import random
import time
from bs4 import BeautifulSoup as parser

url = "https://mbasic.facebook.com"

cookie = ""

headers = {"cookie": cookie}
data = []

def parsing(url, headers):
    req = requests.get(url, headers=headers)
    html = parser(req.text, "html.parser")
    return html
    
def pick_reactions(base_url, headers):
    global data
    html = parsing(base_url, headers)
    for r in html.find_all("a"):
        if "/ufi/reaction" in str(r["href"]):
            data.append(url+str(r["href"]))
            h = requests.get(random.choice(data), headers=headers)
            print(h)
            time.sleep(5)
    
def more_request(html, headers):
    for tanggapi in html.find_all("a", string="Tanggapi"):
        base_url = url+str(tanggapi["href"])
        pick_reactions(base_url, headers)
    if "Lihat Berita Lain" in str(html):
        lanjut = url+str(html.find("a", string="Lihat Berita Lain")["href"])
        main(lanjut, headers)
    else:
        main(url, headers)

def main(url, headers):
    html = parsing(url, headers)
    more_request(html, headers)
    
if __name__ == '__main__':
    main(url, headers)
