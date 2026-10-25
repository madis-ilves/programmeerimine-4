# googleplaan
Graafilise kasutajaliidesega programm, eesmärgiks siduda TTG tunniplaan Google Calendariga  
Valminud TTG programmeerimise 4. kursuse raames  
**Kasutamiseks käivitada *src/main.py***  

### Projekti haldus  
**Rühmaliikmed:** Madis, Hardi, Taaniel  
Ülesannete halduskesskkond Trello: https://trello.com/b/GA9CN42U  
Kokkuvõtvalt tööülesannetest: Madis - HTMLi töötlus ja info leidmine; Hardi - kalendrisse laadimine ja kõige kokku panemine; Taaniel - kasutajaliides  
  
## Täpsem info  
Kasutatud on teeke *requests*(HTML saamine), *BeautifulSoup*(HTML töötlemine), *tkinter*(kasutajaliides) ning Google API(kalendrisse üleslaadimine)  
Google API allalaadimiseks tuleb kasutada käsklust:  
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib  
  
  
*Sisend:* klass, valik selle klassi tunniplaanist leitud kursuste seast(vajalik ka Google sisselogimine; ***OLULINE: Töötab ainult TTG kontoga***)  
*Väljund:* kasutaja valitud kursused laetakse tema Google Calendari ülesse nende õigel toimumise ajal, korduvad kuni perioodi lõpuni  
  
### Ülevaade failidest:
***src/main.py* käivitab programmi**, ühendab projekti erinevad osad(Hardi)  
*src/calenderupload.py* tegeleb Google Calendariga(Hardi)  
*src/infoGatherer.py* saab iga klassi nime ja sellele vastava tunniplaani lingi(Hardi), tundide ajad ja kursuste info(Madis)  
*src/ui3.py* on kasutajaliides(Taaniel+Hardi)  
*src/credentials.json* on Google API tööks vajalik  
  
**Järgmiseid ei ole programmi tööks vaja, aga on tööprotsessi jäädvustamiseks säilitatud:**  
*scr/brlr2.py* oli iseseisev kasutajaliidese baas, millest kujunes välja *ui3.py*(Taaniel)  
*src/tb-tkinter* kaustas on eksperimendid tkinteriga ja esimesed kasutajaliidese katsed(Taaniel)  
*paberprototüüp.png* on esmane prototüüp sellele, kuidas kasutajaliides võiks välja näha(Taaniel)  
*testifailid* kaustas on esimese tunni *test_nimi.py* failid  

 
