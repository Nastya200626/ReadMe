from pygame import *
from random import *
from time import time as timer
font.init()
font2=font.SysFont('Arial',36)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(size_x,size_y))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y<300:
            self.rect.y+=self.speed
class Player1(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y<300:
            self.rect.y+=self.speed
window = display.set_mode((700, 500))
display.set_caption('Ping pong') 
background=transform.scale(image.load('Фон игры.jpg'), (700, 500))
player=Player('racket.png',5,30,30,200,4)
player2=Player1('racket.png',660,30,30,200,4 )
ball=GameSprite('tenis_ball.png',300,200,65,65,4)
game=True
clock=time.Clock()
FPS=60
mixer.init()
mixer.music.load('1.mp3')
mixer.music.play()
finish=False
speed_x=3
speed_y=3
lose=font2.render('Игрок 2 проиграл',1,(255,0,0))
lose1=font2.render('Игрок 1 проиграл',1,(255,0,0))
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if finish !=True:
        window.blit(background,(0,0))
        player.update()
        player2.update()
        ball.update()
        player.reset()
        player2.reset()
        ball.reset()
        ball.rect.x +=speed_x
        ball.rect.y +=speed_y
        if ball.rect.y > 450 or ball.rect.y<0:
            speed_y *= -1
        if sprite.collide_rect(player,ball) or sprite.collide_rect(player2,ball):
            speed_x*= -1
        if ball.rect.x > 650:
            finish=True
            window.blit(lose1,(200,200))
        if ball.rect.x<0:
            finish=True
            window.blit(lose1,(200,200))
            
        
    display.update()
    clock.tick(FPS)