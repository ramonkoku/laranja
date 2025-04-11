import pygame
from config import PLAYER_SPEED

class Player:
    def __init__(self):
        self.image = pygame.Surface((40, 60))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect(center=(200, 200))
        self.attacking = False
        self.attack_rect = pygame.Rect(0, 0, 50, 50)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_s]: self.rect.y += PLAYER_SPEED
        if keys[pygame.K_a]: self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_d]: self.rect.x += PLAYER_SPEED
        
        if self.attacking:
            self.attacking = False  # O ataque dura só um frame

    def attack(self):
        self.attacking = True
        self.attack_rect.center = (self.rect.centerx + 40, self.rect.centery)  # Ataque à frente
