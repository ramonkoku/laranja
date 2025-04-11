import pygame
from player import Player
from config import WIDTH, HEIGHT, MAP_FILE
from pytmx.util_pygame import load_pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = Player()
    
    # Carregar mapa
    tmx_data = load_pygame(MAP_FILE)
    
    running = True
    while running:
        screen.fill((30, 30, 30))  # Fundo escuro
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.attack()
        
        # Desenhar o mapa
        for layer in tmx_data.visible_layers:
            if hasattr(layer, "data"):
                for x, y, gid in layer:  
                    tile = tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        screen.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))
        
        player.update()
        screen.blit(player.image, player.rect)
        
        # Desenhar ataque se estiver ativo
        if player.attacking:
            pygame.draw.rect(screen, (255, 0, 0), player.attack_rect, 2)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
