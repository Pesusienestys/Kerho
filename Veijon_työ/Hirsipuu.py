
#Def==================================

import random
tiedostå = open("kotus sanat.txt")
sanat = tiedostå.readlines()
käytetyt = []

#Ohjeet===============================================================================

o = input("Tervetuloa pelaamaan Veijon hirsipuuta. Syötä 'o', jos haluat lukea ohjeet. ")

if o == "o":
    print("")
    print("Ohjeet: Tietokone arpoo satunnaisen sanan tiedostosta 'kotus sanat.txt'. \n"+
          "Sinun täytyy arvata kirjimia yksi kerrallaan. Jos arvaat kirjaimen \n"+
          "joka ei kuulu sanaan, menetät yhden elämän. Jos arvaat oikein, \n"+
          "kirjain menee paikalleen. Voitat, kun koko sana on valmis. \n"+
          "Voit myös valita vaikeustason, joka määrää elämien määrän.")
else:
    pass

#Sanan arvonta==================================
      
print("")
sana = sanat[random.randint(0, len(sanat))]
sana.split()
listana = []
for i in sana:
    if i != "\n":    
        listana.append(i)

#Vaikeustason funktio==============================================
        
def elämä():
    vaikeustaso = input("Syötä vaikeustaso (1, 2 tai 3):")
    global elämät, onnittelutaso
    while True:
        if vaikeustaso == "1":
            elämät = 10
            onnittelutaso = "helpolla"
            break
        if vaikeustaso == "2":
            elämät = 7
            onnittelutaso = "keskimmäisellä"
            break
        if vaikeustaso == "3":
            elämät = 3
            onnittelutaso = "vaikeimmalla"
            break
        if vaikeustaso != "1" or "2" or "3":
            print(" Ei hyväksytä.")
            break
    try:    
        print(" Elämät:"  +str(elämät))
    except:
        elämä()
elämä()

#Peli alkaa===============================================

uuslista = ["_ "]*(len(sana)-1)
print("  Sanan pituus on "+str(len(listana))+" kirjainta. ")
print("")
print(len(listana)*"_ ")

#Loopit alkaa========================

while True:
    while True:
        print("")
        if elämät == 0:
            break
        if uuslista == listana:
            break

#Virheelliset arvaukset==============================
        
        arvaus = input("Arvaa kirjain: ")
        if arvaus in käytetyt:
            print(" Arvasit jo tämän kirjaimen.")
            break

        if arvaus == "å":
            print("Ei mitään itsemurhia.")
            break

        while True:
            if len(arvaus) == 1:
                break
            else:
                print(" Syötä YKSI kirjain.")
                break
        
#Oikein ja väärin======================================
            
        if arvaus in listana:
            print(" "+arvaus+" on sanassa.")
            käytetyt.append(arvaus)
            
        if arvaus not in listana and len(arvaus) == 1:
            print(" VÄÄRIN")
            elämät = elämät-1
            käytetyt.append(arvaus)
            if elämät != 0 or 1:
                print("  Elämät: "+str(elämät))
                break

#Hieno visuaalinen osuus=================================================
            
        if arvaus in listana:
            for kirjain in listana and käytetyt:
                s = [i for i, uuslista in enumerate(listana) if kirjain in uuslista]
                for k in s:
                    uuslista[k] = kirjain
            print("  "+"".join(map(str,uuslista)))

#Voitto ja häviö======================================
            
        if uuslista == listana:
            print("")
            print("Onneksi olkoon! Voitit "+onnittelutaso+" vaikeustasolla!")
            print("")
        break
    if elämät == 0:
        print("")
        print("HÄVISIT! Sana olisi ollut "+sana)
        break
    if uuslista == listana:
        break

#Lopetus==========================================================

loppu = input("Kiitos kun pelasit! Paina Enter lopettaaksesi.")
if loppu == loppu:
    print()
