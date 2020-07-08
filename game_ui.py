import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect


GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
gui_block = Rect(0, 470, 800, 130)
#weapons = pygame.image.load("weapon.png")


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb):
        super().__init__()

        self.mouse_over = False

        default_image = create_surface_with_text(text, font_size, text_rgb, bg_rgb)

        highlighted_image = create_surface_with_text(text, font_size * 1.2, text_rgb, bg_rgb)

        self.images = [default_image, highlighted_image]
        self.rects = [default_image.get_rect(center=center_position),
                      highlighted_image.get_rect(center=center_position)]

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)


def start(screen):
    item_button = UIElement(
        center_position=(400, 500),
        font_size=40,
        bg_rgb=GRAY,
        text_rgb=WHITE,
        text='Items'
    )

    done = False
    while not done:
        screen.fill(BLACK)
        pygame.draw.rect(screen, GRAY, gui_block)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        #item_button.update(pygame.mouse.get_pos())
        #item_button.draw(screen)
        pygame.display.flip()