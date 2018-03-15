import pygame
import Projectile

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

done = False

player1 = pygame.image.load("smallCharacter.png")
player1x = 100
player1y = 100
player1dir = "right"
player1HitBox = player1.get_rect()
p1Bullets = []

player2 = pygame.image.load("smallCharacter.png")
player2x = 400
player2y = 400
player2HitBox = player2.get_rect()
p2Bullets = []
player2dir = "right"

while not done:
    #REQUIRED by pygame: check for single keypress
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            p1Bullets.append(Projectile.Bullet(player1x,
                                               player1y,
                                               5,
                                               (255,0,0),
                                               player1dir))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            p2Bullets.append(Projectile.Bullet(player2x,
                                               player2y,
                                               5,
                                               (0,255,0),
                                               player2dir))

    #checking for continuous key presses
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        player1y -= 3
        player1dir = "up"
    if pressed[pygame.K_s]:
        player1y += 3
        player1dir = "down"
    if pressed[pygame.K_d]:
        player1x += 3
        player1dir = "right"
    if pressed[pygame.K_a]:
        player1x -= 3
        player1dir = "left"
    if pressed[pygame.K_UP]:
        player2y -= 3
        player2dir = "up"
    if pressed[pygame.K_DOWN]:
        player2y += 3
        player2dir = "down"
    if pressed[pygame.K_RIGHT]:
        player2x += 3
        player2dir = "right"
    if pressed[pygame.K_LEFT]:
        player2x -= 3
        player2dir = "left"

    #updating player hit boxes
    player1HitBox.x = player1x
    player1HitBox.y = player1y
    player2HitBox.x = player2x
    player2HitBox.y = player2y

    #move bullets
    for b in p1Bullets:
        b.move()
        if b.isOffScreen(screen):
            p1Bullets.remove(b)
        elif b.hasHit(player2HitBox):
            p1Bullets.remove(b)
    for b in p2Bullets:
        b.move()
        if b.isOffScreen(screen):
            p2Bullets.remove(b)
        elif b.hasHit(player1HitBox):
            p2Bullets.remove(b)

    #checking for collisions
    if player1HitBox.colliderect(player2HitBox):
        player1x = 0
        player1y = 0

    #drawing graphics
    screen.fill((0,0,0))
    textsurface = myfont.render("Bullets: " + str(len(p1Bullets)), False, (255, 0, 255))
    screen.blit(textsurface, (0, 0))
    for b in p1Bullets:
        b.draw(screen)
    for b in p2Bullets:
        b.draw(screen)

    screen.blit(player1, (player1x, player1y))
    screen.blit(player2, (player2x, player2y))

    pygame.draw.rect(screen,
                     (0,255,0),
                     player1HitBox,
                     1)
    pygame.draw.rect(screen,
                     (0, 255, 0),
                     player2HitBox,
                     1)
    pygame.display.flip()