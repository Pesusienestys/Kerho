import pygame

def törmäys(x, y, xnop, ynop, laatikot, piikit, loppu, pelaaja, ycheck):

    nop = 0

    for laatikko in laatikot:

        if pelaaja.colliderect(laatikko):

            # Voitto ja häviö

            for piikki in piikit:
                if pelaaja.colliderect(piikki):
                    print('Hävisit!')
                    pygame.quit()
                    raise SystemExit
                
            if pelaaja.colliderect(loppu):
                print('Voitit!')
                pygame.quit()
                raise SystemExit

            # Tarkistetaan törmäykset akseli kerrallaan
                
            if xnop == 1:
                pelaaja.right = laatikko.left

            if xnop == -1:
                pelaaja.left = laatikko.right

            if ynop > 0:

                pelaaja.bottom = laatikko.top
                ynop = 0
                            
                if ycheck == 1:
                   nop = int((kerroin * 22.5) / -32)
                    
            if ynop < 0:
                pelaaja.top = laatikko.bottom
                ynop = 0

    if nop != 0:
        ynop = nop

    x = pelaaja.left
    y = pelaaja.top

    return x, y, ynop

pygame.init()

piikin_kuva = pygame.image.load("Piikki.png")

kerroin = 1260

x = 0
y = 0

kello = pygame.time.Clock()

ynop = 0
ycheck = 0

tasonLeveys = 0
tasonKorkeus = 0

laatikot = []
piikit = []
väli = []

aloitus = []
lopetus = []

# Tiedostoon voi tehdä oman tason
# L = laatikko, E = end(lopetus), S = start(aloitus), P = piikki

while True:
    try:
        with open(input ('Anna haluttu taso (Tasox.txt, x on tason numero): '), 'r') as taso:
            rivit = taso.readlines()

            for rivi in rivit:
                for sarake in rivi:

                    sarake = sarake.upper()
                     
                    if sarake == 'L':
                        laatikko = (x, y)
                        laatikot.append (laatikko)
                          
                    if sarake == 'E':
                        end = (x, y)
                        laatikot.append (end)
                        loppu = (x, y)
                        lopetus.append(end)
                            
                    if sarake == 'S':
                        alku = (x, y)
                        alku_x = x
                        alku_y = y
                        aloitus.append(alku)

                    if sarake == 'P':
                        piikki = (x, y)
                        laatikot.append(piikki)
                        piikit.append(piikki)
                            

                    x += 1

                x -= 1

                if x > tasonLeveys: tasonLeveys = x
                    
                x = 0
                y += 1

            tasonKorkeus = y
            break

    except:
        print ('Kirjoittamaasi tasoa ei ole.\n')
# Rakennetaan taso



# Tarkistetaan aloituksien ja lopetuksien määrä

e = 0

if len(lopetus) == 0:
    print('Sinulla ei ole lopetuspistettä')
    e = 1

if len(lopetus) > 1:
    print('Sinulla on liian monta lopetuspistettä')
    e = 1

if len(aloitus) == 0:
    print('Sinulla ei ole aloituspistettä')
    e = 1

if len(aloitus) > 1:
    print('Sinulla on liian monta aloituspistettä')
    e = 1

if e == 1:
    pygame.quit()
    raise SystemExit

# Skaalataan taso niin, että se mahtuu kokonaisena näytölle

while True:
    if tasonKorkeus * kerroin > 660 or tasonLeveys * kerroin > 1260:
        kerroin = kerroin - (kerroin / 10)

    else: break

kerroin = int (kerroin)

laatikonKoko = kerroin

korkeus = tasonKorkeus * kerroin
leveys = tasonLeveys * kerroin

näyttö = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption('(Ei vielä niin) Hiano platformeri!')

x = alku_x * kerroin
y = alku_y * kerroin

# Muutetaan laatikot ja piikit rect-muotoon,
# jotta niitä on helpompi käsitellä myöhemmin

for laatikko in laatikot:
    a, b = laatikko
    laatikko = pygame.Rect(a * kerroin, b * kerroin, laatikonKoko, laatikonKoko)
    väli.append(laatikko)

laatikot = väli
väli = []

for piikki in piikit:
    a, b = piikki
    piikki = pygame.Rect(a * kerroin, b * kerroin, laatikonKoko, laatikonKoko)
    väli.append(piikki)

piikit = väli
väli = []

loppul = pygame.Rect(loppu[0] * kerroin, loppu[1] * kerroin, laatikonKoko, laatikonKoko)

# Skaalataan piikin kuva

piikin_kuva = pygame.transform.scale(piikin_kuva, (laatikonKoko, laatikonKoko))

# Pelin looppi, jossa käsitellään koko pelaaminen
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            raise SystemExit

    # Tarkistetaan mitä nappia painetaan ja mitä tehdään

    xnop = 0

    painettu = pygame.key.get_pressed()
    
    if painettu[pygame.K_UP]:
        ycheck = 1
        
    if painettu[pygame.K_LEFT]:
        
        x -= kerroin / 6
        xnop = -1

    if painettu[pygame.K_RIGHT]:
        
        x += kerroin / 6
        xnop = 1

    # Rajoitetaan gravitaatio

    if ynop > laatikonKoko * (4/5):
        ynop = laatikonKoko * (4/5)

    # Kokeillaan törmäyksien varalta akseli kerrallaan

    pelaaja = pygame.Rect(x, y, laatikonKoko, laatikonKoko)
    väli = ynop

    x, y, ynop = törmäys(x, y, xnop, 0, laatikot, piikit, loppul, pelaaja, ycheck)

    ynop = väli
    y += ynop
    ynop += laatikonKoko / 30
    pelaaja = pygame.Rect(x, y, laatikonKoko, laatikonKoko)

    x, y, ynop = törmäys(x, y, 0, ynop, laatikot, piikit, loppul, pelaaja, ycheck)

    # Pidetään pelaaja näytön sisällä
    if y < 0:
        y = 0
        ynop = 0
    if y > korkeus - laatikonKoko:
        y = korkeus - laatikonKoko
        ynop = 0
        if ycheck == 1:
            ynop = int((kerroin * 22.5) / -32)
    if x < 0:
        x = 0
    if x > leveys - laatikonKoko:
        x = leveys - laatikonKoko

    ycheck = 0

    pelaaja = pygame.Rect(x, y, laatikonKoko, laatikonKoko)

    for laatikko in laatikot:
        if pelaaja.colliderect(laatikko):
            y += laatikonKoko

    # Piirretään kaikki
    
    näyttö.fill((0, 0, 0))
    
    for laatikko in laatikot:
        tarkistus = 0
        for piikki in piikit:
            if piikki == laatikko:
                tarkistus = 1

        if tarkistus == 0:
            
            a = laatikko[0]
            b = laatikko[1]
            laatikko = pygame.draw.rect(näyttö, (128, 128, 128), (a, b, laatikonKoko, laatikonKoko))

    for piikki in piikit:
            
        a = piikki[0]
        b = piikki[1]
        näyttö.blit(piikin_kuva, (a, b))


    pygame.draw.rect(näyttö, (0, 255, 0), (loppu[0] * kerroin, loppu[1] * kerroin, laatikonKoko, laatikonKoko))

    pygame.draw.rect(näyttö, (255, 255, 255), (x, y, laatikonKoko, laatikonKoko))

    pygame.display.update()
    kello.tick(60)
