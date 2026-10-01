from bs4 import BeautifulSoup
import requests


#
# Klasside nimed ja tunniplaani lingid - Hardi + Madis tegi ilusamaks
# tagastab lingid

def saa_lingid():
    lingid = {}
    url =  "https://tammegymnaasium.ee/tunniplaanike/"
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
# tagastab tunniplaani kujul tunniplaan[päev][tund][kursus]

def saa_info(tunniplaani_link):
    tunniplaan = [] # tunniplaan[päev][tund][kursus]
    tunniplaan_raw = requests.get(tunniplaani_link)
    soup = BeautifulSoup(tunniplaan_raw.text, features="html.parser")
    tbody_tag = soup.find("tbody")
    tr_tags = tbody_tag.find_all("tr")
    # 1 tr = 1 rida tunniplaanis
    ridu_uue_päevani = -1 # mitu <tr> on veel alles selles päevas, alguseks -1; teisisõnu max kursuste arv ühe tunni ajal sel päeval
    # <tr> sees on <td>'d, igaüks on üks tund selles reas
    praegune_päev = [] # praeguse päeva info, temp muutuja, uue päeva alguses salvestatakse see tunniplaani ja kustutatakse
    
    # töötle läbi kõik read
    for tr_tag in tr_tags:
        # kui on uus päev, leia päeva pikkus
        if ridu_uue_päevani <= 0: # alguseks on see -1
            if ridu_uue_päevani != -1: # salvesta praeguse päeva info kui see pole esimene loop(muidu pole midagi salvestada)
                tunniplaan.append(praegune_päev)
                praegune_päev = []
            päev = tr_tag.find("th")
            päeva_pikkus = int(päev["rowspan"]) # leiab <th> omaduse rowspan väärtuse(ehk mitu tr_tag'i on selles päevas)
            ridu_uue_päevani = päeva_pikkus
        
        td_tags = tr_tag.find_all("td") # leia kõik read selles päevas
        # töötle läbi üks rida
        for td_tag in td_tags:
            # kursuste nimede leidmine
            td_rowspan = int(td_tag["rowspan"])
            if td_rowspan > 1: # tunni ajal on ainult üks kursus
                kursus = td_tag.find("div", class_ = "celltext")
            elif td_rowspan == 1: # tunni ajal on mitu kursust
                kursus = td_tag.find("div", class_ = "celltext5")
            if kursus != None:
                kursuse_nimi = kursus.text # error kui kursus on None, sest tühi koht selles reas TODO: jäta meelde tühjad kohad ja grupeeri kursused tundidesse
                praegune_päev.append(kursuse_nimi)
            #else:
             #   praegune_päev.append(None)
        
        # üks rida läbi töötatud
        ridu_uue_päevani -= 1
    
    return tunniplaan

#
# DEBUG - tunniplaani printimine; hiljem pole seda vaja, tuleb visuaalselt ja kalendrisse
#

def print_tunniplaan(tunniplaan):
    for päev in tunniplaan:
        print("\n UUS PÄEV \n")
        for tund in päev:
            print(tund)

# funktsioonide kutsumine

lingid = saa_lingid()
klass = input("Sisesta klass: ").upper() # nt "12IT"
tunniplaan = saa_info(lingid[klass])
print_tunniplaan(tunniplaan)