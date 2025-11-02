# --------------------------------------------------------------------------------------------------
# Game menu.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
import pygame
import pygame_menu


# --------------------------------------------------------------------------------------------------
class Menu:
    """
    A menu wrapper for the game.
    """

    # ----------------------------------------------------------------------------------------------
    def __init__(self, display_size, wn):
        """
        Default constructor.

        Args:
            display_size (tuple of ints): Size of the game window.
            wn (Object): The rendered window.
        """

        self.wn = wn

        self.menu = pygame_menu.Menu(
            "Welcome",
            display_size[0],
            display_size[1],
            theme=pygame_menu.themes.THEME_BLUE,
        )

        self.menu.add.text_input("Name: ", default="John Doe")

    # ----------------------------------------------------------------------------------------------
    def display(self):
        """
        Displays the menu.
        """

        self.menu.mainloop(self.wn)
