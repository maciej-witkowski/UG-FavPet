import pygame
import random
from pygame.locals import *

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

wybor_postaci = pygame.image.load('screens/CHOOSEv1.png')

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

food = (food1, food2, food3, food4, food5, food6, food7, food8)

monster1 = pygame.image.load('monsters_icons_img/MONSTER1_game.png')
monster2 = pygame.image.load('monsters_icons_img/MONSTER2_game.png')
monster3 = pygame.image.load('monsters_icons_img/MONSTER3_game.png')
monster4 = pygame.image.load('monsters_icons_img/MONSTER4_game.png')
monster5 = pygame.image.load('monsters_icons_img/MONSTER5_game.png')
monster6 = pygame.image.load('monsters_icons_img/MONSTER6_game.png')

screen_choose = pygame.display.set_mode((1000, 600))

pygame.display.set_caption("FavPet: KARMIENIE")
clock = pygame.time.Clock()


def which_monster():
    while True:
        screen_choose.blit(wybor_postaci, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    return monster1
                elif event.key == K_2:
                    return monster2
                elif event.key == K_3:
                    return monster3
                elif event.key == K_4:
                    return monster4
                elif event.key == K_5:
                    return monster5
                elif event.key == K_6:
                    return monster6


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


def message_display(screen, text, size, place_width, place_height, tone):
    text_surface = size.render(text, True, tone)
    text_rect = text_surface.get_rect()
    text_rect.center = ((place_width // 2), (place_height // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.update()


def button(screen, text, x, y, w, h, ia_c, a_c, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, a_c, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, ia_c, (x, y, w, h))
    message_display(screen, text, font_small, (x + (w // 2)) * 2, (y + (h // 2)) * 2, white)


def game_over(screen, count, level):
    music(0, "stop", jazz_music)
    screen.fill(white)
    message_display(screen, "PRZEGRAŁEŚ :(", font_big, display_width, display_height, blue)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        button(screen, "Zagraj ponownie!", 350, 550, 300, 50, blue, blue_light, main)
        button(screen, "Zakończ.", 750, 550, 300, 50, blue, blue_light, quitgame)
        message_display(screen, "Twoje statystyki: ", font_medium, display_width, int(display_height // 4), blue_dark)
        message_display(screen, "Zjedzone: " + str(count), font_medium, int(display_width * 1 / 3), display_height // 2,
                        blue_dark)
        text = font_medium.render("Poziom: " + str(level), True, blue_dark)
        screen.blit(text, (1050, 165))
        pygame.display.update()


def unpaused():
    music(0, "play", jazz_music)
    global pause
    pause = False


def paused(screen):
    while pause:
        music(0, "stop", jazz_music)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        message_display(screen, "Pauza...", font_big, display_width, display_height, blue)
        button(screen, "Kontynuuj", 350, 550, 300, 50, blue, blue_light, unpaused)
        button(screen, "Zakończ.", 750, 550, 300, 50, blue, blue_light, quitgame)
        pygame.display.update()


def play_or_end(screen):
    while pause:
        music(0, "stop", jazz_music)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        message_display(screen, "Nakarmiłeś FavPeta!", font_big, display_width, display_height // 2, blue)
        message_display(screen, "Czy chcesz dalej kontynuować grę?", font_medium, display_width, display_height, blue_dark)
        button(screen, "Kontynuuj", 350, 550, 300, 50, blue, blue_light, unpaused)
        button(screen, "Zakończ.", 750, 550, 300, 50, blue, blue_light, quitgame)
        pygame.display.update()


def quitgame():
    pygame.quit()
    quit()


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


def main(img):
    global pause
    pause = False

    screen_main = pygame.display.set_mode((display_width, display_height))

    music(0, "play", jazz_music)

    x_monster = int(display_width * 0.43)
    y_monster = int(display_height * 0.80)

    x_change = 0

    object_startx = random.randrange(0 + 55, display_width - object_width - 51)
    object_starty = -display_height
    object_speed = 4
    objectimg = which_object(food)

    catched = 0
    missed = 0
    level = 1

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_a:
                    x_change = -10
                elif event.key == K_d:
                    x_change = 10
                elif event.key == K_p:
                    pause = True
                    paused(screen_main)
            if event.type == KEYUP:
                if event.key == K_a or event.key == K_d:
                    x_change = 0

        screen_main.fill(white)

        monster(screen_main, x_monster, y_monster, img)
        objects(screen_main, object_startx, object_starty, objectimg)

        levels(screen_main, level)
        hp(screen_main, missed)
        food_bar(screen_main, catched)
        ate(screen_main, catched)

        object_starty += object_speed
        x_monster += x_change

        if x_monster > display_width - monster_width - 51 or x_monster < 0 + 55:
            x_monster -= x_change

        if object_starty > display_height - object_height:
            if objectimg != food[6] and objectimg != food[7]:
                missed += 1
            objectimg = which_object(food)
            object_starty = 0
            object_startx = random.randrange(0 + 55, display_width - object_width - 51)

        if object_starty + object_height > y_monster:
            if x_monster + monster_width > object_startx and x_monster < object_startx + object_width:
                music(1, "play", bite_sound)
                if objectimg == food[6]:
                    missed -= 1
                elif objectimg == food[7]:
                    missed += 1
                else:
                    catched += 1
                if catched % 5 == 0:
                    if objectimg != food[6] and objectimg != food[7]:
                        level += 1
                        object_speed += 1
                objectimg = which_object(food)
                object_starty = 0
                object_startx = random.randrange(0 + 55, display_width - object_width - 51)
                if catched == 50:
                    pause = True
                    play_or_end(screen_main)

        if missed < 0:
            missed = 0

        if missed > 9:
            game_over(screen_main, catched, level)

        pygame.display.update()
        clock.tick(60)



# quitgame()
