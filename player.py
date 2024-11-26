import pygame
import math

from animated_sprite import SpriteAnimation

class Player():
    max_speed = 0

    def __init__(self, level):
        self.position = [math.floor(level.w / 2), math.floor(level.h / 2)]
        self.animations = {
            "idle": SpriteAnimation('/home/kraibse/projects/scavanger/assets/sprites/player/', 'player0', 1)
        }

        self.current_animation = "idle"
        self.get_current_animation().play()

    def change_animation(self, new_anim="idle"):
        animation = self.get_current_animation()
        animation.stop()
        
        self.current_animation = new_anim
        animation.play()

    def get_current_animation(self):
        return self.animations.get(self.current_animation)

    def is_accelerating(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return True
        
        return False

    def move(self):
        self.current_animation = "idle"

        mousex, mousey = pygame.mouse.get_pos()
        mx = mousex - self.position[0]
        my = mousey - self.position[1]

        distance = math.sqrt(mx ** 2 + my ** 2)

        # TODO: accelerate and deccelerate smoothly
        motion = [mx / distance, my / distance] * self.max_speed    # move the player at a constant speed for now

        if self.is_accelerating():
            self.position[0] + motion[0]
            self.position[1] + motion[1]


    def mine(self):
        pass