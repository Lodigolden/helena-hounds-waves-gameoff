# --------------------------------------------------------------------------------------------------
# The pirate component.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
import pygame


# --------------------------------------------------------------------------------------------------
class Pirate:
    """
    A class for the pirate object.
    """

    # ----------------------------------------------------------------------------------------------
    def __init__(self, game_loop, x_pos, y_pos):
        """
        The parameterized constructor sets the pirate location.

        Args:
            game_loop (Game_loop): Reference to the main game loop object.
            x_pos (int): Ship x-position.
            y_pos (int): Ship y-position.
        """

        self.pos = pygame.Vector2(x_pos, y_pos)
        self.game_loop = game_loop

    # ----------------------------------------------------------------------------------------------
    def render(self):
        """
        Renders the pirate object.
        """

        pygame.draw.circle(self.game_loop.wn, "purple", self.pos, 40)

# --------------------------------------------------------------------------------------------------
class Player(Pirate):
    """
    A class for the player object.
    """

    # ----------------------------------------------------------------------------------------------
    def __init__(self, game_loop, x_pos, y_pos):
        """
        The parameterized constructor sets the pirate location.

        Args:
            game_loop (Game_loop): Reference to the main game loop object.
            x_pos (int): Ship x-position.
            y_pos (int): Ship y-position.
        """

        super().__init__(game_loop, x_pos, y_pos)

    # ----------------------------------------------------------------------------------------------
    def render(self):
        super().render()

        if self.game_loop.keys[pygame.K_a]:
            self.pos.x -= 300 * self.game_loop.dt
        if self.game_loop.keys[pygame.K_d]:
            self.pos.x += 300 * self.game_loop.dt
