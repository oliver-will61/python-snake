import random
import pygame
from code.Const import WIN_WIDTH, BLOCK_SIZE, WIN_HEIGHT, C_RED, HUD, C_RED

class Food:
    def __init__(self):
        self.position = list(self.new_position())

    def new_position(self):
        
        x = random.randint(0, (WIN_WIDTH // BLOCK_SIZE) -1 )* BLOCK_SIZE
        
        y = random.randint((HUD['hud_height'] // BLOCK_SIZE), (WIN_HEIGHT // BLOCK_SIZE) -1 )* BLOCK_SIZE
        
        return [x,y]
    
        # self.position = [0,0
        # ] #usado apenas para teste
        
    def draw_food(self, windown):
        pygame.draw.rect(windown, C_RED, pygame.Rect(self.position[0],self.position[1], BLOCK_SIZE, BLOCK_SIZE))

    def relocate(self):
        self.position = list(self.new_position())