import pygame

class Ship:
    #a class to manage the ship
    def __init__(self, ai_game):
    #initialize the ship and set it's starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #load the ship image and get it's rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #start each new ship at the bottom of the screen
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        #draw the ship at its current location
        self.screen.blit(self.image, self.rect)
        