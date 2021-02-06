import pygame
from Color import color
from player import Human_player

class Screen:
    def __init__(self, score = 0, width = 800, height = 600, background_color = color.BLACK, font_type = 'monospace', font_size = 35, clock_tick = 30 ):
        self.height = height
        self.width = width
        self.background_color = background_color
        self.screen = pygame.display.set_mode((width, height))
        self.font_type = font_type
        self.font_size = font_size
        self.font = pygame.font.SysFont(font_type, font_size)
        self.clock = pygame.time.Clock()
        self.clock_tick = clock_tick
        self.score = score

    def refresh_background(self):
        self.screen.fill(color.BLACK)

    def draw_enemies(self, enemy_list):
        for enemy in self.enemy_list:
            enemy.draw(self.screen)
    
    def draw_player(self, player):
        player.draw(self.screen)

    def draw_score_label(self, score, color = color.YELLOW):
        self.screen.blit(self.font.render("Score" + str(score),1, color)(self.width-200, self.height-40))
    
    def update_screen(self, player, enemy_list, score):
        refresh_background()
        draw_enemies(enemy_list)
        draw_player(player)
        draw_score_label(score)
        self.clock.tick(self.clock_tick)
        pygame.display.update()