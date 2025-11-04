# --------------------------------------------------------------------------------------------------
# Main Gameloop object.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from components.menu import Menu
from components.ship import Ship
from core.states import Game_state

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

        # Configuration variables.
        self.display_size = display_size
        self.fps = fps
        self.running = True
        self.game_state = Game_state.MENU_STATE

        # Child initialization.
        pygame.init()
        self.wn = pygame.display.set_mode(self.display_size)
        self.clock = pygame.time.Clock()
        self.menu = Menu(self.display_size, self.wn, self)
        self.keys = pygame.key.get_pressed()
        
        self.ship = Ship(self)
        self.ship.pos.x = self.wn.get_width() / 2
        self.ship.pos.y = self.wn.get_height() / 2

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

        # Look for special events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # Get keys pressed by user:
        self.keys = pygame.key.get_pressed()

        # Update clock tick:
        self.dt = self.clock.tick(60) / 1000

    # ----------------------------------------------------------------------------------------------
    def update(self):
        """
        Updates the game.
        """

        match self.game_state:
            case Game_state.MENU_STATE:
                self.handle_menu_state()
            case Game_state.GAME_STATE:
                self.handle_game_state()
            case _:
                self.wn.fill("purple")

    # ----------------------------------------------------------------------------------------------
    def render(self):
        """
        Renders the updated game.
        """

        pygame.display.flip()
        self.clock.tick(self.fps)

    # ----------------------------------------------------------------------------------------------
    def handle_menu_state(self):
        """
        State for the menu.
        """

        if self.game_state == Game_state.MENU_STATE:
            self.menu.display()

    # ----------------------------------------------------------------------------------------------
    def handle_game_state(self):
        """
        State for playing the game.
        """

        self.wn.fill("blue")
        self.ship.render()
