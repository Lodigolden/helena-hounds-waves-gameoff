# --------------------------------------------------------------------------------------------------
# Main Gameloop object.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from src.components.menu import Menu

import pygame


# --------------------------------------------------------------------------------------------------
class Game_loop:
    """
    A wrapper class to handle the main game loop.
    """

    # ----------------------------------------------------------------------------------------------
    def __init__(self, display_size, fps):
        """
        Parameterized constructor sets the window display size and refresh rate.

        Args:
            display_size (tuple of ints): Size of the game window.
            fps (int): Window refresh rate.
        """

        self.display_size = display_size
        self.fps = fps
        self.running = True

    # ----------------------------------------------------------------------------------------------
    def run(self):
        """
        Runs the main game loop.
        """

        pygame.init()
        self.wn = pygame.display.set_mode(self.display_size)
        self.clock = pygame.time.Clock()
        self.menu = Menu(self.display_size, self.wn)

        while self.running:
            self.handle_events()
            self.update()
            self.render()

        pygame.quit()

    # ----------------------------------------------------------------------------------------------
    def handle_events(self):
        """
        Handles user inputs / game events.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    # ----------------------------------------------------------------------------------------------
    def update(self):
        """
        Updates the game.
        """

        self.menu.display()
        self.wn.fill("purple")

    # ----------------------------------------------------------------------------------------------
    def render(self):
        """
        Renders the updated game.
        """

        pygame.display.flip()
        self.clock.tick(self.fps)
