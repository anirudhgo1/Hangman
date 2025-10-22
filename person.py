import pygame, sys
from main import RED, SCREEN

pygame.init()


class Person:

  def __init__(self):
    super().__init__()
    self.row = 0
    self.col = 0

  def drawhead(self):
    player = Person()


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      sys.exit()
