import os
import pygame
from common import config
from model.pipe_factory import PipeFactory

class GameModel:
    def __init__(self, width, height):
        self.pipe_surface = pygame.image.load(config.PIPE_PATH).convert_alpha()
        self.dot_radius = 15
        self.pipe_shape = PipeFactory.create_pipe("mask", mask_surface=self.pipe_surface, dot_radius=self.dot_radius)
        self.dot_pos = self.pipe_shape.get_starting_point(self.dot_radius)
        self.width, self.height = self.pipe_surface.get_size()
        self.dragging = False
        self.game_over = False
        self.win = False  # Add a flag for win condition
        self.red_line_y = self.get_red_line_position()  # Get the Y position of the red line

    def get_red_line_position(self):
        # Find the Y position of the red line (this depends on your pipe_mask image)
        # This method assumes the red line is a specific color, and you can find its position
        for y in range(self.height):
            for x in range(self.width):
                # Check if the pixel is red (or a specific color code for red)
                if self.pipe_surface.get_at((x, y)) == (255, 0, 0, 255):  # RGBA for red
                    return y
        return None  # Return None if no red line is found

    def is_in_pipe(self):
        return self.pipe_shape.is_inside(self.dot_pos, self.dot_radius)

    def update_dot_position(self, pos):
        self.dot_pos = list(pos)
        if not self.is_in_pipe():
            self.game_over = True
        elif self.red_line_y is not None \
            and self.dot_pos[1] <= self.red_line_y:  # Check if the blue point passed the red line
            self.win = True

    def try_start_drag(self, mouse_pos):
        dx = mouse_pos[0] - self.dot_pos[0]
        dy = mouse_pos[1] - self.dot_pos[1]
        distance_squared = dx * dx + dy * dy
        if distance_squared <= self.dot_radius * self.dot_radius:
            self.dragging = True
            return True
        return False

    def stop_drag(self):
        self.dragging = False

    def reset_game(self):
        self.dot_pos = self.pipe_shape.get_starting_point(self.dot_radius)
        self.dragging = False
        self.game_over = False
        self.win = False  # Reset win condition
