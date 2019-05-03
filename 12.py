import pygame, sys, random
pygame.init()

funzone = pygame.display.set_mode((500, 500))

### Crab
width = 50
height = 50
pX =250
pY = 250

vel = 10

Swidth = 20
Sheight = 20
pygame.display

foodX = random.randrange(500)
foodY = random.randrange(500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys=pygame.key.get_pressed()
    funzone.fill((0,0,0))
    myblock = pygame.draw.rect(funzone, (255,200,175), (foodX, foodY, 20,20))
    pygame.draw.rect(funzone, (255, 0, 0), (pX, pY, width, height))
    pygame.draw.rect(funzone, (255,255,255), (pX, pY, smallwidth, smallheight))
    pygame.draw.rect(funzone, (255,255,255), (pX+25,pY, Swidth, Sheight))

    ### collision
  
    
    ### moving keys
    if keys[pygame.K_a]:
        if pX > 0:
            pX-=vel
    elif keys[pygame.K_d]:
        if pX < 450:
            pX+=vel
    if keys[pygame.K_w]:
        if pY > 0:
            pY-=vel
    elif keys[pygame.K_s]:
        if pY < 450:
            pY+=vel
    
    pygame.display.update()
