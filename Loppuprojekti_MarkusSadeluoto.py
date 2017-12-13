import pygame   #kaiken aa ja oo. Älä hämäänny, kun joitain muuttujia on suomeksi ja useampia englanniksi
from random import randint as ra
pygame.display.init()
pygame.font.init()
text = pygame.font.SysFont("Comic Sans MS", 20)#mainio fontti

näyttö = pygame.display.set_mode((600,600))#luodaan ruutu
pygame.display.set_caption("Hyppäilypeli     varo ruudun ala- ja YLÄreunaa      nuolilla liikutaan")

x = y = 300     #pygamen koordinaatistossa y-arvot kasvavat alaspäin mentäessä
xvel = yvel = 0     #vel = velocity = nopeus
ground_touch = False

kello = pygame.time.Clock()
points = 0

green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)

difficulty = 1 #alkunopeus


def over_edge(x,y):
    if x>585:
        pygame.draw.rect(näyttö,green,(-615+x,y-15,30,30),0)
    if x<15:
        pygame.draw.rect(näyttö,green,(585+x,y-15,30,30),0)        
      
class platform():       #tasot
    def __init__(self,xmin,xmax,y,touch="no",typ=0):
        self.xmin = xmin
        self.xmax = xmax
        self.y = y
        self.touch = touch
        self.typ = typ
        self.timer = 0 #sinisiä varten

    def hit(self,x):#jos hahmo ei ole tasolla
        global y, yvel, ground_touch, touch_y, points, difficulty
        self.touch = "no"
        if self.typ == 2 and y + 15 + yvel + difficulty > self.y + points > y - 20 and yvel<0 and self.xmin-15<x<self.xmax+15:
            yvel *= -1
            y = self.y + points + 20
        
        elif y + 15 + yvel + difficulty > self.y + points > y - 20 and yvel>0 and self.xmin-15<x<self.xmax+15 and self.typ != -1:
            ground_touch = True
            touch_y = self.y
            self.touch = "yes"
    def drop(self,x):#jos hahmo on tasolla
        global ground_touch, yvel
        if self.touch == "yes":
            self.timer += 10
            if self.typ == 1 and self.timer > 200:
                ground_touch = False
                self.touch = "no"
                self.typ = -1
                
            elif self.xmin > x+15 or self.xmax < x-15:
                ground_touch = False
                self.touch = "no"

        
    def draw(self,points):
        global items, q
        if self.y+points > 600: #poistetaan ohjelman nopeuttamiseksi
            items.remove(self)
            q -= 1
        elif self.typ != -1:
            if self.typ == 0:
                color = green
            elif self.typ == 1:
                color = (0,0,255-self.timer)
            else:
                color = red
            pygame.draw.line(näyttö,color,(self.xmin,self.y+points),(self.xmax,self.y+points),10)

items = [platform(0,600,300),platform(200,400,200),platform(250,350,100)]#määritellään ruudulla aluksi olevat tasot
seur = 0        #määrittelee milloin/mihin uusi taso ilmaantuu   
touch_y = 300   #tasolla ollessa y-sijainti
turn = -1       #tämä tasojen vuoropohjaiseen vaihteluun

while 0 < y < 600:#pääsilmukka, toistetaan kunnes pelaaja eksyy kuvaruudun ala- tai yläreuneen, jolloin peli päättyy

    for event in pygame.event.get():#ruksia painettaessa peli loppuu, koska olisi epäloogista, jos niin ei tapahtuisi
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    painettu = pygame.key.get_pressed()#täällä kaikki painetut näppäimet
    x_info = painettu[pygame.K_RIGHT] - painettu[pygame.K_LEFT]
   
    if painettu[pygame.K_UP] and ground_touch == True:
        yvel = -21+difficulty
        ground_touch = False

    xvel += x_info


    if points >= seur:#luodaan uusi taso
        seur = points + 100
        tyyppi = 0
        if turn == 1:
            tyyppi = ra(0,3)
        else:
            tyyppi = ra(0,1)
        if tyyppi == 2:#punainen, aiheuttaa mahdottomia kohtia, jos liian leveää
            platwidth = ra(60,150)
        else:    
            platwidth = ra(60,300)
        left = ra(15,585-platwidth)    
        if tyyppi != 3:
            items.append(platform(left, left + platwidth, -points, typ=tyyppi))
        turn *= -1


    if ground_touch == True:
        yvel=0
        y = points + touch_y - 20    
    else:
        yvel += 1   #gravitaatio
        y += yvel     

    for q in items:     #katsotaan tasojen ja hahmon väliset vuorovaikutukset
        if ground_touch == False:
            q.hit(x)
        elif ground_touch == True:
            q.drop(x)   

    if x<0:
        x=600
    if x>600:#seinän läpi voi kulkea!
        x=0
    
    x += xvel
    xvel *= 0.88
    
    näyttö.fill((0,0,0))
    over_edge(x,y)  #hiano efekti sinun mennessä reunan yli
    pygame.draw.rect(näyttö,green,(x-15,y-15,30,30),0)   #sinä

    kö = text.render(str(round(points)), False, (0, 255, 0))
    näyttö.blit(kö,(5,10))

    q = 0
    while q in range(len(items)):   #en käytä forsilmukkaa, koska se ei ole tässä tarkoituksessa toimivin
        p = items[q]
        p.draw(points)
        q += 1

    difficulty += 0.001     #peli nopeutuu koko ajan
        

    points += difficulty
    pygame.display.flip()
    kello.tick(60)

arvio = ["säälittävää","ei erityisen hyvin","perussuoritus",":-)","hyvä","erinomaista","huippuluokkaa","god","possu","unlimited force"]
näyttö.fill((0,0,0))
kö = text.render("Hävisit. Loppupisteesi oli "+str(round(points)), False,red)
näyttö.blit(kö,(200,300))

if points<500:
    comments = 0
elif points<10500:
    comments = round((points-200)//1250)+1#arvostelussa alle 500 on huonoin, yli 10000 paras, siinä välissä 8 kategoriaa
else:
    comments = 9    
kö = text.render(arvio[comments], False,red)#palautetta suorituksestasi
näyttö.blit(kö,(200,330))
pygame.display.flip()
kello.tick(0.2)

pygame.quit()
raise SystemExit#tein aluksi toisen pelin, mutta sitten vaihdoinkin tähän. Tunteja tekoon meni noin 6.
