from circleshape import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, surface):
        # Override the draw method to draw a circle
        # The position comes from self.position, radius from self.radius
        # And we need to use a width of 2 as specified
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, 2)
    def update(self, dt):
        self.position += (self.velocity * dt) 