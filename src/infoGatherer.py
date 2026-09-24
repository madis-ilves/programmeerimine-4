from bs4 import BeautifulSoup
import requests


#
# Klasside nimed ja tunniplaani lingid - Hardi + Madis tegi ilusamaks
#

def saa_lingid():
    lingid = {}
    url =  "https://tammegymnaasium.ee/tunniplaanike/view/klass/3ECB72B69D529F51" # ükskõik mis klassi link
    page = requests.get(url) # html
    soup = BeautifulSoup(page.text, features="html.parser")

    dropdown_menu = soup.find('ul', class_ = 'dropdown-menu scrollable-menu') # dropdown menu - klasside nimekiri
    a_tags = dropdown_menu.find_all('a') # siin on klass+tunniplaani link

    for a_tag in a_tags:
        klassi_nimi = a_tag.text # nt "12IT"
        link = a_tag.get('href')
        lingid[klassi_nimi] = link
    return lingid



#
# Klassi tunniplaanist info - Madis
#

def saa_info(tunniplaani_link):
    tunniplaan = [] # tunniplaan = päev; tund; kursus
    tunniplaan_raw = requests.get(tunniplaani_link)
    soup = BeautifulSoup(tunniplaan_raw.text, features="html.parser")
    tbody_tag = soup.find("tbody")
    tr_tags = tbody_tag.find_all("tr")
    # 1 tr = 1 rida tunniplaanis
    ridu_uue_päevani = 0 # mitu <tr> on veel alles selles päevas
    # <tr> sees on <td>'d, igaüks on üks tund selles reas
    praegune_päev = [] # praeguse päeva info
    
    for tr_tag in tr_tags:
        # kui on uus päev, leia päeva pikkus
        if ridu_uue_päevani == 0: 
            päev = tr_tag.find("th") # <th>
            päeva_pikkus = int(päev["rowspan"]) # leiab <th> omaduse rowspan väärtuse(ehk mitu tr_tag'i on selles päevas)
            ridu_uue_päevani = päeva_pikkus
        td_tags = tr_tag.find_all("td")
        for td_tag in td_tags:
            td_rowspan = int(td_tag["rowspan"]) # seda kasutada celltext5 vs celltext jaoks
            #print(td_tag)
            #print(td_rowspan)
            if td_rowspan > 1: # celltext5 on siis kui selle tunni ajal on mitu kursust(ehk rowspan on 1), muidu celltext
                kursus = td_tag.find("div", class_ = "celltext")
            elif td_rowspan == 1:
                kursus = td_tag.find("div", class_ = "celltext5")
            if kursus != None:
                kursuse_nimi = kursus.text # error kui kursus on None, sest tühi koht selles reas
                print(kursuse_nimi)
        
        #loopi lõpp, üks rida läbi töötatud
        ridu_uue_päevani -= 1
        
    

# funktsioonide kutsumine

lingid = saa_lingid()
klass = input("Sisesta klass: ").upper() # nt "12IT"
saa_info(lingid[klass])