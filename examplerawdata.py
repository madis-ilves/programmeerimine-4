from bs4 import BeautifulSoup
import requests

uel =  "https://tammegymnaasium.ee/tunniplaanike/view/klass/3ECB72B69D529F51"

page = requests.get(uel)
soup = BeautifulSoup(page.text, 'html')

print(soup)
