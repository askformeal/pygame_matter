import pygame
#this a function used to cop image in pygame

class Matter:
    def __init__(self,my_sprite='',top_left=(),size=()):
        self.top_left = top_left
        self.size = size
        self.sprite = my_sprite
        
    def mat(self):
        sprite = pygame.image.load(self.sprite)
        surface = pygame.Surface(self.size)
        temp_tuple = (self.top_left[0],self.top_left[1],self.size[0],self.size[1])
        surface.blit(sprite,(0,0),temp_tuple)
        return surface