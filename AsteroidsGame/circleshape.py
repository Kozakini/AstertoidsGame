import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self,x, y, radius):
        if hasattr(self, "containners"):
            super().__init__(self.containners)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass
    def update(self, dt):
        pass


