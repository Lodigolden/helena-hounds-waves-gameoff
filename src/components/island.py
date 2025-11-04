# --------------------------------------------------------------------------------------------------
# The island component.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
import pygame


# --------------------------------------------------------------------------------------------------
class Island:
    """
    A class for the island object.
    """

    # ----------------------------------------------------------------------------------------------
    def __init__(self, game_loop, x_pos, y_pos):
        """
        The parametized constructor sets the island location.

        Args:
            game_loop (Game_loop): Reference to the main game loop object.
            x_pos (int): Ship x-position.
            y_pos (int): Ship y-position.
            assest_path (path): Location to asset.
        """

        self.pos = pygame.Vector2(x_pos, y_pos)
        self.game_loop = game_loop
        self.is_home = False
        self.island_color = "white"

    # ----------------------------------------------------------------------------------------------
    def render(self):
        """
        Renders the island object.
        """

        pygame.draw.circle(self.game_loop.wn, self.island_color, self.pos, 40)


# --------------------------------------------------------------------------------------------------
class Home_island(Island):
    """
    A class for the home island.
    """

    # ----------------------------------------------------------------------------------------------
    def __init__(self, game_loop, x_pos, y_pos):
        """
        The parameterized constructor sets the home island location.

        Args:
            game_loop (Game_loop): Reference to the main game loop object.
            x_pos (int): Ship x-position.
            y_pos (int): Ship y-position.
        """

        super().__init__(game_loop, x_pos, y_pos)
        self.is_home = True
        self.island_color = "yellow"
