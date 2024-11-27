import os
import asyncio
import pygame


class SpriteAnimation():
    play_speed = 1

    active_frame = -1
    frames = None

    dt = 0

    def __init__(self, base_path, file_prefix, animation_length, file_ext='.jpg'):
        # self.sprite = pygame.image.load(base_path + file_prefix + file_ext)
        self.base_path = base_path
        self.file_prefix = file_prefix
        self.animation_length = animation_length
        self.file_ext = file_ext
        
        self.clock = pygame.time.Clock()

        if self.frames is None:
            self.frames = []

        if os.path.isfile(base_path + file_prefix + '0' + file_ext):
            print("The file was found.")
        
        self._get_frames()
        self.w = self.frames[0].get_height()
        self.h = self.frames[0].get_width()

    def _get_current_frame(self):
        return self.active_frame

    def _get_current_sprite(self):
        if len(self.frames) == 0:
            return
        
        if self.dt > (60 / self.play_speed):
            self.dt = 0
            self.active_frame = (self.active_frame + 1) % len(self.frames)
        else:
            self.dt += self.clock.tick(60)    
        
        sprite = self.frames[self.active_frame]
        return sprite

    def _get_frames(self):
        for f in range(self.animation_length):
            target_path = self.base_path + self.file_prefix + str(f) + self.file_ext    # path/to/asset/prefix0.jpg
            if os.path.isfile(target_path):
                print(target_path)
                frame = pygame.image.load(target_path).convert_alpha()
                self.frames.append(frame)

        print(self.frames)

    def play(self):
        # run once when the animation of the player or enemy changes
        self._play_animation()

    def stop(self):
        self.is_running = False
        self.active_frame = 0
        self.dt = 0

    async def _play_animation(self):
        self.is_running = True
        while self.is_running:
            self.active_frame = (self.active_frame + 1) % len(self.frames)
            await asyncio.sleep(1 / self.play_speed)

    def set_animation_speed(self, anim_length):
        self.animation_length = anim_length
        return self