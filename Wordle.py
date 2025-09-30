print("Hallo")
print("Hallo, ich bins")
import pygame
import sys
import random
pygame.init()

#Fenster öffnen
Breite, Hoehe = 400, 800
Fenster = pygame.display.set_mode((Breite, Hoehe))
pygame.display.set_caption("Spass mit Worten - Wordle")
clock = pygame.time.Clock()

#Farben definieren
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
yellow = (230, 200, 50)
green = (0, 255, 0)

#Schrift
FONT = pygame.font.SysFont("arial", 30)

#Aufbau des Feldes
Reihen, Spalten = 6, 5
cell_size = 60
Abstand = 10
Tabelle = []
start_x = (Breite - (Spalten * cell_size + (Spalten - 1) * Abstand)) // 2
start_y = 50
for Reihe in range(Reihen):
    Tabelle_Reihe = []
    for Spalte in range(Spalten):
        x = start_x + Spalte * (cell_size + Abstand)
        y = start_y + Reihe * (cell_size + Abstand)
        rect = pygame.Rect(x, y, cell_size, cell_size)
        Tabelle_Reihe.append({"rect": rect, "letter": ""})
    Tabelle.append(Tabelle_Reihe)

#Wörter laden
with open("wortliste.txt", "r", encoding="utf-8") as f:
    alle_woerter = [zeile.strip() for zeile in f]
fuenfer_woerter = [
    wort for wort in alle_woerter
    if len(wort) == 5 and wort[0].isupper()
]
geheimes_wort = random.choice(fuenfer_woerter).upper()


#HIER ZEIGT ER AN, WAS DAS GEHEIME WORT IST!!!!!!!!
print("Zufälliges Wort:", geheimes_wort)



#Spielstatus
akt_Reihe = 0
akt_Spalte = 0


# Wort überprüfen Funktion prüfe_wort
ergebnis = ["gray"] * 5
geheime_buchstaben = list(geheimes_wort)
def pruefe_wort(geratenes_wort, geheimes_wort):
    # Richtige Positionen (grün)
    for i, buchstabe in enumerate(geratenes_wort):
        if buchstabe == geheime_buchstaben[i]:
            ergebnis[i] = "green"
    # Falsche Position, aber vorhanden (gelb)
    if ergebnis[i] != "green":
        for i, buchstabe in enumerate(geratenes_wort):
            if ergebnis[i] == "gray" and buchstabe in geheime_buchstaben:
                ergebnis[i] = "yellow"
    return ergebnis
print(ergebnis)


spielaktiv = True
while spielaktiv:
    Fenster.fill(black)

    # Ereignisse abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if akt_Spalte > 0:
                    akt_Spalte -= 1
                    Tabelle[akt_Reihe][akt_Spalte]["letter"] = ""
            elif event.key == pygame.K_RETURN:
                # ganze Zeile voll
                if akt_Spalte == Spalten:
                    geratenes_Wort = "".join([cell["letter"] for cell in Tabelle[akt_Reihe]])
                    print("Wort eingeben:", geratenes_Wort)
                    #Einfärbung der Buchstaben
                    ergebnis = pruefe_wort(geratenes_Wort, geheimes_wort)    #NEU

                    # Farben in die Kästchen speichern            #NEU
                    for i, farbe in enumerate(ergebnis):          #NEU
                        Tabelle[akt_Reihe][i]["color"] = farbe          #NEU

                print(ergebnis)

                #nächste Zeile freigeben
                if akt_Reihe < Reihen - 1:
                        akt_Reihe += 1
                        akt_Spalte = 0
            elif event.unicode.isalpha() and akt_Spalte < Spalten:
                Tabelle[akt_Reihe][akt_Spalte]["letter"] = event.unicode.upper()
                akt_Spalte += 1


#Kästchen zeichnen
    for Reihe in Tabelle:
        for cell in Reihe:
            farbe = black  # Standardfarbe für leere Felder
            if "color" in cell:
                if cell["color"] == "green":
                    farbe = green
                elif cell["color"] == "yellow":
                    farbe = yellow
                elif cell["color"] == "gray":
                    farbe = gray

            # Rechteck zeichnen
            pygame.draw.rect(Fenster, farbe, cell["rect"])
            pygame.draw.rect(Fenster, white, cell["rect"], 2)  #weißer Rahmen

            if cell["letter"] != "":
                text_surface = FONT.render(cell["letter"], True, white)
                text_rect = text_surface.get_rect(center=cell["rect"].center)
                Fenster.blit(text_surface, text_rect)

    pygame.display.update()
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()