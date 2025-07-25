import pygame
from constants import *
from circleshape import CircleShape
from bullets import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cool_down = 0
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
       self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        self.cool_down -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt
        self.position += unit_vector

    def shoot(self):
        if not self.cool_down > 0:
            shot = Shot(self.position.x,self.position.y)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            self.cool_down = PLAYER_SHOT_COOLDOWN
