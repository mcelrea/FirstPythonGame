import pygame

class Bullet(object):

    def __init__(self, x, y, dir, r):
        self.x = x
        self.y = y
        self.dir = dir
        self.r = r
        self.hitbox = pygame.Rect(x-r,y-r,r*2,r*2)

    def isOffScreen(self):
        #left of screen
        if self.x < 0:
            return True
        #right of screen
        elif self.x > pygame.display.get_surface().get_width():
            return True
        #top of screen
        elif self.y < 0:
            return True
        #bottom of screen
        elif self.y > pygame.display.get_surface().get_height():
            return True
        #else the bullet must be on the screen
        else:
            return False

    def isColliding(self, otherRect):
        if self.hitbox.colliderect(otherRect) == True:
            return True
        else:
            return False

    def draw(self, screen):
        pygame.draw.circle(screen,
                           (255, 0, 0),
                           (int(self.x), int(self.y)),
                           self.r)
        pygame.draw.rect(screen,(0,255,0),self.hitbox,1)

    def move(self):
        if self.dir == "right":
            self.x += 3
            self.hitbox.x = self.x - self.r
        elif self.dir == "left":
            self.x -= 3
            self.hitbox.x = self.x - self.r
        elif self.dir == "up":
            self.y -= 3
            self.hitbox.y = self.y - self.r
        elif self.dir == "down":
            self.y += 3
            self.hitbox.y = self.y - self.r
