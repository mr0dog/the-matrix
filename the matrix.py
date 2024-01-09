
Conversation opened. 1 unread message.

Skip to content
Using Denver Public Schools Mail with screen readers
2 of 175
(no subject)
Inbox

Michael Chavez-Hernandez
9:37 AM (1 hour ago)
to me

import pygame
import random
pygame.init()  
pygame.display.set_caption("snowfall")  # sets the window title
screen = pygame.display.set_mode((500, 500))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock


#set up empty lists to hold x and y positions of flakes
xPositions = []
yPositions = []

#use a for loop to push random values into the x and y position lists
for i in range(50):
    xPositions.append(random.randrange(0, 500))
    yPositions.append(random.randrange(0, 500))



while(1): #omg game lup---------
    clock.tick(60) #FPS
   
    #physics section----
   
    #move flakes
    for i in range(50):
       yPositions[i]-=5 #move down
         
       #respawn  
       if yPositions[i]<0: #reset position if you go off the screen
           yPositions[i]=random.randrange(500, 1000)
                     

    #render section---
    #screen.fill((0,0,0))
   
    for i in range(50):
        pygame.draw.circle(screen, (0, random.randrange(0, 255), 0), (xPositions[i], yPositions[i]), random.randrange(0, 5)) #draw flakes
        pygame.draw.circle(screen, (0, 0, 0), (xPositions[i], yPositions[i]), random.randrange(0, 5)) #draw flakes
   
    pygame.display.flip()#this actually puts the pixel on the screen
   
pygame.quit()

