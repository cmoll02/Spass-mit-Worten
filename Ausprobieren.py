import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Spass mit Worten")
clock = pygame.time.Clock()

text_font = pygame.font.Font(None,30)
score_surf = text_font.render("Score",False, "Black")
score_rect = score_surf.get_rect(center=(400,50))


gut = pygame.Surface((800,300))
gut.fill("blue")
böse = pygame.Surface((800,100))
böse.fill("red")
enemy = pygame.Surface((50,50))
enemy.fill("green")
enemy_rect = enemy.get_rect(bottomleft=(750,300))
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
    screen.blit(score_surf,score_rect)
    screen.blit(enemy,enemy_rect)
    #print(iche_rect.left)
    enemy_rect.left -= 5
    screen.blit(iche_surface,iche_rect)
    if enemy_rect.right <= 0:
        enemy_rect.left = 800
    pygame.display.update()
    clock.tick(60)