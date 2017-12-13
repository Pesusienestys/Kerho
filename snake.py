import pygame
from math import sin,cos
from random import uniform, randint

pygame.display.init()

size = width, height = (600,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

points = 0
colors = [(0,255,0),(255,0,0),(0,0,255)]
tail = []
class bodypart():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self):
        global color, tail
        pygame.draw.circle(screen,colors[randint(0,(randint(0,randint(0,2))))],(round(self.x),round(self.y)),10)

def die(x,y,t):
    global points
    n=9
    while n < len(t)-1:
        n += 1
        h = t[n]
        if (h.x-x)**2+(h.y-y)**2 <400:
            points = 0
            

headX = 300
headY = 300
direction = 0
add = 15

fx,fy,fs,fd = 300,300,6,1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    press = pygame.key.get_pressed()
    direction += (press[pygame.K_RIGHT]-press[pygame.K_LEFT])/40

    length = points+10
    if add != 0:
        add -= 1
    else:
        add = 30
        
    if add%10 == 0:
        tail.append(bodypart(x=headX,y=headY))

    if len(tail)==length:
        tail.remove(tail[0])
    

    headX += cos(direction)
    headY += sin(direction)

    if (fx-headX)**2+(fy-headY)**2 < (7+fs)**2:
        points += 10
        fx = randint(10,590)
        fy = randint(10,590)
        fs = 6
        fd = 1
    if round(fs) in [5,15]:
        fd *= -1
    fs += fd /4

    die(headX,headY,tail)

    if headX < -5:  headX = 605
    if headX > 605: headX = -5
    if headY < -5:  headY = 605
    if headY > 605: headY = -5
        
    screen.fill((0,0,0))

    for u in tail:
        u.draw()

    pygame.draw.circle(screen,(255,255,255),(fx,fy),round(fs))
    pygame.draw.circle(screen,(255,255,0),(round(headX),round(headY)),10)
    pygame.draw.circle(screen,(0,0,255),(round(headX+cos(direction+1)*7),round(headY+sin(direction+1)*7)),3)
    pygame.draw.circle(screen,(0,0,255),(round(headX+cos(direction-1)*7),round(headY+sin(direction-1)*7)),3)


    pygame.display.flip()
    clock.tick(100)
