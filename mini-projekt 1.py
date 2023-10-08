# Importerer pygame modul
import pygame
import math
from datetime import datetime

# Initierer Pygame
pygame.init()

# Laver display surface med en skærmstørrelse på 600x600 pixels
screen = pygame.display.set_mode((600, 600))

# Laver en funktion, som tegner timemarkeringerne på uret
def draw_markings():
    for number in range(1, 13): # Her tegnes der 12 streger og ikke 13, da range er et zero-based index
        angle_degree = number * 30 # Hver markering er adskilt af 30 grader
        start_x, start_y = degrees(190, angle_degree) # Her findes startkoordinaterne for markeringen, som er 190
        end_x, end_y = degrees(165, angle_degree) # Her findes slutkoordianterne for markeringen, som er 165
        pygame.draw.line(screen, (0, 0, 0), (start_x, start_y), (end_x, end_y), 2) # Markeringerne tegnes

# Laver en funktion, der beregner graderne 
def degrees(R, theta): # Funktionen tager to argumenter: R (radius) og theta (vinklen)
    y = math.cos(2*math.pi*theta/360)*R # Beregner cosinus til vinklen theta i grader
    x = math.sin(2*math.pi*theta/360)*R # Beregner sinus til vinklen theta i grader
    return x+300, -(y-300) #Returnerer er en positiv værdi langs x-aksen og negativ værdi ned ad y-aksen i cirklens midte

current_time = datetime.now #Henter den aktuelle tid ved programmets start

# Laver et while-loop, så programmet kører konstant, medmindre det afbrydes af brugeren
while True:
    # Fylder skærmen med farven hvid
    screen.fill((255, 255, 255))

    # Følgende kode tegner en cirkel ved hjælp af pygame
    # Farvekoden resulterer i en lyserød cirkel
    # Paramteret [300, 300] tegner cirklen centreret på skærmen i forhold til skærmens størrelse på 600 pixels
    # 200 er radius af cirklen
    # Tallet 2 er den parameter, der angiver tykkelsen af uret
    pygame.draw.circle(screen, (255, 153, 204), [300, 300], 200, 2)

    # Kalder funktionen til at tegne timemarkeringerne
    draw_markings()

    # Henter den aktuelle tid for sekund, minut og time og tilegner dem en variabel enkeltvis
    current_time = datetime.now()
    second = current_time.second
    minute = current_time.minute
    hour = current_time.hour

    # Tegner en violet streg, som værende sekundviseren
    start_point = (300, 300) # Variablen angiver, at sekundviseren skal tegnes fra centrum med et koordinat på (300, 300) som x- og y-værdi
    R = 180 # Variablen R betegner radius af linjen, som jeg har justeret til 180 pixels
    theta = second*(360/60) # Sekundviseren skal flytte sig 60 gange rundt, da der går 60 sekunder på et minut.
    pygame.draw.line(screen, (204,153,255), start_point, degrees(R, theta), 2)

    # Tegner en violet streg, som værende minutviseren
    start_point = (300, 300) # Variablen angiver, at minutviseren skal tegnes fra centrum med et koordinat på (300, 300) som x- og y-værdi
    R = 150  # Variablen R betegner radius af linjen, som jeg har justeret til 150 pixels
    theta =  minute*(360/60) # Minutviseren skal flytte sig 60 gange rundt, da der går 60 minutter på en time.
    pygame.draw.line(screen, (204,153,255), start_point, degrees(R, theta), 4)

    # Tegner en violet streg, som værende timeviseren
    start_point = (300, 300) # Variablen angiver, at timeviseren skal tegnes fra centrum med et koordinat på (300, 300) som x- og y-værdi
    R = 120 # Variablen R betegner radius af linjen, som jeg har justeret til 120 pixels
    theta = hour*(360/12) # Timeviseren skal flytte sig 12 gange rundt, da der går 12 timer på et halvt døgn.
    pygame.draw.line(screen, (204,153,255), start_point, degrees(R, theta), 5)
   
    # Opdaterer skærmen og viser, hvad der er tegnet
    pygame.display.flip()

    # Lukker programmet, når brugeren krydser vinduet
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
