import pygame
from pygame.font import Font
from pygame import Surface, Rect
from code.Snake import Snake
from code.Food import Food
from code.Score import Score
from code.Const import WIN_WIDTH, WIN_HEIGHT, HUD, SNAKE_VELOCITY, PATH_BG_IMAGEM, HUD, C_ORAGE


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

            if self.snake.collision == False:
                self.events()
                self.to_update()
                self.draw()
                self.clock.tick(SNAKE_VELOCITY) # defini o fps do jogo
            
            else: 
                break

        self.window.blit(self.background, (0,0))

        pygame.mixer_music.load('./assets/audio/level_sound_end.wav')
        pygame.mixer_music.play(-1) #'-1' faz a música tocar em loop infinito
        
        self.score.update_best_score()
        self.game_over()

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
        if not self.snake.collision:
            self.snake.to_update_snake()
            
            # verifica colisão com a parede
            x, y = self.snake.body[0]

            if x >= WIN_WIDTH or x < 0 or  y >= WIN_HEIGHT or y < HUD['hud_height']:
                self.snake.collision = True
                 
            self.snake.body[0] = [x,y]

            #verifica se comeu a comida

            if self.snake.body[0] == self.food.position:
                self.obj_sound('./assets/audio/eat.wav') # som da pontuação 
                self.score.current_score += 1
                self.food.relocate()
                self.snake.body.append(self.snake.body[-1])  # Cresce
        
            #self.reset()

    def draw(self):
        self.window.blit(self.background, (0,0))
        self.score.score_hud(self.window)
        self.snake.draw_snake(self.window)
        self.food.draw_food(self.window)
        pygame.display.flip()
        
    def obj_sound(self, path_sound):
        sound = pygame.mixer.Sound(path_sound)
        sound.play()

    def game_over_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


    def game_over(self):

        while True:


            tamanho_fonte_principal = 50
            tamanho_fonte = 40
            x = WIN_WIDTH / 2
            y = WIN_HEIGHT / 2

            self.game_over_text(tamanho_fonte_principal, "Game Over!", C_ORAGE, (x, y - tamanho_fonte_principal))
            self.game_over_text(tamanho_fonte, f"Pontuação: {self.score.current_score}", C_ORAGE, (x, y))
            self.game_over_text(tamanho_fonte, f"Recorde: {self.score.best_score['best_score']}", C_ORAGE, (x, y + tamanho_fonte))
            pygame.display.flip()
        
