import os
import pygame
from common import config

class GameView:
    def __init__(self, screen, model):
        self.screen = screen
        self.model = model
        image_path = os.path.join(os.path.dirname(__file__), "..", "asset", "gameover.jpg")
        self.game_over_image = pygame.image.load(image_path)
        self.game_over_image = pygame.transform.scale(self.game_over_image, (model.width, model.height))

        self.font = pygame.font.SysFont(None, 36)
        self.button_rect = pygame.Rect(
            (model.width - config.BUTTON_SIZE[0]) // 2,
            (model.height - config.BUTTON_SIZE[1]) // 2,
            config.BUTTON_SIZE[0], config.BUTTON_SIZE[1]
        )

    def render(self):
        self.screen.fill(config.BG_COLOR)
        if self.model.game_over:
            self.screen.blit(self.game_over_image, (0, 0))
            pygame.draw.rect(self.screen, config.BUTTON_COLOR, self.button_rect)
            text_surface = self.font.render("Play Again", True, config.BUTTON_TEXT_COLOR)
            text_rect = text_surface.get_rect(center=self.button_rect.center)
            self.screen.blit(text_surface, text_rect)
        elif self.model.win:
            self.display_win_message()
        else:
            self.model.pipe_shape.draw(self.screen)
            pygame.draw.circle(self.screen, config.BLUE, self.model.dot_pos, self.model.dot_radius)

        pygame.display.flip()

    def display_win_message(self):
        win_text = self.font.render("You Win!", True, (0, 255, 0))  # Green color for winning
        text_rect = win_text.get_rect(center=(self.model.width // 2, self.model.height // 4))
        self.screen.blit(win_text, text_rect)

    def is_restart_clicked(self, pos):
        return self.model.game_over and self.button_rect.collidepoint(pos)
