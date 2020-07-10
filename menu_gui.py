import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
import game_ui
import test

display_height = 720
display_width = 1280

BLUE = (106, 150, 181)
WHITE = (255, 255, 255)
right_arrow = pygame.image.load('arrow.png')
right_arrow = pygame.transform.scale(right_arrow, (100, 80))
left_arrow = pygame.transform.flip(right_arrow, True, False)
right_arrowX = display_width*.625
right_arrowY = display_height*.33
left_arrowX = display_width*.30


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
        center_position=(display_width/2, display_height*.125),
        font_size=60,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Options'
    )

    returnButton = UIElement(
        center_position=(display_width*.25, display_height*.92),
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
        center_position=(display_width/2, display_height*.125),
        font_size=55,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='How many players?'
    )

    startButton = UIElement(
        center_position=(display_width/2, display_height*.75),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Start'
    )

    returnButton = UIElement(
        center_position=(display_width*.25, display_height*.92),
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
                    startGame(screen)
                    return
                if returnButton.rect.collidepoint(pos):
                    done = True

        how_many_title.draw(screen)
        screen.blit(right_arrow, (int(right_arrowX), int(right_arrowY)))
        screen.blit(left_arrow, (int(left_arrowX), int(right_arrowY)))
        startButton.update(pygame.mouse.get_pos())
        startButton.draw(screen)
        returnButton.update(pygame.mouse.get_pos())
        returnButton.draw(screen)
        pygame.display.flip()


def startGame(screen):
    test.start(screen)


def main():
    pygame.init()

    screen = pygame.display.set_mode((display_width, display_height))

    gameTitle = UIElement(
        center_position=(display_width/2, display_height*.125),
        font_size=60,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Tumble Rumble'
    )

    startGame = UIElement(
        center_position=(display_width/2, display_height*.292),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Start Game'
    )

    optionButton = UIElement(
        center_position=(display_width/2, display_height*.375),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text='Options'
    )

    exitGame = UIElement(
        center_position=(display_width/2, display_height*.458),
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