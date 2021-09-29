import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=400
height=600
screen = pygame.display.set_mode((width,height))
  
building = pygame.Rect(5,200,30,400)


def draw_building():
    global height
    # Drawing the 'building' rect on the screen
    pygame.draw.rect(screen,[255,255,255],building)
    
    # Incrementing x-coordinate of 'building' by 40
    building.x=building.x+40
    
    # Assigning a random value in the range of 100 to 500 for 'building.height'
    building.height=random.randint(100, 500)
    building.y=height-building.height

    
while True:    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Calling the function defined to draw the building
                draw_building()
            
  
   
    pygame.display.update()
    clock.tick(30)
