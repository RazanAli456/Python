import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
pygame.display.set_caption("My Second Pygame Window")
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
            pygame.quit()
pygame.display.filp()