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
        self.w = self.sprite.get_height()
        self.h = self.sprite.get_width()

        if self.frames is None:
            self.frames = []
        
        self._get_frames()

    def _get_current_frame(self):
        return self.active_frame

    def _get_current_sprite(self):
        if len(self.frames) == 0:
            return
        
        if self.dt > (60 / self.play_speed):
            self.dt = 0
            self.active_frame = (self.active_frame + 1) % len(self.frames)
        else:
            self.dt += 1        
        
        sprite = self.frames[self.active_frame]
        return sprite

    def _get_frames(self):
        for f in range(self.animation_length + 1):
            target_path = self.base_path + self.file_prefix + str(f) + self.file_ext    # path/to/asset/prefix0.jpg
            if os.path.isfile(target_path):
                print(target_path)
                frame = pygame.image.load(target_path).convert_alpha()
                self.frames.append(frame)
                
        print(self.frames)

    def play(self):
        # run once when the animation of the player or enemy changes
        asyncio.run(self._play_animation)

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