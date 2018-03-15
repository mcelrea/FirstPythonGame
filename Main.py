import pygame
import Projectile

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
done = False


player1 = pygame.image.load("smallCharacter.png")
p1x = 100
p1y = 100
p1HitBox = player1.get_rect()
p1Bullets = []
p1Dir = "right"

player2 = pygame.image.load("smallCharacter.png")
p2x = 400
p2y = 400
p2HitBox = player2.get_rect()

while not done:
    # required by pygame, check for keypresses ONE time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            p1Bullets.append(Projectile.Bullet(p1x,p1y,p1Dir,5))

    # check for keypresses continually
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        p1x += 3
        p1Dir = "right"
    if pressed[pygame.K_LEFT]:
        p1x -= 3
        p1Dir = "left"
    if pressed[pygame.K_UP]:
        p1y -= 3
        p1Dir = "up"
    if pressed[pygame.K_DOWN]:
        p1y += 3
        p1Dir = "down"

    # update hit boxes
    p1HitBox.x = p1x
    p1HitBox.y = p1y
    p2HitBox.x = p2x
    p2HitBox.y = p2y

    # move the bullets
    for b in p1Bullets:
        b.move()
        if b.isOffScreen() == True:
            p1Bullets.remove(b)
        elif b.isColliding(p2HitBox):
            p1Bullets.remove(b)

    # check for collisions
    if p1HitBox.colliderect(p2HitBox):
        p1HitBox.x = 10
        p1HitBox.y = 10
        p1x = 10
        p1y = 10

    # draw all the graphics
    screen.fill((0,0,0))
    textsurface = myfont.render("Bullets: " + str(len(p1Bullets)), False, (255, 255, 255))
    screen.blit(textsurface, (0, 0))
    for b in p1Bullets:
        b.draw(screen)
    pygame.draw.rect(screen,
                     (0,255,0),
                     p1HitBox,
                     1)
    pygame.draw.rect(screen,
                     (0, 255, 0),
                     p2HitBox,
                     1)
    screen.blit(player1, (p1x,p1y))
    screen.blit(player2, (p2x, p2y))
    pygame.display.flip()