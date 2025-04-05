import requests

# response = requests.get("https://uaserials.pro/films/")
# print(response.content)
# print(type(response.content))
# response = requests.post("https://httpbin.org/get/", data="Test data")
# headers = {'h1':"Test title"}
# print(response.text)


import requests

response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")

for pars_elem_1 in response_parse:
    if pars_elem_1.startswith('$'):
        for pars_elem_2 in pars_elem_1.split('</span>'):
            if pars_elem_2.startswith('$') and len(pars_elem_2) > 1 and pars_elem_2[1].isdigit():
                print(pars_elem_2)
                print(pars_elem_2)
