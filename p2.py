import pygame
pygame.init()
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 300
display = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption('Dragon Game')
dragon_left_image = pygame.image.load("dragon-icon.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_image.topleft = (0,0)

running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.blit(dragon_left_image, dragon_left_rect)
    pygame.display.update()

pygame.quit()
