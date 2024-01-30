import pygame

# Inicialización de Pygame
pygame.init()

# Inicialización de la superficie de dibujo (Primer dato--> Anchura, Segunda dato--> Altura)
ventana = pygame.display.set_mode((1080,720))
pygame.display.set_caption("Arkanoid")

# Bucle principal del juego
jugando = True
while jugando:
    # Comprobamos los eventos
    #Comprobamos si se ha pulsado el botón de cierre de la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Se pinta la ventana con un color
    # Esto borra los posibles elementos que teníamos anteriormente
    ventana.fill((255, 255, 255))

    # Todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()

    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60)

pygame.quit()
