import pygame
import time

# Set window
x = 960
y = 540
black = (0,0,0)
white = (255,255,255)
bluecolor = (0,0,255)
score = 0
Title = "The Hopping Dinosaur"
display = pygame.display.set_mode((x,y))
pygame.display.set_caption(Title)
speed = .02


"""
Character Creation
"""
ground=350


body = pygame.Surface((40, 40))                        # Size 
body.fill(white)                                       # Color

head = pygame.Surface((25, 15))                        # Size
head.fill(white)                                       # Color

leg = pygame.Surface((3, 10))                         # Size
leg.fill(white)                                       # Color





def update():
    display.fill(black)
    # Body
    player_body = body.get_rect(topleft=(55, ground))
    display.blit(body, player_body)
    # Head
    player_head = head.get_rect(topleft=(80, ground-10))
    display.blit(head, player_head)
    # Leg 1
    player_leg1 = leg.get_rect(topleft=(65, ground+40))
    display.blit(leg, player_leg1)
    # Leg 2
    player_leg2 = leg.get_rect(topleft=(75, ground+40))
    display.blit(leg, player_leg2)

    pygame.display.update()


    
def move():

    # Move up
    global ground
    global player_rect
    for i in range (0,10):
        ground = ground-10
        update()
        print('-10')
        time.sleep(speed)

    # Then move down
    for i in range (0,10):
        ground = ground+10
        update()
        print('+10')
        time.sleep(speed)




launch = True
while launch:
    update()


    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:                
                print("Up")
                move()
                #speed = abs((speed*.001)/.002)



            if event.key == pygame.K_LEFT: 
                print("LEFT  Registered") 
                pygame.quit()
                quit()





     

