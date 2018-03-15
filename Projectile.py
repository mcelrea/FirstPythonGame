import pygame

class Bullet(object):


    def __init__(self, x, y, r, color, dir):
        self.x = x
        self.y = y
        self.radius = r
        self.color = color
        self.dir = dir
        self.hitbox = pygame.Rect(x-r,y-r,r*2,r*2)

    def isOffScreen(self, screen):
        w, h = pygame.display.get_surface().get_size()
        # off right side of screen
        if self.x > w:
            return True
        # off left side of screen
        elif self.x < 0:
            return True
        #off the top of the screen
        elif self.y < 0:
            return True
        #off the bottom of the screen
        elif self.y > h:
            return True
        #else if must still be on the screen
        else:
            return False
        
    def hasHit(self, rect):
        if self.hitbox.colliderect(rect):
            return True
        else:
            return False

    def move(self):
        if self.dir == "right":
            self.x += 3.1
            self.hitbox.x = self.x - self.radius
        elif self.dir == "left":
            self.x -= 3.1
            self.hitbox.x = self.x - self.radius
        elif self.dir == "down":
            self.y += 3.1
            self.hitbox.y = self.y - self.radius
        elif self.dir == "up":
            self.y -= 3.1
            self.hitbox.y = self.y - self.radius

    def draw(self,screen):
        pygame.draw.circle(screen,
                           self.color,
                           (int(self.x), int(self.y)),
                           self.radius)
        pygame.draw.rect(screen,
                         (255,255,0),
                         pygame.Rect(int(self.hitbox.x),
                                     int(self.hitbox.y),
                                     self.hitbox.width,
                                     self.hitbox.height),
                         1)

