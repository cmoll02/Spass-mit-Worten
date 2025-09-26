import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Spass mit Worten")
clock = pygame.time.Clock()
text_font = pygame.font.Font(None,30)

gut = pygame.Surface((800,50))
gut.fill("blue")
böse = pygame.Surface((800,50))
böse.fill("red")
enemy = pygame.Surface((50,50))
enemy.fill("green")
enemy_x_pos = 700
#pygame.image.load(Pfadhiereinfügen) um Bilder zu importieren...erstellt neuen surface


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(gut,(0,0))
    screen.blit(böse,(0,100))
    enemy_x_pos -= 5
    screen.blit(enemy,(enemy_x_pos, 50))
    pygame.display.update()
    clock.tick(60)