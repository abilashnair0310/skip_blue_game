import pygame
import random
import sys
from player import Human_player
from screen import Screen
from game import Game

pygame.init()
pygame.mixer.quit()
game_over = False
Screen = Screen()
player = Human_player(x=Screen.width/2, y=Screen.height - 2*50)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -= player.size
            elif event.key == pygame.K_RIGHT:
                player.x += player.size
    
    Game.drop_enemies(Screen.width - player.size)
    Game.update_enemy_positions()
    Game.set_level()
    Screen.update_screen(player,Game.enemy_list,Game.score)

    if Game.collision_check(player):
        game_over = True
        break
