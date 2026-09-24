from bs4 import BeautifulSoup
import requests

uel =  "https://tammegymnaasium.ee/tunniplaanike/view/klass/3ECB72B69D529F51"

page = requests.get(uel)
soup = BeautifulSoup(page.text, features="html.parser")

crack = soup.find('ul', class_ = 'dropdown-menu scrollable-menu')
aaaa = crack.find_all('a')

somelist = {}
for link in aaaa:
    skill = link.text
    issue = link.get('href')
    somelist[skill] = issue
print(somelist)
klass = input("sisestaklass")
print(somelist[klass])
    





