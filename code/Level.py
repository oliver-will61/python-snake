import pygame
from pygame import Surface 
from code.Snake import Snake
from code.Food import Food
from code.Score import Score
from code.Const import WIN_WIDTH, WIN_HEIGHT, HUD, C_GREEN, SNAKE_VELOCITY, PATH_BG_IMAGEM, BLOCK_SIZE, HUD


class Level:
    def __init__(self, window: Surface):   
        self.window = window
        self.bg_imagem = pygame.image.load(PATH_BG_IMAGEM).convert_alpha() #carega a imagem
        self.background = pygame.transform.scale(self.bg_imagem, (WIN_WIDTH, WIN_HEIGHT))  # Ajusta a imagem ao tamanho da tela
        self.clock = pygame.time.Clock()    
        self.reset()

    def reset(self):
        self.snake = Snake()
        self.food = Food()
        self.score = Score()

    def level_run(self):
        pygame.mixer_music.load('./assets/audio/level_sound.wav')
        pygame.mixer_music.play(-1) #'-1' faz a música tocar em loop infinito
        while True:
            self.events()
            self.to_update()
            self.draw()
            self.clock.tick(SNAKE_VELOCITY) # defini o fps do jogo

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('UP') 
                    self.obj_sound('./assets/audio/direction.mp3')
                elif event.key  == pygame.K_DOWN:
                    self.snake.change_direction('DOWN')
                    self.obj_sound('./assets/audio/direction.mp3')
                elif event.key  == pygame.K_LEFT:
                    self.snake.change_direction('LEFT')
                    self.obj_sound('./assets/audio/direction.mp3')
                elif event.key  == pygame.K_RIGHT:
                    self.snake.change_direction('RIGHT')
                    self.obj_sound('./assets/audio/direction.mp3')
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    
    def to_update (self):
        if self.snake.alive:
            self.snake.to_update_snake()
            
            # verifica colisão com a parede
            x, y = self.snake.body[0]

            if x >= WIN_WIDTH or x < 0 or  y >= WIN_HEIGHT or y < HUD['hud_height']:
                self.snake.alive = False
                 
            self.snake.body[0] = [x,y]

            #verifica se comeu a comida

            if self.snake.body[0] == self.food.position:
                self.obj_sound('./assets/audio/eat.wav') # som da pontuação 
                self.score.current_score += 1
                self.food.relocate()
                self.snake.body.append(self.snake.body[-1])  # Cresce
        
        else:
            self.score.update_best_score()
            self.reset()

    def draw(self):
        self.window.blit(self.background, (0,0))
        self.score.score_hud(self.window)
        self.snake.draw_snake(self.window)
        self.food.draw_food(self.window)
        pygame.display.flip()
        
    def obj_sound(self, path_sound):
        sound = pygame.mixer.Sound(path_sound)
        sound.play()
