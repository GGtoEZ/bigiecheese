import pygame, sys

pygame.init()

funZone = pygame.display.set_mode((400, 400))
posX = 200
posY = 200 

pygame.display.set_caption("Funzone :^)")
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                posX += 10
            elif event.key == pygame.K_a:
                posX -= 10
            



    funZone.fill(black)
    pygame.draw.rect(funZone, red, (posX, posY, 25, 25), 0)
     
    pygame.display.update()
