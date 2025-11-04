# --------------------------------------------------------------------------------------------------
# Main Gameloop object.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from components.menu import Menu

from enum import Enum
import pygame

# --------------------------------------------------------------------------------------------------

class Game_state(Enum):
    """
    Enum class for game states.
    """
    MENU_STATE = 0


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

        # Configuration variables.
        self.display_size = display_size
        self.fps = fps
        self.running = True
        game_state = Game_state.MENU_STATE

        # Child initialization.
        pygame.init()
        self.wn = pygame.display.set_mode(self.display_size)
        self.clock = pygame.time.Clock()
        self.menu = Menu(self.display_size, self.wn)

        self.menu.enable()

    # ----------------------------------------------------------------------------------------------
    def run(self):
        """
        Runs the main game loop.
        """

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

        if self.menu.is_enabled():
            self.menu.display()
        else:
            self.wn.fill("purple")

    # ----------------------------------------------------------------------------------------------
    def render(self):
        """
        Renders the updated game.
        """

        pygame.display.flip()
        self.clock.tick(self.fps)
