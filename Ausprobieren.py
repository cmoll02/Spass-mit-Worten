import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Spass mit Worten")
clock = pygame.time.Clock()
text_font = pygame.font.Font(None,30)

gut = pygame.Surface((800,300))
gut.fill("blue")
böse = pygame.Surface((800,100))
böse.fill("red")
enemy = pygame.Surface((50,50))
enemy.fill("green")
enemy_x_pos = 770
iche_surface = pygame.Surface((50,50))
iche_surface.fill("violet")
iche_rect = iche_surface.get_rect(midleft=(50,250))
#pygame.image.load(Pfadhiereinfügen) um Bilder zu importieren...erstellt neuen surface


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(gut,(0,0))
    screen.blit(böse,(0,300))
    screen.blit(iche_surface,iche_rect)
    print(iche_rect.left)
    enemy_x_pos -= 5
    screen.blit(enemy,(enemy_x_pos, 250))
    if enemy_x_pos <= -50:
        enemy_x_pos = 850
        enemy.fill("orange")
    pygame.display.update()
    clock.tick(60)