from code.Const import BLOCK_SIZE, C_GREEN
import pygame

class Snake:
    def __init__(self):
        self.body = [[100, 100]]
        self.direction = 'RIGHT'
        self.alive = True

    def move(self):
        x, y = self.body[0]

        if self.direction == 'UP':
            y -= BLOCK_SIZE
        elif self.direction == 'DOWN':
            y += BLOCK_SIZE
        elif self.direction == 'LEFT':
            x -= BLOCK_SIZE
        elif self.direction == 'RIGHT':
            x += BLOCK_SIZE

        new_head = [x,y]


        #verifica colisão

        if new_head in self.body:
            self.alive = False
            return
        
        self.body.insert(0, new_head)


    def to_update_snake(self):
        if self.alive:
            self.move()
            self.body.pop() # Remove a �ltima parte do corpo para simular movimento

    def change_direction(self, direction):
        oposts = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if direction != oposts.get(self.direction, ""):
            self.direction = direction

    def draw_snake(self, windown):
        for block in self.body:
            pygame.draw.rect(windown, C_GREEN, (*block, BLOCK_SIZE, BLOCK_SIZE)) #*block desempacota a tupla block