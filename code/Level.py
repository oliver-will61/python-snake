from pygame import Surface, Rect
import pygame
from code.Snake import Snake
from code.Food import Food
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, C_BLACK


class Level:
    def __init__(self, window: Surface):
        self.window = window
        self.reset()


    def level_run(self):
        while True:
            self.events()
            self.to_update()
            self.draw()


    def reset(self):
            self.snake = Snake()
            self.food = Food()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('UP') 
                elif event.key  == pygame.K_DOWN:
                    self.snake.change_direction('DOWN')
                elif event.key  == pygame.K_LEFT:
                    self.snake.change_direction('LEFT')
                elif event.key  == pygame.K_RIGHT:
                    self.snake.change_direction('RIGHT')
    
    def to_update (self):
        if self.snake.alive:
            self.snake.to_update_snake()

            #verifica se comeu a comida

            if self.snake.body[0] == self.food.position:
                self.food.new_position()
                self.snake.body.append(self.snake.body[-1])  # Cresce
            
            # verifica colisão com a parede
            x, y = self.snake.body[0]
            if x < 0 or x >= WIN_WIDTH or y < 0 or y >= WIN_HEIGHT:
                self.snake.alive = False
        
        else:
            self.reset()

    def draw(self):
        self.window.fill(C_BLACK)
        self.snake.draw_snake(self.window)
        self.food.draw_food(self.window)
        pygame.display.flip()