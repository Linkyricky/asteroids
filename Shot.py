from circleshape import *
import pygame
from player import *  # Add this import

class Shot(CircleShape):
    def __init__(self, x, y, radius, player_angle, PLAYER_SHOOT_SPEED):
        super().__init__(x, y, radius)
    
    # Set velocity based on player's angle and speed
        direction = pygame.Vector2(0, -1)  # Default direction (upwards)
        direction = direction.rotate(player_angle)  # Rotate based on player's facing angle
        self.velocity = direction * PLAYER_SHOOT_SPEED
    
    def draw(self, surface):
        # Override the draw method to draw a circle
        # The position comes from self.position, radius from self.radius
        # And we need to use a width of 2 as specified
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, 2)
    def update(self, dt):
    # Move the bullet
        self.position += (self.velocity * dt)
    
    # Screen boundary checks
        screen_width, screen_height = 800, 600  # Replace with actual screen size
        if (self.position.x < 0 or self.position.x > screen_width or
            self.position.y < 0 or self.position.y > screen_height):
            self.kill()  # Remove bullet from all sprite groups

    