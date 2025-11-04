# --------------------------------------------------------------------------------------------------
# The pirate ship component.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from core.utils import fetch_asset

import os
import pygame


# --------------------------------------------------------------------------------------------------
class Ship:
    """
    A class for the ship object.
    """

    # ----------------------------------------------------------------------------------------------
    def __init__(self, game_loop, x_pos, y_pos, asset_path):
        """
        The parameterized constructor sets the ship location.

        Args:
            game_loop (Game_loop): Reference to the main game loop object.
            x_pos (int): Ship x-position.
            y_pos (int): Ship y-position.
            assest_path (path): Location to asset.
        """

        self.pos = pygame.Vector2(x_pos, y_pos)
        self.game_loop = game_loop
        self.angle = 0

        self.ship_surface = fetch_asset(asset_path)

    # ----------------------------------------------------------------------------------------------
    def render(self):
        """
        Renders the ship object.
        """

        rotated_ship_surface = pygame.transform.rotate(self.ship_surface, self.angle)
        self.game_loop.wn.blit(rotated_ship_surface, self.pos)

        if self.game_loop.keys[pygame.K_w]:
            self.angle = 0
            self.pos.y -= 300 * self.game_loop.dt
        if self.game_loop.keys[pygame.K_s]:
            self.angle = 180
            self.pos.y += 300 * self.game_loop.dt
        if self.game_loop.keys[pygame.K_a]:
            self.angle = 90
            self.pos.x -= 300 * self.game_loop.dt
        if self.game_loop.keys[pygame.K_d]:
            self.angle = 270
            self.pos.x += 300 * self.game_loop.dt
