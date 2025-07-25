from posix import wait
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullets import Shot
from explosion import Boom
import pygame.freetype

def main():
    pygame.init()

    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    score = 0
    time = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    font = pygame.font.Font('PressStart2P-vaV7.ttf', 32)
    text = font.render(str(score), True, white, (0,0,0,255))
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH// 2, 100)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    explosions = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2 - 5, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    asteroids = pygame.sprite.Group()
    Boom.containers = (drawable, updatable, explosions)
    Shot.containers = (bullets, updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    asteroids_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        text = font.render(str(score), True, white, (0,0,0,255))
        updatable.update(dt)



        for asteroid in asteroids:
            for bullet in bullets:
                if asteroid.collision(bullet):
                    Boom(asteroid.position.x, asteroid.position.y, asteroid.radius)
                    asteroid.split()
                    bullet.kill()
                    score += 1
            if asteroid.collision(player):
                print("Game over!")
                pygame.quit()
                return


        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        screen.blit(text, textRect)
        #add framerate
        pygame.display.flip()
        dt = time.tick(60) / 1000


if __name__ == "__main__":
    main()
