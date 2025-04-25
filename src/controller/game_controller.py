import pygame

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return False  # Stop the game if the user quits

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.view.is_restart_clicked(event.pos):
                self.model.reset_game()  # Restart the game if the restart button is clicked
            else:
                self.model.try_start_drag(event.pos)  # Start dragging the blue point

        elif event.type == pygame.MOUSEBUTTONUP:
            self.model.stop_drag()  # Stop dragging

        elif event.type == pygame.MOUSEMOTION:
            if self.model.dragging and not self.model.game_over and not self.model.win:
                self.model.update_dot_position(event.pos)  # Update the position of the dot while dragging

        return True  # Continue the game loop

    def render(self):
        self.view.render()
