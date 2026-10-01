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
    praegune_rida = []
    praegune_päev_on_üks_kursus = [] #selleks, et jätta meelde tühjad kohad reas
    
    # töötle läbi kõik read
    for tr_tag in tr_tags:
        # kui on uus päev
        if ridu_uue_päevani <= 0: # alguseks on see -1
            on_esimene_rida_päevas = True
            päev = tr_tag.find("th")
            päeva_pikkus = int(päev["rowspan"]) # leiab <th> omaduse rowspan väärtuse(ehk mitu tr_tag'i on selles päevas)
            
            # salvesta praeguse päeva info kui see pole esimene loop(muidu pole midagi salvestada)
            if ridu_uue_päevani != -1: 
                tunniplaan.append(praegune_päev)
                praegune_päev = []
                print(praegune_päev_on_üks_kursus)
                praegune_päev_on_üks_kursus = [] # selleks, et jätta meelde tühjad kohad reas
            ridu_uue_päevani = päeva_pikkus
        
        td_tags = tr_tag.find_all("td") # leia kõik read selles päevas
        # töötle läbi üks rida
        praegune_rida = []
        koht_reas = -1
        for td_tag in td_tags:   # kasuta len(td_tags) et teha valmis listid tunniplaani sisse, et saaks lisada asju igale järgmisele reale
            koht_reas += 1
            # kursuste nimede leidmine
            td_rowspan = int(td_tag["rowspan"])
            if td_rowspan > 1: # tunni ajal on ainult üks kursus
                kursus = td_tag.find("div", class_ = "celltext")
                if on_esimene_rida_päevas:
                    praegune_päev_on_üks_kursus.append(True)
            elif td_rowspan == 1: # tunni ajal on mitu kursust
                kursus = td_tag.find("div", class_ = "celltext5")
                if on_esimene_rida_päevas:
                    praegune_päev_on_üks_kursus.append(False)
            if kursus != None:
                kursuse_nimi = kursus.text # error kui kursus on None, sest tühi koht selles reas; aga mitte ainult üks kursus
                praegune_rida.append(kursuse_nimi)
            else:
                praegune_rida.append(None)
                
            if praegune_päev_on_üks_kursus[koht_reas] and on_esimene_rida_päevas: # siis peaks iga ülejäänud rida olema siin kohal None
                praegune_rida.append("test") # siin peaks olema kõik järgmised read
        
        # üks rida läbi töötatud
        on_esimene_rida_päevas = False
        praegune_päev.append(praegune_rida)
        ridu_uue_päevani -= 1
    
    #sorteeritud ridadeks
    
    
    
    
    
    return tunniplaan

#
# DEBUG - tunniplaani printimine; hiljem pole seda vaja, tuleb visuaalselt ja kalendrisse
#

def print_tunniplaan(tunniplaan):
    for päev in tunniplaan:
        print("\n UUS PÄEV \n")
        for rida in päev:
            print(rida)

# funktsioonide kutsumine

lingid = saa_lingid()
klass = input("Sisesta klass: ").upper() # nt "12IT"
tunniplaan = saa_info(lingid[klass])
print_tunniplaan(tunniplaan)