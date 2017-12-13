import pygame
from math import pi,sin,cos,atan,sqrt,asin,acos
from random import uniform as uni
pygame.display.init()

size = width, height = (600,400)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
tem = 1

class ball():
    def __init__(self,x,y,xvel=0,yvel=0,r=0):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
        self.r = r


    def draw(self):
        pygame.draw.circle(screen,(255,0,0),(round(self.x),round(self.y)),round(self.r),0)

    def move(self):
        self.x += self.xvel
        self.y += self.yvel
    def wallcollision(self):
        if self.x < self.r:
            self.x = self.r
            self.xvel *= -1
        if self.x > width - self.r:
            self.x = width - self.r
            self.xvel *= -1
        if self.y < self.r:
            self.y = self.r
            self.yvel *= -1
        if self.y > height - self.r:
            self.y = height - self.r
            self.yvel *= -1

    def ballcollide(self):
        global balls
        for w in balls:
            if w != self:
                xdist = self.x - w.x
                ydist = self.y - w.y
                realdist = sqrt(xdist**2+ydist**2)
                if realdist < self.r+w.r:
                    self.xvel = uni(-tem,tem)
                    self.yvel = uni(-tem,tem)
                    

            

balls = []

j=0
while j != 120:
    tem += 0.05
    j+=1
    radius = uni(2,10)
    x = uni(radius,width-radius)
    y = uni(radius,height-radius)
    nope = False
    for w in balls:
        xdist = x - w.x
        ydist = y - w.y
        if xdist**2+ydist**2 < (radius+w.r)**2:
            j -= 1
            nope = True
            break
    if nope == False:           
        balls.append(ball(x,y,uni(-1,1),uni(-1,1),r=radius))
    print(j)        


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit    

    for b in balls:
        b.move()

    for b in balls:
        b.ballcollide()        
    for b in balls:
        b.wallcollision()

    screen.fill((0,0,0))

    for b in balls:
        b.draw()
    
    pygame.display.flip()
    clock.tick(60)
