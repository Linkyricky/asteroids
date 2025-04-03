from circleshape import *
from constants import *
import pygame
from Shot import *  # Import the Shot class

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.movement_direction = 0  # 1 for forward, -1 for backward, 0 for no movement
        self.shoot_cooldown = 0  # Timer to manage rate of shooting (in milliseconds)

    def triangle(self):
        """Create the triangular shape representing the player."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Direction the player is facing
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]  # Vertices of the triangle
    
    def draw(self, screen):
        """Draw the player's shape on the screen."""
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, direction, dt):
        """Rotate the player left or right."""
        self.rotation += PLAYER_TURN_SPEED * direction * dt  # Positive direction is right, negative is left
    
    def move(self, dt):
        """Move the player forward or backward based on its facing direction."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Facing direction
        self.position += forward * PLAYER_SPEED * dt * self.movement_direction

    def shoot(self, shots_group):
        """
        Create and add a shot to the shots_group.

        Args:
            shots_group (pygame.sprite.Group): The group to which the new shot should be added.
        """
        # Check if the cooldown timer allows shooting
        if self.shoot_cooldown <= 0:
            new_shot = Shot(self.position, PLAYER_SHOOT_RADIUS, self.rotation, PLAYER_SHOOT_SPEED)
            shots_group.add(new_shot)

    def update(self, dt, shots_group):

        keys = pygame.key.get_pressed()  # Get pressed keys

        # Handle rotation
        if keys[pygame.K_a]:  # Rotate left
            self.rotate(-1, dt)
        if keys[pygame.K_d]:  # Rotate right
            self.rotate(1, dt)

        # Handle movement
        if keys[pygame.K_w]:  # Move forward
            self.movement_direction = 1
            self.move(dt)
        elif keys[pygame.K_s]:  # Move backward
            self.movement_direction = -1
            self.move(dt)
        else:
            self.movement_direction = 0

        # Decrease the cooldown timer
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt * 1000  # Decrease cooldown each frame (dt in seconds)

        # Handle shooting
        if keys[pygame.K_SPACE] and self.shoot_cooldown <= 0:  # Fire only if cooldown is 0
            self.shoot(shots_group)  # Call the shoot method
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN