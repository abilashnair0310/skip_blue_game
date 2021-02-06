import random
from player import Enemy
from screen import Screen

class Game:
    def __init__(self,speed,score,delay = 0.1, max_enemies = 10):
        self.speed = speed
        self.score = score
        self.delay = delay
        self.max_enemies = max_enemies
        self.enemy_list = []

    def set_level(self):
        if self.score < 20:
            self.speed = 5
        elif self.score < 40:
            self.speed = 8
        elif self.score < 60:
            self.speed = 12
        else:
            self.speed = 15
    
    def drop_enemies(self,screen_width):
        delay = random.random()
        if len(self.enemy_list) < self.max_enemies and delay < self.delay:
            x_pos = random.randint(0,screen_width)
            y_pos = 0
            enemy = Enemy(x_pos,y_pos)
            enemy_list.append(enemy)
    
    def update_enemy_positions(self,screen_height):
        new_enemy_list = []
        for idx, enemy in enumerate(enemy_list):
            if enemy.y >= 0 and enemy.y < screen_height:
                enemy.y += self.speed
            else:
                new_enemy_list.pop(idx)
                self.score += 1
        self.enemy_list = new_enemy_list

    def collision_check(self,player):
        for enemy in enemy_list:
            if player.detect_collision(player):
                return True
        return False


    