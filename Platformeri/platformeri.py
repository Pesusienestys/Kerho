import pygame
pygame.display.init()
size = height, width = (1000,500)
screen = pygame.display.set_mode(size)

ö = open("level.txt","r")
rows = ö.readlines()
ö.close()

clock = pygame.time.Clock()

green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)

class block():
    def __init__(self,x,y,style):
        self.x = x
        self.y = y
        self.style = style
        
    def draw(self):
        if self.style == "B":
            color = blue
        elif self.style == "R":
            color = red
        elif self.style == "G":
            color = green
        else:
            color = white
        pygame.draw.rect(screen, color,(self.x*50, self.y*50, 50, 50),0)
    def collision(self):
        global yvel, xvel, your_x, your_y
        box_x = self.x+25
        box_y = self.y+25
        if your_x - 50 < box_x or your_x + 50 > box_x:#jatka tästä
            xvel *= -1
            your_x += xvel

blocks = []

n=0
for a in rows:
    m = 0
    for b in a:
        if b != " ":
            blocks.append(block(m,n,b))
        m += 1    
    n += 1

your_x = 100
your_y = 100
xvel = 0
yvel = 0
ground_touch = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    pressed = pygame.key.get_pressed()
    x_info = pressed[pygame.K_RIGHT] - pressed[pygame.K_LEFT]
    y_info = pressed[pygame.K_UP] - pressed[pygame.K_DOWN]

    xvel += x_info
    xvel *= 0.8
    your_x += xvel
    
        
    for q in blocks:
        q.collision()        
    
    screen.fill((0,0,0))

    for q in blocks:
        q.draw()
    pygame.draw.rect(screen,(0,255,255),(your_x-25,your_y-25,50,50),0)    

    pygame.display.flip()
    clock.tick(60)   
    
       

        


