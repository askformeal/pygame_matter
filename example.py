import sys
import pygame
from pygame_matting import Matter

#since my screen wasn't big enough, I can't display the entire picture

screen  = pygame.display.set_mode((1000,700))
image = pygame.Surface((749,941))
my_mat = Matter('example.bmp',(30,77),(749,941))
image = my_mat.mat()
screen.blit(image,(0,0))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()