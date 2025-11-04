# --------------------------------------------------------------------------------------------------
# Game menu.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
import pygame
import pygame_menu


# --------------------------------------------------------------------------------------------------
class Menu(pygame_menu.Menu):
    """
    A menu wrapper for the game.
    """

    # ----------------------------------------------------------------------------------------------
    def __init__(self, display_size, wn):
        """
        Parameterized constructor sets the display size and references the window.

        Args:
            display_size (tuple of ints): Size of the game window.
            wn (Object): The rendered window.
        """

        self.wn = wn
        super().__init__(
            "Welcome",
            display_size[0],
            display_size[1],
            theme=pygame_menu.themes.THEME_BLUE,
        )

        self.add.button("Play", self.disable)

    # ----------------------------------------------------------------------------------------------
    def display(self):
        """
        Displays the menu.
        """

        self.mainloop(self.wn)
