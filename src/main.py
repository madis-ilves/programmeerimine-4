from infoGatherer import *
from calenderupload import *



lingid = saa_lingid()
tunniajad = saa_tundide_ajad()
klass = input("Sisesta klass: ").upper() # nt "12IT"
tunniplaan = saa_tunniplaan(lingid[klass])
valikained = []
tunniuploadimiseks = [] #google calender api vormis list
#    example append_events(events_to_upload,'skill','issue', ['08:45','09:55'], 'MO','20261231')
day = 0
aeg = 0
dayindex = ['MO','TU','WE','TH','FR','SA','SU']
for paev in tunniplaan:
    
    aeg = 0
    for tund in paev:
        if tund == paev[0]:
            pass
        else:
            name = ''
            #print(tund) #debug asi
            if len(tund) == 1:
                
                string = tund[0]
                if tund == paev[6]:
                    if string != 'Järelevastamine' and '(v)' not in string:
                        string += '(v)'
                        if string not in valikained:
                            valikained.append(aine)
                name = string
            elif len(tund)== 0:
                name = 'no tund'
            else:
                same = True
                valik = False
                for aine in tund:
                    if aine != tund[0]:
                        same = False
                    if '(v)' in aine:
                        valik = True
                        if aine not in valikained:
                            valikained.append(aine)
                if same == True:
                    name = tund[0]
                elif same == False and valik == False:
                    string = ''
                    for aine in tund:
                        string += f'/{aine}'
                    name = string.strip('/')
                else:
                    string = ''
                    for aine in tund:
                        string += f'/{aine}'
                        if '(v)'not in aine:
                            string += ' (v)'
                    name = string.strip('/')
            print(tunniajad[aeg])
            if name != 'no tund':
                append_events(tunniuploadimiseks, name ,'undefined', tunniajad[aeg], dayindex[day],'20261231')
            aeg +=1 #brute force aja järgimine
                    
                    
    
    
    print(dayindex[day])
    day+=1 #brute force paeva järgimine
    
    
print(valikained)
upload_events(tunniuploadimiseks)
