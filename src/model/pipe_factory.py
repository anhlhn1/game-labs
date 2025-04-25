import math
import pygame
from common import config


class PipeShape:
    def draw(self, screen):
        raise NotImplementedError("This method should be overridden by subclasses.")

class RectPipe(PipeShape):
    def __init__(self, rect):
        self.rect = rect

    def draw(self, screen):
        pygame.draw.rect(screen, config.PIPE_COLOR, self.rect)

class CirclePipe(PipeShape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, config.PIPE_COLOR, self.center, self.radius, width=20)

class MaskPipe(PipeShape):
    def __init__(self, mask_surface):
        self.mask_surface = mask_surface
        self.mask = pygame.mask.from_surface(mask_surface)
        self.rect = self.mask_surface.get_rect()

    def draw(self, screen):
        screen.blit(self.mask_surface, self.rect.topleft)

    def is_inside(self, pos, dot_radius):
        x, y = pos
        try:
            # Check if any point of the edge of the dot goes outside the pipe
            for angle in range(0, 360, 10):  # Check multiple points on the circle's boundary
                # Calculate the edge point using cos and sin
                edge_x = int(x + dot_radius * math.cos(math.radians(angle)))
                edge_y = int(y + dot_radius * math.sin(math.radians(angle)))

                rel_x = edge_x - self.rect.x
                rel_y = edge_y - self.rect.y

                print("edge_x: ", edge_x, "edge_y: ", edge_y)
                print("rel_x: ", rel_x, "rel_y: ", rel_y)

                # If any edge point goes outside the pipe, return False
                if self.mask.get_at((rel_x, rel_y)) == 0:
                    return False
            return True
        except IndexError:
            return False

    def get_starting_point(self, dot_radius):
        width, height = self.mask.get_size()
        for y in range(height - 1, -1, -1):  # Start from bottom
            for x in range(width - 1, -1, -1):  # Then scan right to left
                if self.mask.get_at((x, y)) == 1:
                    starting_x = x + self.rect.x - 2*dot_radius
                    starting_y = y + self.rect.y - 2*dot_radius
                    return [starting_x, starting_y]
        return [self.rect.centerx, self.rect.centery]  # fallback

class PipeFactory:
    @staticmethod
    def create_pipe(shape_type, **kwargs):
        if shape_type == "rect":
            return RectPipe(kwargs.get("rect"))
        elif shape_type == "circle":
            return CirclePipe(kwargs.get("center"), kwargs.get("radius"))
        elif shape_type == "mask":
            return MaskPipe(kwargs.get("mask_surface"))
        else:
            raise ValueError("Unsupported pipe shape type: " + shape_type)
