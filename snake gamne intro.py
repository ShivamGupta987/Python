# import pygame,sys
# from pygame.locals import*
# red=[250,0,0]

# # initialize pygame
# pygame.init()
# # set up window
# window=pygame.display.set_mode((1000,600))

# pygame.display.set_caption("sleather eat-the snake game")

# # set up drawing surface
# screen=pygame.display.get_surface()
# screen.fill(red)
# pygame.display.set_caption("snake")
# pygame.display.flip()
# count=0

# while True:
#     print("sleather eat-the snake game!")
#     pass



import pygame,sys
from pygame.locals import*
red=[250,0,0]

# initialize pygame
pygame.init()
# set up window
window=pygame.display.set_mode((1000,600))

pygame.display.set_caption("sleather eat-the snake game")

# set up drawing surface
screen=pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("snake")
pygame.display.flip()


while True:
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.QUIT()
            sys.exit()
        pygame.display.update()            