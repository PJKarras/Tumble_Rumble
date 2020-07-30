import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

display_height = 720
display_width = 1280

GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKYBLUE = (100, 190, 255)
gui_block = Rect(0, 525, 800, 75)

weapons = pygame.image.load("assets/Weapons.png")
weapons_glow = pygame.image.load("assets/Weapons_glow.png")
fire = pygame.image.load("assets/fire.png")
fire_hover = pygame.image.load("assets/fire_hover.png")
items = pygame.image.load("assets/items.png")
items_glow = pygame.image.load("assets/items_glow.png")
leave = pygame.image.load("assets/leave.png")
leave_glow = pygame.image.load("assets/leave_glow.png")
missile = pygame.image.load("assets/missile.png")
missile_glow = pygame.image.load("assets/missile_glow.png")
missileX2 = pygame.image.load("assets/missileX2.png")
missileX2_glow = pygame.image.load("assets/missileX2_glow.png")
missileX3 = pygame.image.load("assets/missileX3.png")
missileX3_glow = pygame.image.load("assets/missileX3_glow.png")
atomic = pygame.image.load("assets/atomic.png")
atomic_glow = pygame.image.load("assets/atomic_glow.png")
weapon_item_holder = pygame.image.load("assets/weapon_item_holder.png")
wrench = pygame.image.load("assets/wrench.png")
wrench_glow = pygame.image.load("assets/wrench_glow.png")
jetpack = pygame.image.load("assets/jetpack.png")
jetpack_glow = pygame.image.load("assets/jetpack_glow.png")
shield = pygame.image.load("assets/shield.png")
shield_glow = pygame.image.load("assets/shield_glow.png")
move_on = pygame.image.load("assets/move_on.png")
move_off = pygame.image.load("assets/move_off.png")
right_arrow = pygame.image.load('arrow.png')
right_arrow = pygame.transform.scale(right_arrow, (100, 80))
left_arrow = pygame.transform.flip(right_arrow, True, False)
aim = pygame.image.load('assets/aim.png')
aim_glow = pygame.image.load('assets/aim_glow.png')
reticle = pygame.image.load('assets/reticle.png')


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


weapon_button = GuiElement(
    center_position=(display_width*.40, display_height*.03),
    image=weapons,
    image_glow=weapons_glow
)

fire_button = GuiElement(
    center_position=(display_width*.875, display_height*.05),
    image=fire,
    image_glow=fire_hover
)

leave_button = GuiElement(
    center_position=(display_width*.056, display_height*.03),
    image=leave,
    image_glow=leave_glow
)

items_button = GuiElement(
    center_position=(display_width*.55, display_height*.03),
    image=items,
    image_glow=items_glow
)

weapons_holder = GuiElement(
    center_position=(display_width * .40, (display_height * .03)+90),
    image=weapon_item_holder,
    image_glow=weapon_item_holder
)

items_holder = GuiElement(
    center_position=(display_width * .55, (display_height * .03) + 90),
    image=weapon_item_holder,
    image_glow=weapon_item_holder
)

move_on_button = GuiElement(
    center_position=(display_width*.15, display_height*.03),
    image=move_on,
    image_glow=move_on
)

move_off_button = GuiElement(
    center_position=(display_width * .15, display_height*.03),
    image=move_off,
    image_glow=move_off
)

missile1 = GuiElement(
    center_position=(display_width * .365, (display_height * .03)+50),
    image=missile,
    image_glow=missile_glow
)

missile2 = GuiElement(
    center_position=(display_width * .435, (display_height * .03)+50),
    image=missileX2,
    image_glow=missileX2_glow
)

missile3 = GuiElement(
    center_position=(display_width * .365, (display_height * .03)+120),
    image=missileX3,
    image_glow=missileX3_glow
)

atomic_icon = GuiElement(
    center_position=(display_width * .435, (display_height * .03)+120),
    image=atomic,
    image_glow=atomic_glow
)

wrench_icon = GuiElement(
    center_position=(display_width * .515, (display_height * .03)+52),
    image=wrench,
    image_glow=wrench_glow
)

shield_icon = GuiElement(
    center_position=(display_width * .585, (display_height * .03)+52),
    image=shield,
    image_glow=shield_glow
)

jetpack_icon = GuiElement(
    center_position=(display_width * .515, (display_height * .03)+120),
    image=jetpack,
    image_glow=jetpack_glow
)

left_arrow_button = GuiElement(
    center_position=(display_width * .40, display_height * .33),
    image=left_arrow,
    image_glow=left_arrow
)

right_arrow_button = GuiElement(
    center_position=(display_width * .60, display_height * .33),
    image=right_arrow,
    image_glow=right_arrow
)

aim_button = GuiElement(
    center_position=(display_width*.875, display_height*.05),
    image=aim,
    image_glow=aim_glow
)


button_list = [weapon_button, leave_button, items_button]
weapons_list = [missile1, missile2, missile3, atomic_icon]
item_list = [wrench_icon, shield_icon, jetpack_icon]


# def start(screen):
#
#     weapon_menu_open = False
#     item_menu_open = False
#     done = False
#     while not done:
#         screen.fill(BLACK)
#         if weapon_menu_open:
#             weapons_holder.draw(screen)
#         if item_menu_open:
#             items_holder.draw(screen)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 pos = pygame.mouse.get_pos()
#                 if leave_button.rect.collidepoint(pos):
#                     return
#                 if weapon_button.rect.collidepoint(pos):
#                     if weapon_menu_open:
#                         weapon_menu_open = False
#                     else:
#                         weapon_menu_open = True
#                 if items_button.rect.collidepoint(pos):
#                     if item_menu_open:
#                         item_menu_open = False
#                     else:
#                         item_menu_open = True
#
#
#         #item_button.update(pygame.mouse.get_pos())
#         #item_button.draw(screen)
#         for i in button_list:
#             i.update(pygame.mouse.get_pos())
#             i.draw(screen)
#         pygame.display.flip()