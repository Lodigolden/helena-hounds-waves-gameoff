# --------------------------------------------------------------------------------------------------
# The pirate ship component.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
import pygame

# --------------------------------------------------------------------------------------------------
class Ship:
    """
    A class for the ship object.
    """

    # ----------------------------------------------------------------------------------------------
    def __init__(self, game_loop):
        """
        The parameterized constructor sets the ship location and appearance.

        Args:
            game_loop (Game_loop): Reference to the main game loop object.
        """

        self.pos = pygame.Vector2(0, 0)
        self.game_loop = game_loop

    # ----------------------------------------------------------------------------------------------
    def render(self):
        """
        Renders the ship object.
        """

        pygame.draw.circle(self.game_loop.wn, "yellow", self.pos, 40)

        if self.game_loop.keys[pygame.K_w]:
            self.pos.y -= 300 * self.game_loop.dt
        if self.game_loop.keys[pygame.K_s]:
            self.pos.y += 300 * self.game_loop.dt
        if self.game_loop.keys[pygame.K_a]:
            self.pos.x -= 300 * self.game_loop.dt
        if self.game_loop.keys[pygame.K_d]:
            self.pos.x += 300 * self.game_loop.dt
