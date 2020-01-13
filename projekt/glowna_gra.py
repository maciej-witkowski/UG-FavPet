import pygame
import random
from pygame.locals import *

pygame.init()

display_width = 1000
display_height = 600

TITLE_PAGE = pygame.image.load(('screens/pic01.png'))
wybor_postaci = pygame.image.load('screens/CHOOSEv1.png')

monster1 = pygame.image.load('monsters_icons_img/MONSTER1_game.png')
monster2 = pygame.image.load('monsters_icons_img/MONSTER2_game.png')
monster3 = pygame.image.load('monsters_icons_img/MONSTER3_game.png')
monster4 = pygame.image.load('monsters_icons_img/MONSTER4_game.png')
monster5 = pygame.image.load('monsters_icons_img/MONSTER5_game.png')
monster6 = pygame.image.load('monsters_icons_img/MONSTER6_game.png')

monster1_big = pygame.image.load('monsters_img/MONSTER1.png')
monster2_big = pygame.image.load('monsters_img/MONSTER2.png')
monster3_big = pygame.image.load('monsters_img/MONSTER3.png')
monster4_big = pygame.image.load('monsters_img/MONSTER4.png')
monster5_big = pygame.image.load('monsters_img/MONSTER5.png')
monster6_big = pygame.image.load('monsters_img/MONSTER6.png')

packet1 = [monster1, monster1_big]
packet2 = [monster2, monster2_big]
packet3 = [monster3, monster3_big]
packet4 = [monster4, monster4_big]
packet5 = [monster5, monster5_big]
packet6 = [monster6, monster6_big]

packets = [packet1, packet2, packet3, packet4, packet5, packet6]



monsters = {
    monster1 : {
        "name" : "Spiteling",
        "type" : "Water",
        "weight" : "6.9",
        "height" : "0.7"
    },
    monster2: {
        "name": "Vampling",
        "type": "Fire",
        "weight": "13.7",
        "height": "1.3"
    },
    monster3: {
        "name": "Cinder",
        "type": "Ground",
        "weight": "12.9",
        "height": "1.1"
    },
    monster4: {
        "name": "Vextaur",
        "type": "Flying",
        "weight": "5.4",
        "height": "0.9"
    },
    monster5: {
        "name": "Wazow",
        "type": "Fighting",
        "weight": "1.4",
        "height": "1.0"
    },
    monster6: {
        "name": "Swirlip",
        "type": "Fairy",
        "weight": "2.4",
        "height": "0.5"
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
        screen.fill(white)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        for i in range(0, 6, 1):
            if img == packets[i][0]:
                screen.blit(packets[i][1], (0, 0))
        name = font_small.render("Imię zwierzątka:   "+creature["name"], True, blue)
        screen.blit(name, (450, 100))
        type = font_small.render("Typ:   "+creature["type"], True, blue)
        screen.blit(type, (450, 200))
        weight = font_small.render("Waga:   "+creature["weight"]+" kg", True, blue)
        screen.blit(weight, (450, 300))
        height = font_small.render("Wzrost:   "+creature["height"]+" m", True, blue)
        screen.blit(height, (450, 400))
        pygame.display.update()


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
        pygame.display.update()

character = intro()
getInformation(monsters[character], character)
