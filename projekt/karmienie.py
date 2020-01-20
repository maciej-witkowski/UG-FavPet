import pygame
import random
pygame.init()

display_width = 1400
display_height = 750

monster_width = 150
monster_height = 150
object_width = 75
object_height = 75

white = (255, 255, 255)
blue = (0, 119, 204)
blue_light = (145, 226, 245)
blue_dark = (0, 0, 128)

font_small = pygame.font.Font('fonts/orangejuice.ttf', 30)
font_medium = pygame.font.Font('fonts/orangejuice.ttf', 50)
font_big = pygame.font.Font('fonts/orangejuice.ttf', 120)

bite_sound = pygame.mixer.Sound('sounds/bite.wav')
jazz_music = pygame.mixer.Sound('sounds/jazz_musicv2.wav')

HPbar_vertical = pygame.image.load('bars/hpbar_vertical.png')

HPcover = pygame.image.load('bars/white_pallet.png')

HPcover_vert = pygame.image.load('bars/white_pallet_vert.png')

Bar = pygame.image.load('bars/chicken_ia_bar.png')
Bar2 = pygame.image.load('bars/chicken_ac_bar.png')

food1 = pygame.image.load('food_img/tomato.png')
food2 = pygame.image.load('food_img/cucumber.png')
food3 = pygame.image.load('food_img/cabbage.png')
food4 = pygame.image.load('food_img/apple.png')
food5 = pygame.image.load('food_img/orange.png')
food6 = pygame.image.load('food_img/watermelon.png')
food7 = pygame.image.load('food_img/special1.png')
food8 = pygame.image.load('food_img/poo.png')

food = [food1, food2, food3, food4, food5, food6, food7, food8]

screen_choose = pygame.display.set_mode((1000, 600))


def monster(screen, x, y, img):
    screen.blit(img, (x, y))


def which_object(lista):
    count = random.randrange(0, 8)
    if count == 0:
        return lista[0]
    elif count == 1:
        return lista[1]
    elif count == 2:
        return lista[2]
    elif count == 3:
        return lista[3]
    elif count == 4:
        return lista[4]
    elif count == 5:
        return lista[5]
    elif count == 6:
        return lista[6]
    elif count == 7:
        return lista[7]


def objects(screen, x, y, img):
    screen.blit(img, (x, y))


def ate(screen, count):
    text = font_medium.render("Zjedzone: " + str(count), True, blue)
    screen.blit(text, (display_width - 260, 5))


def levels(screen, level):
    text = font_medium.render("Poziom: " + str(level), True, blue)
    screen.blit(text, (5, 5))


def hp(screen, count):
    screen.blit(HPbar_vertical, (5, display_height - 630))
    if count == 1:
        screen.blit(HPcover_vert, (5, 602))
    elif count == 2:
        screen.blit(HPcover_vert, (5, 548))
    elif count == 3:
        screen.blit(HPcover_vert, (5, 494))
    elif count == 4:
        screen.blit(HPcover_vert, (5, 440))
    elif count == 5:
        screen.blit(HPcover_vert, (5, 386))
    elif count == 6:
        screen.blit(HPcover_vert, (5, 332))
    elif count == 7:
        screen.blit(HPcover_vert, (5, 278))
    elif count == 8:
        screen.blit(HPcover_vert, (5, 224))
    elif count == 9:
        screen.blit(HPcover_vert, (5, 170))


def food_bar(screen, count):
    screen.blit(Bar, (display_width - 51, display_height - 655))
    if 4 < count < 10:
        screen.blit(Bar2, (display_width - 51, 645))
        screen.blit(HPcover_vert, (display_width - 51, 700))
    elif 9 < count < 15:
        screen.blit(Bar2, (display_width - 51, 584))
        screen.blit(HPcover_vert, (display_width - 51, 700))
    elif 14 < count < 20:
        screen.blit(Bar2, (display_width - 51, 523))
        screen.blit(HPcover_vert, (display_width - 51, 700))
    elif 19 < count < 25:
        screen.blit(Bar2, (display_width - 51, 462))
        screen.blit(HPcover_vert, (display_width - 51, 700))
    elif 24 < count < 30:
        screen.blit(Bar2, (display_width - 51, 401))
        screen.blit(HPcover_vert, (display_width - 51, 700))
    elif 29 < count < 35:
        screen.blit(Bar2, (display_width - 51, 340))
        screen.blit(HPcover_vert, (display_width - 51, 700))
    elif 34 < count < 40:
        screen.blit(Bar2, (display_width - 51, 279))
        screen.blit(HPcover_vert, (display_width - 51, 700))
    elif 39 < count < 45:
        screen.blit(Bar2, (display_width - 51, 218))
        screen.blit(HPcover_vert, (display_width - 51, 700))
    elif 44 < count < 50:
        screen.blit(Bar2, (display_width - 51, 157))
        screen.blit(HPcover_vert, (display_width - 51, 700))
    elif count > 49:
        screen.blit(Bar2, (display_width - 51, 96))
        screen.blit(HPcover_vert, (display_width - 51, 700))


def music(channel, action, file):
    if action == "play":
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound(file))
    elif action == "stop":
        pygame.mixer.Channel(channel).stop()
