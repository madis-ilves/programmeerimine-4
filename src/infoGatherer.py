from bs4 import BeautifulSoup
import requests


#
# Klasside nimed ja tunniplaani lingid - Hardi + Madis tegi ilusamaks
# tagastab lingid sõnastikuna, kus link = saa_lingid()[klassi_nimi], link ja klassi_nimi on str

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
# Tundide ajad
# tagastab tundide ajad 2d järjendina, välimine on tund ja sisemine on algus ja lõpp

def saa_tundide_ajad():
    url =  "https://tammegymnaasium.ee/tunniplaanike/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html.parser")
    
    thead = soup.find('thead')
    ajad = thead.find_all("div", class_ = "aeg")
    
    tundide_ajad = []
    
    for aeg in ajad:
        tund = aeg.text.split(" - ")
        tundide_ajad.append(tund)
    
    return tundide_ajad
        
#
# Klassi tunniplaanist info - Madis
# tagastab tunniplaani järjendina, kus kursus = saa_tunniplaan(tunniplaani_link)[päev][tund][kursus], päev ja tund on int, kursus ja tunniplaani_link on str

def saa_tunniplaan(tunniplaani_link):
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
        td_tags = tr_tag.find_all("td") # leia kõik read selles päevas
        
        # kui on uus päev
        if ridu_uue_päevani <= 0: # alguseks on see -1
            on_esimene_rida_päevas = True
            päev = tr_tag.find("th")
            päeva_pikkus = int(päev["rowspan"]) # leiab <th> omaduse rowspan väärtuse(ehk mitu tr_tag'i on selles päevas)
            ridu_uue_päevani = päeva_pikkus

            # kasuta len(td_tags) et teha valmis listid tunniplaani sisse, et saaks lisada asju igale järgmisele reale
            kohti_reas = len(td_tags) # max tundide arv
            for _ in range(kohti_reas):
                praegune_päev.append([])

        # töötle läbi üks rida
        praegune_rida = []
        koht_reas = -1
        for td_tag in td_tags:

            koht_reas += 1
            if not on_esimene_rida_päevas:
                for value in praegune_päev_on_üks_kursus[koht_reas:]: # liigu edasi järgmise kohani, kus pole ainult 1 tund(vist)
                    if value:
                        koht_reas += 1
                    else:
                        break
    
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
            
            # kursuste nimede salvestamine
            if kursus != None: # kui kursus on None, siis tühi koht selles reas, aga mitte ainult üks kursus
                kursuse_nimi = kursus.text 
                praegune_päev[koht_reas].append(kursuse_nimi)
            else:
                praegune_päev_on_üks_kursus[koht_reas] = True # kui kursus on None, siis on selles kohas kursused otsas ja selle peaks vahele jätma
            
        
        # üks rida läbi töötatud
        on_esimene_rida_päevas = False
        ridu_uue_päevani -= 1
        # kui tuleb uus päev
        if ridu_uue_päevani == 0:
            tunniplaan.append(praegune_päev)
            praegune_päev = []
            praegune_päev_on_üks_kursus = [] # selleks, et jätta meelde tühjad kohad reas, elemendid True/False iga tunni kohta
            
    return tunniplaan

#
# DEBUG - tunniplaani printimine; hiljem pole seda vaja, tuleb visuaalselt ja kalendrisse
#

def print_tunniplaan(tunniplaan):
    for päev in tunniplaan:
        print("\n UUS PÄEV \n")
        for tund in päev:
            print(tund)

#
# funktsioonide kutsumine
#

if __name__ == "__main__":
    lingid = saa_lingid()
    print(saa_tundide_ajad())
    klass = input("Sisesta klass: ").upper() # nt "12IT"
    tunniplaan = saa_tunniplaan(lingid[klass])
    #print_tunniplaan(tunniplaan)
    
    