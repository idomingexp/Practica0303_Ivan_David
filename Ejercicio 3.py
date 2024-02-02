import pygame

pygame.init()
ventana = pygame.display.set_mode((1200,673))
pygame.display.set_caption("Ejemplo 3")

#Cargamos el fondo de la ventana
fondo = pygame.image.load("fondo.jpg")
ventana.blit(fondo, (0,0))

#Cargamos la bola
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [3,3]
ballrect.move_ip(0,0)

# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()

# Pongo el bate en la parte inferior de la pantalla
# Primer dato es la posición horizontal y segundo la vertical
baterect.move_ip(600,600)

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-4,0)
        
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(4,0)
        

    # Compruebo si hay colisión
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]
    #Hacemos que el bate no se salga de los limites de la pantalla
    if baterect.left < 0:
       baterect = baterect.move(4,0)
    if baterect.right > ventana.get_width():
        baterect = baterect.move(-4,0)
     #Borrar lo que habia en la ventana
    ventana.fill((0,0,0))
     #Ponemos todo el rato el fondo
    ventana.blit(fondo, (0,0))
    ventana.blit(ball, ballrect)

    # Dibujo el bate
    ventana.blit(bate, baterect)
    pygame.display.flip()
    pygame.time.Clock().tick(144)

pygame.quit()
