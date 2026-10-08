# programmeerimine-4
Graafilise kasutajaliidesega programm, eesmärgiga siduda TTG tunniplaan Google Calendariga  
Valminud TTG programmeerimise 4. kursuse raames  
### Projekti haldus  
**Rühmaliikmed:** Madis, Hardi, Taaniel  
Ülesannete halduskesskkond Trello: https://trello.com/b/GA9CN42U  
Kokkuvõtvalt tööülesannetest: Madis - HTMLi töötlus ja info leidmine; Hardi - HTML saamine, kalendrisse laadimine; Taaniel - kasutajaliides  
  
## Täpsem info  
*Sisend:* klass, valik selle klassi tunniplaanist leitud kursuste seast(vajalik ka Google sisselogimine; ***OLULINE: Töötab ainult TTG kontoga***)  
*Väljund:* kasutaja valitud kursused laetakse tema Google Calendari ülesse nende õigel toimumise ajal, korduvad kuni perioodi lõpuni  
  
Kasutatud on teeke requests(HTML saamine), BeautifulSoup(HTML töötlemine), tkinter(kasutajaliides) ning Google API(kalendrisse üleslaadimine)  
  
### Ülevaade failidest:  
testifailid kaustas on esimese tunni test_nimi.py failid  
src/calenderupload.py tegeleb Google Calendariga(Hardi), hetkel prototüüp testimiseks  
src/infoGatherer.py saab iga klassi nime ja sellele vastava tunniplaani lingi(Hardi), tundide ajad ja kursuste info(Madis)  
paberprototüüp.png on esmane prototüüp sellele, kuidas kasutajaliides võiks välja näha(Taaniel)  
src/tb-tkinter kaustas on eksperimendid tkinteriga
src/tb-tkinter/prog-CURRENT.zip failis on esmane, paberprototüübist lähtuv liides(Taaniel), loodud pigem õppeesmärgil, täpsustunud vajaduste jaoks on vaja keerulisemat  
