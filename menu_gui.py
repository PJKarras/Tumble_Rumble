import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

BLUE = (106, 150, 181)
WHITE = (255, 255, 255)
right_arrow = pygame.image.load('arrow.png')
right_arrow = pygame.transform.scale(right_arrow, (100, 80))
left_arrow = pygame.transform.flip(right_arrow, True, False)
right_arrowX = 470
right_arrowY = 200
left_arrowX = 230


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


def optionsMenu(screen):

    optionTitle = UIElement(
        center_position=(400, 75),
        font_size=60,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Options'
    )

    returnButton = UIElement(
        center_position=(200, 550),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Return to Main Menu'
    )
    done = False
    while not done:
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if returnButton.rect.collidepoint(pos):
                    done = True

        optionTitle.draw(screen)
        returnButton.update(pygame.mouse.get_pos())
        returnButton.draw(screen)
        pygame.display.flip()


def startMenu(screen):
    how_many_title = UIElement(
        center_position=(400, 100),
        font_size=55,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='How many players?'
    )

    startButton = UIElement(
        center_position=(400, 450),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Start'
    )

    returnButton = UIElement(
        center_position=(200, 550),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Return to Main Menu'
    )
    done = False
    while not done:
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if startButton.rect.collidepoint(pos):
                    done = True
                if returnButton.rect.collidepoint(pos):
                    done = True

        how_many_title.draw(screen)
        screen.blit(right_arrow, (right_arrowX, right_arrowY))
        screen.blit(left_arrow, (left_arrowX, right_arrowY))
        startButton.update(pygame.mouse.get_pos())
        startButton.draw(screen)
        returnButton.update(pygame.mouse.get_pos())
        returnButton.draw(screen)
        pygame.display.flip()


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    gameTitle = UIElement(
        center_position=(400, 75),
        font_size=60,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Tumble Rumble'
    )

    startGame = UIElement(
        center_position=(400, 175),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Start Game'
    )

    optionButton = UIElement(
        center_position=(400, 225),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Options'
    )

    exitGame = UIElement(
        center_position=(400, 275),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Exit Game'
    )
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if exitGame.rect.collidepoint(pos):
                    done = True
                if startGame.rect.collidepoint(pos):
                    startMenu(screen)
                if optionButton.rect.collidepoint(pos):
                    optionsMenu(screen)
        screen.fill(BLUE)

        gameTitle.draw(screen)
        startGame.update(pygame.mouse.get_pos())
        startGame.draw(screen)
        optionButton.update(pygame.mouse.get_pos())
        optionButton.draw(screen)
        exitGame.update(pygame.mouse.get_pos())
        exitGame.draw(screen)
        pygame.display.flip()

main()