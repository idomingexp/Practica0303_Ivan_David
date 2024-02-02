import pygame

pygame.init()
ventana = pygame.display.set_mode((1080,720))
pygame.display.set_caption("Ejemplo 3")

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [3,3]
ballrect.move_ip(0,0)

# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()

# Pongo el bate en la parte inferior de la pantalla
baterect.move_ip(540,620)

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
    ventana.fill((39,55,70))
    ventana.blit(ball, ballrect)

    # Dibujo el bate
    ventana.blit(bate, baterect)
    pygame.display.flip()
    pygame.time.Clock().tick(144)

pygame.quit()