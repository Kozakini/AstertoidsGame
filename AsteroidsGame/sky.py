import pygame
from circleshape import CircleShape
from constants import *
import random

class Star(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,2)

    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
