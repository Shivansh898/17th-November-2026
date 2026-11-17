import pygame
pygame.init()
WIDTH = 800
HEIGHT = 800 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("white")
class circle():
    def __init__(self,radius,color,x,y,border):
        self.radius = radius
        self.color = color
        self.y = y
        self.x = x
        self.border = border
    def draw_circle(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,self.border)
    def circle_larger(self,x):
        self.radius+=x
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,self.border)
    def circle_change(self,w,s,a,c):
            self.x += w
            self.y += s
            self.border += a
            self.color = c
            pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,self.border)
class rectangle():
    def __init__(self,width,height, color,x,y,border):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y
        self.border = border
    def draw_rectangle(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height),self.border)
    def custom_rect(self):
        global WIDTH,HEIGHT
        self.width = int(input("Enter the width: "))
        WIDTH = self.width +80
        self.height = int(input("Enter the height: "))
        HEIGHT = self.height +80
        self.color = str(input("Enter a color: "))
        self.x = int(input("Enter the 'x' value: "))
        self.y = int(input("Enter the 'y' value: "))
        self.border = int(input("Enter border size: "))
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height),self.border)
    
circle1 = circle(50,"black",400,400,0)
rect1 = rectangle(200,250,"pink",525,500,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                circle1.circle_larger(20)
            if event.button == 3:
                screen.fill("white")
                circle1.circle_larger(-20)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                screen.fill("white")
                circle1.circle_change(0,-25,0,"black")
            if event.key == pygame.K_LEFT:
                screen.fill("white")
                circle1.circle_change(-25,0,0,"black")
            if event.key == pygame.K_RIGHT:
                screen.fill("white")
                circle1.circle_change(25,0,0,"black")
            if event.key == pygame.K_DOWN:
                screen.fill("white")
                circle1.circle_change(0,25,0,"black")
            if event.key == pygame.K_c:
                screen.fill("white")
            if event.key == pygame.K_q:
                screen.fill("white")
                circle1.circle_change(0,0,2,"black")
            if event.key == pygame.K_r:
                screen.fill("white")
                circle1.circle_change(0,0,0,"red")
            if event.key == pygame.K_y:
                screen.fill("white")
                circle1.circle_change(0,0,0,"yellow")
            if event.key == pygame.K_g:
                screen.fill("white")
                circle1.circle_change(0,0,0,"green")
            if event.key == pygame.K_b:
                screen.fill("white")
                circle1.circle_change(0,0,0,"blue")
            if event.key == pygame.K_r:
                screen.fill("white")
                rect1.draw_rectangle()
            if event.key == pygame.K_c:
                screen.fill("white")
                circle1.circle_larger(20)
            if event.key == pygame.K_l:
                screen.fill("white")
                pygame.draw.line(screen,"green",(50,50),(400,500),4)

        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            circle2 = circle(1,"black",pos[0],pos[1],0)
            circle2.draw_circle()
            
    pygame.display.update()
    
