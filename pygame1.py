import pygame

from sys import exit #for terminating the while loop

#Score function
def display_score():
    current_time=pygame.time.get_ticks()//1000-start_time
    score_text=text.render(str(current_time),True,'Black')
    score_rect=score_text.get_rect(center=(400,120))
    screen.blit(score_text,score_rect)


start_time=0
#Initialize elements
pygame.init()

#Screen
screen=pygame.display.set_mode((800,460))

#Title
title=pygame.display.set_caption('Game')

#Clock for managing frame rates
clock=pygame.time.Clock()


#creating text elements
text=pygame.font.Font(None,50)

#Importing images
#Put images on test surfaces
sky=pygame.image.load(r'F:\Games\pygame\assets\graphics\Sky.png').convert()
ground=pygame.image.load(r'F:\Games\pygame\assets\graphics\ground.png').convert()
snail=pygame.image.load(r'F:\Games\pygame\assets\graphics\snail\snail1.png').convert_alpha()
player1=pygame.image.load(r'F:\Games\pygame\assets\graphics\Player\player_walk_1.png').convert_alpha()

#Position
sky_x=sky_y=ground_x=collision=0
ground_y=300
player1_x,player1_y=80,300
snail_x,snail_y=800,300

# player rectangle
player1_rect=player1.get_rect(midbottom=(player1_x,player1_y))
player1_gravity=0 
#Snail rectangle
snail_rect=snail.get_rect(bottomright=(snail_x,snail_y))


#text on surface
text_surface=text.render('Pygame',True,'Black')
#Score
score=text.render('Score',True,'Black')




#Rectangle
text_rect=text_surface.get_rect(center=(400,50))
score_rect=score.get_rect(center=(400,90))


game_active=True

#Game Loop
while True:

    

    for event in pygame.event.get():#Get all the events of pygame in event
        #Closing window
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:

            #Collision using rectangles
            if event.type==pygame.MOUSEBUTTONDOWN :
                            if player1_rect.collidepoint(event.pos) and  player1_rect.bottom>=300:
                                player1_gravity=-8
                            
            #KeyBoard Inputs
            if event.type == pygame.KEYDOWN :#siMILARLY pygame.KEYUP
                        if event.key==pygame.K_SPACE and player1_rect.bottom>=300:
                            player1_gravity=-5
                        if event.key==pygame.K_d :
                            player1_rect.x+=20
                        if event.key==pygame.K_a :
                            player1_rect.x-=20
        else:
              
              if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE:
                  game_active=True
                  snail_rect.left=800
                  start_time=pygame.time.get_ticks()//1000
                     
    if game_active:
        #Draw surfaces to main surface
        screen.blit(sky,(sky_x,sky_y))
        screen.blit(ground,(ground_x,ground_y))

        #Title

        pygame.draw.rect(screen,'Blue',text_rect)

        screen.blit(text_surface,text_rect)

        

        #Score_surface
        pygame.draw.rect(screen,'Pink',score_rect,2,10)
        pygame.draw.rect(screen,'Pink',score_rect)
       
        screen.blit(score,score_rect)

        #Snail
        screen.blit(snail,snail_rect)
        
        #Player
        player1_gravity+=0.1
        player1_rect.y+=player1_gravity
        if player1_rect.bottom>=300:player1_rect.bottom=300
        screen.blit(player1,player1_rect)

        #Updation and Reappear
        snail_rect.x-=4
        if snail_rect.right<0:
            snail_rect.left=800
            collision+=1
     #Collision
        if snail_rect.colliderect(player1_rect):
            game_active=False
            
        display_score() 
     #   '''player1_rect.x+=2
      #  if player1_rect.left>800:
       #     player1_rect.right=30'''

        #Collision using rectangles
          #'''mouse_pos=pygame.mouse.get_pos()
           #if player1_rect.collidepoint(mouse_pos): print(pygame.mouse.get_pressed())
          #if player1_rect.colliderect(snail_rect):'''

        #KEYBOARD INPUT
       #''' keys=pygame.key.get_pressed()
       # if keys[pygame.K_SPACE]:
          #  print('Jump')'''

        #Update window after adding functions
        pygame.display.update()
        #Controling frame rate
        clock.tick(100)#game doesn't exceeds 100 frames per second
