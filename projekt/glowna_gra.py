import pygame
import random
import karmienie
import bronienie
from pygame.locals import *

pygame.init()

display_width = 1000
display_height = 600

TITLE_PAGE = pygame.image.load(('screens/pic01.png'))
wybor_postaci = pygame.image.load('screens/CHOOSEv1.png')
menu_glowne = pygame.image.load('screens/szablon.png')

monster1 = pygame.image.load('monsters_icons_img/MONSTER1_game.png')
monster2 = pygame.image.load('monsters_icons_img/MONSTER2_game.png')
monster3 = pygame.image.load('monsters_icons_img/MONSTER3_game.png')
monster4 = pygame.image.load('monsters_icons_img/MONSTER4_game.png')
monster5 = pygame.image.load('monsters_icons_img/MONSTER5_game.png')
monster6 = pygame.image.load('monsters_icons_img/MONSTER6_game.png')

monster1_big = pygame.image.load('monsters_img/MONSTER1_edit.png')
monster2_big = pygame.image.load('monsters_img/MONSTER2_edit.png')
monster3_big = pygame.image.load('monsters_img/MONSTER3_edit.png')
monster4_big = pygame.image.load('monsters_img/MONSTER4_edit.png')
monster5_big = pygame.image.load('monsters_img/MONSTER5_edit.png')
monster6_big = pygame.image.load('monsters_img/MONSTER6_edit.png')

packet1 = [monster1, monster1_big]
packet2 = [monster2, monster2_big]
packet3 = [monster3, monster3_big]
packet4 = [monster4, monster4_big]
packet5 = [monster5, monster5_big]
packet6 = [monster6, monster6_big]

packets = [packet1, packet2, packet3, packet4, packet5, packet6]



monsters = {
    monster1 : {
        "name": "Spiteling",
        "type": "Water",
        "weight": 6.9,
        "height": 0.7
    },
    monster2: {
        "name": "Vampling",
        "type": "Fire",
        "weight": 13.7,
        "height": 1.3
    },
    monster3: {
        "name": "Cinder",
        "type": "Ground",
        "weight": 12.9,
        "height": 1.1
    },
    monster4: {
        "name": "Vextaur",
        "type": "Flying",
        "weight": 5.4,
        "height": 0.9
    },
    monster5: {
        "name": "Wazow",
        "type": "Fighting",
        "weight": 1.4,
        "height": 1.0
    },
    monster6: {
        "name": "Swirlip",
        "type": "Fairy",
        "weight": 2.4,
        "height": 0.5
    }
}

font_small = pygame.font.Font('fonts/orangejuice.ttf', 30)
font_medium = pygame.font.Font('fonts/orangejuice.ttf', 50)
font_big = pygame.font.Font('fonts/orangejuice.ttf', 120)

white = (255, 255, 255)
blue = (0, 119, 204)
blue_light = (145, 226, 245)
blue_dark = (0, 0, 128)

screen = pygame.display.set_mode((display_width, display_height))
screen.blit(TITLE_PAGE, (0,0))
pygame.display.set_caption("FavPet")

def button(text, x, y, w, h, ia_c, a_c, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, a_c, (x, y, w, h))
        if click[0] == 1 and action is not None:
            if action == "karmienie":
                karmienie.main(character)
            elif action == "obrona":
                bronienie.main(character)
    else:
        pygame.draw.rect(screen, ia_c, (x, y, w, h))
    message_display(text, font_small, (x+(w//2)) * 2, (y+(h//2)) * 2, white)

def message_display(text, size, place_width, place_height, tone):
    text_surface = size.render(text, True, tone)
    text_rect = text_surface.get_rect()
    text_rect.center = ((place_width//2), (place_height//2))
    screen.blit(text_surface, text_rect)
    pygame.display.update()

def which_monster():
    while True:
        screen.blit(wybor_postaci, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    return packets[0][0]
                elif event.key == K_2:
                    return packets[1][0]
                elif event.key == K_3:
                    return packets[2][0]
                elif event.key == K_4:
                    return packets[3][0]
                elif event.key == K_5:
                    return packets[4][0]
                elif event.key == K_6:
                    return packets[5][0]


def getInformation(creature, img):
    while True:
        screen.blit(menu_glowne, (0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        for i in range(0, 6, 1):
            if img == packets[i][0]:
                screen.blit(packets[i][1], (35, 80))
        statystyki = font_medium.render("Statystyki:", True, blue_dark)
        screen.blit(statystyki, (600, 20))
        name = font_small.render("Imię zwierzątka:   "+str(creature["name"]), True, blue_dark)
        screen.blit(name, (450, 100))
        type = font_small.render("Typ:   "+str(creature["type"]), True, blue_dark)
        screen.blit(type, (450, 150))
        weight = font_small.render("Waga:   "+str(creature["weight"])+" kg", True, blue_dark)
        screen.blit(weight, (450, 200))
        height = font_small.render("Wzrost:   "+str(creature["height"])+" m", True, blue_dark)
        screen.blit(height, (450, 250))
        aktywnosci = font_medium.render("Aktywności: ", True, blue_dark)
        screen.blit(aktywnosci, (590, 340))
        button("Karmienie", 450, 450, 200, 50, blue, blue_dark, "karmienie")
        button("Obrona", 750, 450, 200, 50, blue, blue_dark, "obrona")


def intro():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    monster = which_monster()
                    return monster
        screen.blit(TITLE_PAGE, (0,0))
        message_display("Kliknij SPACE, aby kontynuować...", font_medium, 1080, 730, blue_dark)
        pygame.display.update()

character = intro()
getInformation(monsters[character], character)