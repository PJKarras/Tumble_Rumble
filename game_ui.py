import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect


GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
gui_block = Rect(0, 525, 800, 75)
weapons = pygame.transform.scale(pygame.image.load("assets/Weapons.png"), (240, 80))
weapons_glow = pygame.transform.scale(pygame.image.load("assets/Weapons_glow.png"), (256, 80))
fire = pygame.transform.scale(pygame.image.load("assets/fire.png"), (240, 70))
fire_hover = pygame.transform.scale(pygame.image.load("assets/fire_hover.png"), (240, 70))
items = pygame.transform.scale(pygame.image.load("assets/items.png"), (150, 80))
items_glow = pygame.transform.scale(pygame.image.load("assets/items_glow.png"), (150, 80))
leave = pygame.transform.scale(pygame.image.load("assets/leave.png"), (180, 60))
leave_glow = pygame.transform.scale(pygame.image.load("assets/leave_glow.png"), (180, 60))


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class GuiElement(Sprite):

    def __init__(self, center_position, image, image_glow):
        super().__init__()

        self.mouse_over = False

        default_image = image

        glow_image = image_glow

        self.images = [default_image, glow_image]
        self.rects = [default_image.get_rect(center=center_position),
                      glow_image.get_rect(center=center_position)]

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
    weapon_button = GuiElement(
        center_position=(115, 565),
        image=weapons,
        image_glow=weapons_glow
    )

    fire_button = GuiElement(
        center_position=(500, 565),
        image=fire,
        image_glow=fire_hover
    )

    leave_button = GuiElement(
        center_position=(710, 570),
        image=leave,
        image_glow=leave_glow
    )

    items_button = GuiElement(
        center_position=(305, 570),
        image=items,
        image_glow=items_glow
    )

    button_list = [weapon_button, fire_button, leave_button, items_button]

    done = False
    while not done:
        screen.fill(BLACK)
        pygame.draw.rect(screen, GRAY, gui_block)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()


        #item_button.update(pygame.mouse.get_pos())
        #item_button.draw(screen)
        for i in button_list:
            i.update(pygame.mouse.get_pos())
            i.draw(screen)
        pygame.display.flip()