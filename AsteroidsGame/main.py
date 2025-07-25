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

    keys = pygame.key.get_pressed()
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
    running = True
    game_over = False

    def reset():
        for asteroid in asteroids:
            asteroid.kill()
        for bullet in bullets:
            bullet.kill()


        player.position = (SCREEN_WIDTH / 2 - 5, SCREEN_HEIGHT / 2)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            # First, check IF a key was pressed
            if event.type == pygame.KEYDOWN:
                # Now we can safely check WHICH key it was.
                # Only allow reset if the game is actually over.
                if event.key == pygame.K_r:
                    reset()  # Call your reset function
                    game_over = False  # Turn the game back on!
                    score = 0

        text = font.render(str(score), True, white, (0,0,0,255))



        if not game_over:
            updatable.update(dt)
            for asteroid in asteroids:
                for bullet in bullets:
                    if asteroid.collision(bullet):
                        Boom(asteroid.position.x, asteroid.position.y, asteroid.radius)
                        asteroid.split()
                        bullet.kill()
                        score += 1
                if asteroid.collision(player):
                        game_over = font.render("Restart?, press R if yes", True, white, (0,0,0,255))
                        screen.blit(game_over, textRect)

                        game_over = True




            screen.fill("black")
            for thing in drawable:
                thing.draw(screen)
            screen.blit(text, textRect)
            #add framerate

            dt = time.tick(60) / 1000
        else:
            # --- Game is over ---
            screen.fill((0, 0, 0)) # Black background

            # Render and display "Game Over" text
            game_over_font = pygame.font.Font(None, 74)
            game_over_text = game_over_font.render("Game Over", True, white)
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
            screen.blit(game_over_text, game_over_rect)

            # Render and display "Press R to Restart" text
            restart_font = pygame.font.Font(None, 50)
            restart_text = restart_font.render("Press R to Restart", True, white)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            screen.blit(restart_text, restart_rect)

            restart_font = pygame.font.Font(None, 50)
            restart_text = restart_font.render("Score: "+str(score), True, white)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
            screen.blit(restart_text, restart_rect)
        pygame.display.flip()
if __name__ == "__main__":
    main()
