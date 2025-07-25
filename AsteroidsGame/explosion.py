import pygame
from circleshape import *

class Boom(CircleShape):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.explosion_time = 0.2
        self.vectors_start = pygame.Vector2(0,size * 0.75)
        self.vectors_end = pygame.Vector2(0,size+5)

    def update(self, dt):
        self.explosion_time -= dt
        if self.explosion_time < 0:
            self.kill()




    def draw(self, screen):
        pygame.draw.line(screen, "white", self.position + self.vectors_start,self.position + self.vectors_end , 2)
        pygame.draw.line(screen, "white", self.position + self.vectors_start.rotate(45), self.position + self.vectors_end.rotate(45) , 2)
        pygame.draw.line(screen, "white", self.position + self.vectors_start.rotate(90), self.position + self.vectors_end.rotate(90) , 2)
        pygame.draw.line(screen, "white", self.position + self.vectors_start.rotate(135), self.position + self.vectors_end.rotate(135) , 2)
        pygame.draw.line(screen, "white", self.position + self.vectors_start.rotate(180), self.position + self.vectors_end.rotate(180) , 2)
        pygame.draw.line(screen, "white", self.position + self.vectors_start.rotate(-45), self.position + self.vectors_end.rotate(-45) , 2)
        pygame.draw.line(screen, "white", self.position + self.vectors_start.rotate(-90), self.position + self.vectors_end.rotate(-90) , 2)
        pygame.draw.line(screen, "white", self.position + self.vectors_start.rotate(-135), self.position + self.vectors_end.rotate(-135) , 2)
