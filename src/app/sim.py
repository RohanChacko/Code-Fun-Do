# import pygame
# from person import Person
# import random

# people_array = []
# map_height = None
# map_width = None



        
# def main():
#     while(True):




                    

#!/usr/bin/env python2

import pygame
import random
import time
from person import Person

people_array = []
connection = []


WIDTH = 860
HEIGHT = 880
FPS = 10

def init():
    k = 1
    for i in range(50):
        people_array.append(Person(HEIGHT, WIDTH))
        print(i)
    for person in people_array:
        person.id = k
        k= k+1

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("App")
clock = pygame.time.Clock()     ## For syncing the FPS


## group all the sprites together for ease of update
# all_sprites = pygame.sprite.group()

## Game loop
running = True
init()
while running:

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False


    #2 Update
    # all_sprites.update()
    # for person in people_array:
    #     person.move()
    #     for other_person in people_array:
    #         if other_person == person:
    #             pass
    #         else:
    #             if person.detect_signal(other_person):
    #                 pygame.draw.line(screen, GREEN, (person.x_coordinate,person.y_coordinate), (other_person.x_coordinate,other_person.y_coordinate), 1)
                    
                    # pass
                    # person.displacement_x = 0
                    # person.displacement_y = 0
                    # other_person.displacement_x = 0
                    # other_person.displacement_y = 0
                    # connection.append([person.x_coordinate,person.y_coordinate,other_person.x_coordinate,other_person.y_coordinate])



    #3 Draw/render
    screen.fill(BLACK)

    
    for person in people_array:
        person.move()
        if random.randint(0, 500) == 50:
            person.cell_connectivity = True
        
        if random.randint(0, 500) == 50:
            person.ismessage = True
            person.message = "Message from person " + str(person.id) + ": " + str(person.x_coordinate) + "," + str(person.displacement_y)
            person.send_message()
            print(person.message)
        for other_person in people_array:
            if other_person == person:
                pass
            else:
                if person.detect_signal(other_person):
                    pygame.draw.line(screen, GREEN, (person.x_coordinate,person.y_coordinate), (other_person.x_coordinate,other_person.y_coordinate), 1)
        person.connect_server()
        if random.randint(0, 100) == 50:
            person.cell_connectivity = False
    # all_sprites.draw(screen)
    ########################
    for person in people_array:
        pygame.draw.circle(screen, RED, (person.x_coordinate,person.y_coordinate), 3)

    # for connect in connection:
    #     pygame.draw.line(screen, GREEN, (connect[0],connect[1]), (connect[2], connect[3]), 1)

    ### Your code comes here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()