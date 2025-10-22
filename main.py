import pygame, sys
from pygame.locals import QUIT
import random

pygame.init()
WIDTH = 700
HEIGHT = 500
FPS = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT,))
pygame.display.set_caption('Hangman')
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0, 255,0)
PINK = (255,153,255)
PURPLE = (204,153,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
SCREEN.fill(PINK)

#Define Points for Polygon
points = [(495,220), (500,230), (520,260)]
points2 = [(495,220), (490,230), (470,260)]

#Define Radius of Cirlces
bRadius = 18
wRadius = 15

font = pygame.font.Font(None, 74)

def drawbubble(x,y):
   pygame.draw.circle(SCREEN, BLACK, (x, y), bRadius) #CircleA Black
   pygame.draw.circle(SCREEN,WHITE, (x, y), wRadius) #CircleA Black

while True:
   pygame.draw.rect(SCREEN, BLACK, (450, 325, 200,10) ) #Bottom Platform
   pygame.draw.rect(SCREEN, BLACK, (580, 75, 10, 250 )) #Tall Vertical Stick
   pygame.draw.rect(SCREEN, BLACK, (490, 70, 100, 10)) #Short Horizontal
   pygame.draw.rect(SCREEN, BLACK, (490,80, 10, 50)) #Short Vertical Stick
   pygame.draw.circle(SCREEN, WHITE, (495,145), 15) #Head
   pygame.draw.rect(SCREEN, WHITE, (490,160, 10, 60)) #Body
   pygame.draw.rect(SCREEN, WHITE, (450, 170, 40, 10)) #LeftArm
   pygame.draw.rect(SCREEN, WHITE, (500,170, 40, 10)) #RightArm
   pygame.draw.polygon(SCREEN, WHITE, points, 10) #RightLeg
   pygame.draw.polygon(SCREEN, WHITE, points2, 10) #LeftLeg

   
  #Letter Lines 
   pygame.draw.rect(SCREEN, WHITE, (20, 100, 40, 10)) #Far Left Letter Line
   pygame.draw.rect(SCREEN, WHITE, (70, 100, 40, 10)) #2nd Far Left Letter Line
   pygame.draw.rect(SCREEN, WHITE, (120, 100, 40, 10)) #Middle Letter Line
   pygame.draw.rect(SCREEN, WHITE, (170, 100, 40, 10)) #2nd Far Right Letter Line
   pygame.draw.rect(SCREEN, WHITE, (220, 100, 40, 10)) #FAR Right Letter Line

  #ROW1
   drawbubble(50, 380)
   drawbubble(100, 380)
   drawbubble(150,380)
   drawbubble(200,380)
   drawbubble(250,380)
   drawbubble(300,380)
   drawbubble(350,380)
   drawbubble(400,380)
   drawbubble(450,380)
   drawbubble(500,380)
   drawbubble(550,380)
   drawbubble(600,380)
   drawbubble(650,380)

  #ROW2
   drawbubble(50,430)
   drawbubble(100,430)
   drawbubble(150,430)
   drawbubble(200,430)
   drawbubble(250,430)
   drawbubble(300,430)
   drawbubble(350,430)
   drawbubble(400,430)
   drawbubble(450,430)
   drawbubble(500,430)
   drawbubble(550,430)
   drawbubble(600,430)
   drawbubble(650,430)

   keys = pygame.key.get_pressed()
   
   for i in range(pygame.K_a, pygame.K_z + 1):
      if keys[i]:
         letters = chr(i)
         text_surface = font.render(letters, True, WHITE)
         SCREEN.blit(text_surface, (30, 60))
         SCREEN.blit(text_surface, (80,60))
         SCREEN.blit(text_surface, (130, 60))
         SCREEN.blit(text_surface, (180,60))
         SCREEN.blit(text_surface, (230,60))

   # keys = pygame.key.get_pressed()
   # if keys[pygame.K_a]:
      
   #Text

   for i in range(13):
      font = pygame.font.Font(None, 40)
      letter = chr(65+i)
      text_surface = font.render(letter, True, (0, 0, 0))  
      SCREEN.blit(text_surface, (50*i+40,370))
      print(letter)

   for i in range(13):
      font = pygame.font.Font(None, 40)
      letter1 = chr(78+i)
      text_surface = font.render(letter1, True, (0, 0, 0))  
      SCREEN.blit(text_surface, (50*i+40,420))
      print(letter1)



   # font = pygame.font.Font(None, 45)j
   # text = font.render("A", True, BLACK)
   # textRect = text.get_rect()
   # textRect.center = (50,380)
   # SCREEN.blit(text,textRect)

   for event in pygame.event.get():
           if event.type == QUIT:
               pygame.quit()
               sys.exit()
   pygame.display.update()