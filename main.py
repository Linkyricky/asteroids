# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
import pygame
from player import Player  # Add this import
from asteroid import Asteroid  # Add this import
from asteroidfield import AsteroidField  # Add this import
import sys
from Shot import *  # Import the Shot class


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    # Set containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    
    # Create player instance
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    
    # Delta time variable
    dt = 0

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        
        # Update all updatable objects
        updatable.update(dt)
        shots_group.update(dt) 
        # Draw all drawable objects
        for entity in drawable:
            entity.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        # Check for collisions
        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game over!")
                pygame.quit()  # Properly quit pygame
                sys.exit()

if __name__ == "__main__":
    main()