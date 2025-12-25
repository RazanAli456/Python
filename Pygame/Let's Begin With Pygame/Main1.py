import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("My Pygame Window")
image=pygame.image.load("PenguinBackground.png")
BackgroundImage=pygame.transform.scale(image,(500,500))
p_image=pygame.image.load("Penguin.png")
penguin_image=pygame.transform.scale(p_image,(500,500))
penguin_rect=penguin_image.get_rect(
    center=(500 // 2, 400 // 2 - 30)
)
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
            pygame.quit()
        screen.blit(BackgroundImage,(0,0))
        screen.blit(penguin_image,penguin_rect)
        pygame.display.flip()