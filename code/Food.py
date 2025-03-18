import random
import pygame
from code.Const import WIN_WIDTH, BLOCK_SIZE, WIN_HEIGHT, C_RED

class Food:
    def __init__(self):
        self.new_position()

    def new_position(self):
        self.position = [
            random.randint(0, (WIN_WIDTH // BLOCK_SIZE) -1 )* BLOCK_SIZE,
            random.randint(0, (WIN_HEIGHT // BLOCK_SIZE) -1 )* BLOCK_SIZE
        ]
    def draw_food(self, windown):
        pygame.draw.rect(windown, C_RED, (*self.position, BLOCK_SIZE, BLOCK_SIZE))