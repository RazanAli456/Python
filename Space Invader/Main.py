#Razan Ali
import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
background = pygame.image.load('bg (1).png')
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
playerImg = pygame.image.load('player.png')
PLAYER_START_X = 370
PLAYER_START_Y = 380
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0
playerX_change=0
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            Done=True
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              playerX_change = -5
          if event.key == pygame.K_RIGHT:
              playerX_change = 5
    playerX += playerX_change
    playerX = max(0, min(playerX, 500 - 64))  # 64 is the size of the player

    screen.blit(background,(0,0))
    screen.blit(playerImg,(playerX,380))

    pygame.display.update()