# --------------------------------------------------------------------------------------------------
# Main Gameloop object.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from components.menu import Menu
from components.pirate import Pirate
from components.ship import Ship
from components.island import Island, Home_island
from core.states import Game_state
from core.utils import fetch_asset

import os
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

        current_dir = os.getcwd()

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

        self.map_background = fetch_asset(
            os.path.join(current_dir, "assets", "backgrounds", "water.png")
        )
        self.home_background = fetch_asset(
            os.path.join(current_dir, "assets", "backgrounds", "home.png")
        )

        self.ship = Ship(
            self,
            self.wn.get_width() / 2,
            self.wn.get_height() / 2,
            os.path.join(current_dir, "assets", "ships", "player_ship.png"),
        )

        # All Islands:
        self.islands = []
        self.islands.append(
            Island(self, self.wn.get_width() / 4, self.wn.get_height() / 4)
        )
        self.islands.append(
            Island(self, 3 * self.wn.get_width() / 4, 3 * self.wn.get_height() / 4)
        )
        self.islands.append(
            Island(self, self.wn.get_width() / 4, 3 * self.wn.get_height() / 4)
        )
        self.islands.append(
            Home_island(self, 3 * self.wn.get_width() / 4, self.wn.get_height() / 4)
        )

        self.pirate = Pirate(
            self, self.wn.get_width() / 10, 3 * self.wn.get_height() / 3
        )

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
            case Game_state.GAME_MAP_STATE:
                self.handle_game_map_state()
            case Game_state.GAME_PLATFORMER_STATE:
                self.handle_game_platformer_state()
            case Game_state.GAME_HOME_STATE:
                self.handle_home_state()
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
    def handle_game_map_state(self):
        """
        State for the main map.
        """

        self.wn.blit(self.map_background, (0, 0))
        self.ship.render()

        for island in self.islands:
            island.render()

            if (abs(self.ship.pos.x - island.pos.x) < 30) and (
                abs(self.ship.pos.y - island.pos.y) < 30
            ):
                if island.is_home:
                    self.pirate.pos.x = self.wn.get_width() / 10
                    self.pirate.pos.y = 2 * self.wn.get_height() / 3
                    self.game_state = Game_state.GAME_HOME_STATE
                else:
                    self.game_state = Game_state.GAME_PLATFORMER_STATE

    # ----------------------------------------------------------------------------------------------
    def handle_game_platformer_state(self):
        """
        State for a platformer level.
        """

        self.wn.fill("black")

    # ----------------------------------------------------------------------------------------------
    def handle_home_state(self):
        """
        State for the home base.
        """

        self.wn.blit(self.home_background, (0, 0))
        self.pirate.render()

        # Return to map.
        if self.pirate.pos.x < 0:
            self.ship.pos.x -= 50
            self.game_state = Game_state.GAME_MAP_STATE
