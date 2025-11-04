# --------------------------------------------------------------------------------------------------
# Game menu.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from core.states import Game_state

import pygame_menu

# --------------------------------------------------------------------------------------------------
class Menu(pygame_menu.Menu):
    """
    A menu wrapper for the game.
    """

    # ----------------------------------------------------------------------------------------------
    def __init__(self, display_size, wn, game_loop):
        """
        Parameterized constructor sets the display size and references the window.

        Args:
            display_size (tuple of ints): Size of the game window.
            wn (Object): The rendered window.
            game_loop (Game_loop): Reference to the main game loop object.
        """

        self.wn = wn
        self.game_loop = game_loop

        super().__init__(
            "Welcome",
            display_size[0],
            display_size[1],
            theme=pygame_menu.themes.THEME_BLUE,
        )

        self.add.button("Play", self.handle_play)

    # ----------------------------------------------------------------------------------------------
    def display(self):
        """
        Displays the menu.
        """

        if (self.game_loop.game_state == Game_state.MENU_STATE):
            self.mainloop(self.wn)

    # ----------------------------------------------------------------------------------------------
    def handle_play(self):
        """
        Handles when the user clicks the "Play" button.
        """

        self.game_loop.game_state = Game_state.GAME_STATE
        self.disable()
