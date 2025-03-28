from code.Difficulty import Difficulty
from code.Const import BLOCK_SIZE, C_GREEN, C_YELLOW, HUD, WIN_WIDTH, WIN_HEIGHT
import pygame

class Snake(Difficulty):
    def __init__(self):
        super().__init__()

        self.body = [[100, 100]] #posição inicial da cobra
        self.direction = 'RIGHT'
        self.collision = False
        self.velocity = self.apply_Difficulty()
        self.color = C_YELLOW

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
            self.collision = True
            return
        
        self.body.insert(0, new_head)


    def to_update_snake(self):
        if not self.collision:
            self.move()
            self.body.pop() # Remove a �ltima parte do corpo para simular movimento

    def change_direction(self, direction):
        oposts = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if direction != oposts.get(self.direction, ""):
            self.direction = direction

    def draw_snake(self, windown):

        hud_height = HUD['hud_height']  # Altura do HUD
        
        # Define a área onde a cobra pode ser desenhada
        clip_rect = pygame.Rect(0, hud_height, WIN_WIDTH, WIN_HEIGHT - hud_height)
        windown.set_clip(clip_rect)  # Aplica o recorte
        
        for block in self.body:
            pygame.draw.rect(windown, self.color, (*block, BLOCK_SIZE, BLOCK_SIZE))
        
        windown.set_clip(None)  # Remove o recorte