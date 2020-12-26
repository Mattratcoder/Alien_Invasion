import sys

import pygame

class AlienInvasion:
    #overall class to manage the game assets and behavior
    
    def __init__(self):
        #initialize the game and create game resources
        pygame
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
    
    def run_game(self):
        #start the main loop for the game
        While True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            #make the most recently drawn screen visible
            pygame.display.flip()
            
            
if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()