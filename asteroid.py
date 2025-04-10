import pygame
from circleshape import CircleShape
import random 
from constants import ASTEROID_MIN_RADIUS

class Asteroid(pygame.sprite.Sprite):
    containers = None  # This will be set from the main game file
    
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self, self.containers)  # Initialize with containers
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)


    def split(self):
        # Kill the current asteroid
        self.kill()

        # If the asteroid is large enough, spawn smaller ones
        if self.radius > ASTEROID_MIN_RADIUS:
            # Calculate the new radius for the smaller asteroids
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # Generate a random angle between 20 and 50 degrees
            random_angle = random.uniform(20, 50)

            # Create two new velocity vectors rotated by ±random_angle
            velocity1 = pygame.Vector2(self.velocity).rotate(random_angle) * 1.2
            velocity2 = pygame.Vector2(self.velocity).rotate(-random_angle) * 1.2

            # Create two new smaller asteroids
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = velocity1

            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = velocity2

            # Add the new asteroids to the same group as the current asteroid
            for group in self.groups():
                group.add(asteroid1, asteroid2)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def collides_with(self, other):
        # Calculate distance between centers
        distance = (self.position - other.position).length()
        # Check if the distance is less than the sum of radii
        return distance < (self.radius + other.radius)