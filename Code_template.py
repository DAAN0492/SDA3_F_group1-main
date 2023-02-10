# Python code template

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
PIXELS_PER_FRAME = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s),  etc.
ballImage = pygame.image.load("ball.png")

# 5 - Initialize variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect
MAX_HEIGHT = WINDOW_HEIGHT - ballRect
START_HEIGHT = random 
START_WIDTH = random 
WINDOW_WIDTH
WINDOW_HEIGHT
xSpeed = 
ySpeed =

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8 - Do any "per frame" actions
    if WINDOW_WIDTH == MAX_WIDTH
        xSpeed = 0

    # 9 - Clear the window before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the window elements

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
