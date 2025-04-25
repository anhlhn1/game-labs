import pygame
from model.game_model import GameModel
from view.game_view import GameView
from controller.game_controller import GameController

def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Drag the Dot Through the Pipe")

    clock = pygame.time.Clock()
    model = GameModel(WIDTH, HEIGHT)
    view = GameView(screen, model)
    controller = GameController(model, view)  # Pass both model and view to the controller

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            running = controller.handle_event(event)  # Pass each event here

        view.render()  # Render the updated view
        clock.tick(60)  # Limit the game loop to 60 frames per second

if __name__ == "__main__":
    main()