# --------------------------------------------------------------------------------------------------
# Utility functions.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
import os
import pygame


# --------------------------------------------------------------------------------------------------
def fetch_asset(asset_path):
    """
    Grabs an asset from a path and converts it into something usable by Pygame.

    Args:
        assest_path (path): Location to asset.

    Returns:
        Rendered Pygame asset.
    """

    try:
        surface = pygame.image.load(asset_path)
    except pygame.error as message:
        print(f"Cannot load image: { asset_path }")
        raise SystemExit(message)

    if surface.get_alpha() is not None:
        surface = surface.convert_alpha()
    else:
        surface = surface.convert()

    return surface
