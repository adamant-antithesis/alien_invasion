import pygame.font


class Button:

    def __init__(self, ai_game, msg):
        """Initializes the attributes of the button."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Assigning sizes and properties to buttons.
        self.width, self.height = 180, 100
        self.button_color = (52, 235, 52)
        self.text_color = (206, 227, 237)
        self.font = pygame.font.SysFont(None, 48, bold=True, italic=True)

        # Constructing the button's rect object and aligning it to the center of the screen.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message is created only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Converts msg to a rectangle and aligns the text to the center."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
