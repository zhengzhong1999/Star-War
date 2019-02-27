import pygame
from sys import exit
import random


class Bullet:
    def __init__(self):
        self.x=0
        self.y=-1
        self.image= pygame.image.load('bullet.png').convert_alpha()
        self.active=False

    def move(self):
        if self.active:
            self.y-=3
        if self.y<0:
            self.active=False
            
    def restart(self):
        mousex,mousey=pygame.mouse.get_pos()
        self.x=mousex-self.image.get_width()/2
        self.y=mousey-self.image.get_height()/2
        self.active=True
        
        
class Air:
    def __init__(self):
        self.x=225
        self.y=400
        self.image=pygame.image.load('air.png').convert_alpha()

    def Move(self):
        mousex,mousey=pygame.mouse.get_pos()
        self.x=mousex-self.image.get_width()/2
        self.y=mousey-self.image.get_height()/2

    def restart(self):
        self.x=225
        self.y=400
        self.image=pygame.image.load('air.png').convert_alpha()
        


class Enemy:
    def restart(self):
        self.x=random.uniform(30,420)
        self.y=random.uniform(-200,-50)
        
    def __init__(self):
        self.restart()
        self.image=pygame.image.load('enemy.png')
        self.speed=0.08

    def move(self):
        if self.y>608:
            self.speed+=0.01
            self.restart()
            
        else:
            self.y=self.y+self.speed
            
            

pygame.init()
screen=pygame.display.set_mode((450,608))
pygame.display.set_caption('Star War')
background=pygame.image.load('background.png').convert()
interval_b=0
index_b=0
bullets=[]


for i in range(100):
    bullets.append(Bullet())

air=Air()
enemies=[]
for i in range(6):
    enemies.append(Enemy())

def checkHit(enemy, bullet):
    if (bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width())\
    and (bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()):
        enemy.restart()
        bullet.active = False
        return True
    return False

def checkCrash(enemy, air):
    if (enemy.x + enemy.image.get_width() > 1.2*air.x and\
        enemy.x < air.x + 0.6*air.image.get_width())and\
        (enemy.y<air.y+air.image.get_height()and\
         enemy.y+enemy.image.get_height()>air.y):
        return True
    return False





score=0
font=pygame.font.Font(None,32)
gameover=False
start=False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if gameover and event.type==pygame.MOUSEBUTTONUP:
            air.restart()
            for e in enemies:
                e.restart()
            for b in bullets:
                b.restart()
            score=0
            gameover=False
            
        if event.type==pygame.MOUSEBUTTONDOWN:
            start=True
    screen.blit(background,(0,0))
    interval_b-=10
    if interval_b<0:
        bullets[index_b].restart()
        interval_b=100
        index_b=(1+index_b)%100

    if not gameover and start:
        for b in bullets:
            if b.active:
                for e in enemies:
                    if checkHit(e,b):
                        score+=100
                b.move()
                screen.blit(b.image,(b.x,b.y))

        for e in enemies:
            if checkCrash(e,air):
                
                gameover=True
                start=False
            e.move()
            screen.blit(e.image,(e.x,e.y))            
        air.Move()
        screen.blit(air.image,(air.x,air.y))
        text=font.render('Score:%d' % score,1,(0,0,0))
        screen.blit(text,(0,0))
    

    if gameover:
        text=font.render('Score:%d' % score,1,(0,0,0))
        screen.blit(text,(160,150))
    if gameover==False and start==False:
        text=font.render('Click to Start Game!',1,(0,0,0))
        screen.blit(text,(100,150))
     
    pygame.display.update()
    
   
    
                    
    











            
        
