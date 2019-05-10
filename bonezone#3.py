import pygame, sys, random
pygame.init()

funzone = pygame.display.set_mode((500, 500))

### Crab
width = 25
height = 25
pX =250
pY = 250

vel = 10

Swidth = 20
Sheight = 20
pygame.display
moveup = False
movedown = False
moveleft = False
moveright = False

### food!!!! ####

foodX = random.randrange(500)
foodY = random.randrange(500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moveup = True
                movedown = False
                moveleft = False
                moveright = False
            if event.key == pygame.K_s:
                moveup = False
                movedown = True
                moveleft = False
                moveright = False
            if event.key == pygame.K_d:
                moveup = False
                movedown = False
                moveleft = True
                moveright = False
            if event.key == pygame.K_a:
                moveup = False
                movedown = False
                moveleft = False
                moveright = True
                
    keys=pygame.key.get_pressed()
    if moveup and pY > 0:
        pY -= 5
    if movedown and pY < 500-25:
        pY += 5
    if moveright and pX > 0:
        pX -= 5
    if moveleft and pX < 500-25:
        pX += 5

              ### collision ###
    if any(pX <= X <= (pX + width) for X in range (foodX, foodX + Swidth)) and any(pY <= y <= (pY + height) for y in range (foodY, foodY + Sheight)): 
        foodX = random.randrange(500)
        foodY = random.randrange(500)
        
            
    funzone.fill((0,0,0))
    myblock = pygame.draw.rect(funzone, (255,200,175), (foodX, foodY, 20,20))
    pygame.draw.rect(funzone, (255, 0, 0), (pX, pY, width, height))
    pygame.draw.rect(funzone, (255,255,255), (pX, pY, Swidth, Sheight))
    pygame.draw.rect(funzone, (255,255,255), (pX+25,pY, Swidth, Sheight))

  
        
    
    ### moving keys
        
                
        
    pygame.display.update()
