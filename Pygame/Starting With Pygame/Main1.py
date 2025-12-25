import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
pygame.display.set_caption("Learning How To Add Background")
image=pygame.transform.scale(pygame.image.load("Yeahhhhhh.jpg").convert(),(400,300))
done=False

while not done:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            done=True
            pygame.quit()
            screen.blit(image,(0,0))
pygame.display.flip()