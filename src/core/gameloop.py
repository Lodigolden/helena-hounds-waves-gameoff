# --------------------------------------------------------------------------------------------------
# Main Gameloop object.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from components.menu import Menu
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

        self.ball_pos = pygame.Vector2(self.wn.get_width() / 2, self.wn.get_height() / 2)

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

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

        self.wn.fill("purple")

        pygame.draw.circle(self.wn, "red", self.ball_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.ball_pos.y -= 300 * self.dt
        if keys[pygame.K_s]:
            self.ball_pos.y += 300 * self.dt
        if keys[pygame.K_a]:
            self.ball_pos.x -= 300 * self.dt
        if keys[pygame.K_d]:
            self.ball_pos.x += 300 * self.dt
