# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("https://coinmarketcap.com/")
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, features="html.parser")
#     # Find all the anchor tags with the given href for Bitcoin
#     soup_list = soup.find_all("a", href="/currencies/bitcoin/#markets")
#
#     # Print the text of the first element found
#     if soup_list:
#         res = soup_list[0]
#         print(res.text)
#     else:
#         print("No matching links found.")
#

from bs4 import BeautifulSoup
import requests

url = "https://uaserials.pro/films/"
r = requests.get(url)


soup = BeautifulSoup(r.text, features="html.parser")


soup_list_name = soup.find_all('div', {"class": "th-title truncate"})

name_list = []


for i in soup_list_name:
    name_list.append(i.text.strip())


print(name_list)

