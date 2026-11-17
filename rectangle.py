import pygame
pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
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
    def rect_change(self,w,s,a,c):
        self.x += w
        self.y += s
        self.border += a
        self.color = c
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height),self.border)
rect1 = rectangle(450,200,"green",0,0,2)
rect2 = rectangle(450,200,"pink",150,400,0)
rect1.draw_rectangle()
rect2.draw_rectangle()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                screen.fill("white")
                rect1.rect_change(0,-25,0,"black")
            if event.key == pygame.K_LEFT:
                screen.fill("white")
                rect1.rect_change(-25,0,0,"black")
            if event.key == pygame.K_RIGHT:
                screen.fill("white")
                rect1.rect_change(25,0,0,"black")
            if event.key == pygame.K_DOWN:
                screen.fill("white")
                rect1.rect_change(0,25,0,"black")
        pygame.display.update() 

