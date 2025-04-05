from bs4 import BeautifulSoup
import requests

url = "https://uaserials.pro/films/"
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")


soup_list_href = soup.find_all("a", {"class": "short-img img-fit"})


with open("link.txt", "w", encoding="utf-8") as f:
    for href in soup_list_href:
        link = href.get("href")
        if link:
            print(link)
            f.write(f"{link}\n")

f.close()
