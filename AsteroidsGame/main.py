import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullets import Shot

def main():
    pygame.init()

    time = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    asteroids = pygame.sprite.Group()

    Shot.containers = (bullets, updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    asteroids_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            for bullet in bullets:
                if asteroid.collision(bullet):
                    asteroid.split()
            if asteroid.collision(player):
                print("Game over!")
                pygame.quit()
                return

        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)

        #add framerate
        pygame.display.flip()
        dt = time.tick(60) / 1000


if __name__ == "__main__":
    main()
