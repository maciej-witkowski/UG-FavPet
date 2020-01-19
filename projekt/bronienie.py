import pygame
import random
from pygame.locals import *
pygame.init()

display_width = 1400
display_height = 750

monster_width = 150
monster_height = 150

enemy_width = 75
enemy_height = 75

white = (255, 255, 255)
blue = (0, 119, 204)
blue_light = (145, 226, 245)
blue_dark = (0, 0, 128)

font_small = pygame.font.Font('fonts/orangejuice.ttf', 30)
font_medium = pygame.font.Font('fonts/orangejuice.ttf', 50)
font_big = pygame.font.Font('fonts/orangejuice.ttf', 120)

main_music = pygame.mixer.Sound('sounds/music_defend.wav')
kill_sound = pygame.mixer.Sound('sounds/kill_sound.wav')
hurt_sound = pygame.mixer.Sound('sounds/oof.wav')

wybor_postaci = pygame.image.load('screens/CHOOSEv1.png')

hp_bar = pygame.image.load('bars/hpbar_horizontal.png')
hp_cover = pygame.image.load('bars/white_pallet.png')

enemy1 = pygame.image.load('enemy_img/enemy1icon.png')
enemy2 = pygame.image.load('enemy_img/enemy2icon.png')
enemy3 = pygame.image.load('enemy_img/enemy3icon.png')
enemy4 = pygame.image.load('enemy_img/enemy5icon.png')

enemies = [enemy1, enemy2, enemy3, enemy4]

monster1 = pygame.image.load('monsters_icons_img/MONSTER1_game.png')
monster2 = pygame.image.load('monsters_icons_img/MONSTER2_game.png')
monster3 = pygame.image.load('monsters_icons_img/MONSTER3_game.png')
monster4 = pygame.image.load('monsters_icons_img/MONSTER4_game.png')
monster5 = pygame.image.load('monsters_icons_img/MONSTER5_game.png')
monster6 = pygame.image.load('monsters_icons_img/MONSTER6_game.png')

choose_screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("FavPet: OBRONA")

clock = pygame.time.Clock()


def monster(screen, x, y, img):
    screen.blit(img, (x, y))


def spawn_enemy(screen, place, x, y):
    if place == 0:
        screen.blit(enemies[2], (x, y))
    elif place == 1:
        screen.blit(enemies[1], (x, y))
    elif place == 2:
        screen.blit(enemies[0], (x, y))
    elif place == 3:
        screen.blit(enemies[3], (x, y))


def reset_enemy_pos(pos_enemies, which):
    if which == 0:
        pos_enemies[0][0] = 0
        pos_enemies[0][1] = 0
    elif which == 1:
        pos_enemies[1][0] = 1325
        pos_enemies[1][1] = 0
    elif which == 2:
        pos_enemies[2][0] = 1325
        pos_enemies[2][1] = 675
    elif which == 3:
        pos_enemies[3][0] = 0
        pos_enemies[3][1] = 675


def kill_count(screen, count):
    text = font_medium.render("Zestrzelone: "+str(count), True, blue)
    screen.blit(text, (display_width // 2, 700))


def hp(screen, count):
    screen.blit(hp_bar, (435, 10))
    if count == 1:
        screen.blit(hp_cover, (919, 0))
    elif count == 2:
        screen.blit(hp_cover, (865, 0))
    elif count == 3:
        screen.blit(hp_cover, (811, 0))
    elif count == 4:
        screen.blit(hp_cover, (757, 0))
    elif count == 5:
        screen.blit(hp_cover, (703, 0))
    elif count == 6:
        screen.blit(hp_cover, (649, 0))
    elif count == 7:
        screen.blit(hp_cover, (595, 0))
    elif count == 8:
        screen.blit(hp_cover, (541, 0))
    elif count == 9:
        screen.blit(hp_cover, (487, 0))


def levels(screen, count):
    text = font_medium.render("Poziom: "+str(count), True, blue)
    screen.blit(text, (display_width // 4 + 50, 700))


def set_enemy_speed(level):
    if level == 1:
        x = random.randrange(2, 5)
        if x % 2 == 1:
            x += 1
        y = x // 2
        return x, y
    elif level == 2:
        x = random.randrange(6, 9)
        if x % 2 == 1:
            x += 1
        y = x // 2
        return x, y
    elif level == 3:
        x = random.randrange(9, 12)
        if x % 2 == 1:
            x += 1
        y = x // 2
        return x, y
    elif level == 4:
        x = random.randrange(12, 15)
        if x % 2 == 1:
            x += 1
        y = x // 2
        return x, y
    elif level == 5:
        x = random.randrange(15, 19)
        if x % 2 == 1:
            x += 1
        y = x // 2
        return x, y


def message_display(screen, text, size, place_width, place_height, tone):
    text_surface = size.render(text, True, tone)
    text_rect = text_surface.get_rect()
    text_rect.center = ((place_width//2), (place_height//2))
    screen.blit(text_surface, text_rect)
    pygame.display.update()


def button(screen, img, text, x, y, w, h, ia_c, a_c, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, a_c, (x, y, w, h))
        if click[0] == 1 and action is not None:
            if action == "main":
                main(img)
            else:
                action()
    else:
        pygame.draw.rect(screen, ia_c, (x, y, w, h))
    message_display(screen, text, font_small, (x+(w//2)) * 2, (y+(h//2)) * 2, white)


def music(channel, action, file):
    if action == "play":
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound(file))
    elif action == "stop":
        pygame.mixer.Channel(channel).stop()


def unpaused():
    global pause
    music(0, "play", main_music)
    pause = False


def paused(screen, img):
    while pause:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        music(0, "stop", main_music)
        message_display(screen, "Pauza...", font_big, display_width, display_height - 200, blue)
        button(screen, img, "Kontynuuj", 350, 550, 300, 50, blue, blue_light, unpaused)
        button(screen, img, "Zakończ.", 750, 550, 300, 50, blue, blue_light, quitgame)


def game_over(screen, img, kill, level):
    music(0, "stop", main_music)
    screen.fill(white)
    message_display(screen, "PRZEGRAŁEŚ :(", font_big, display_width, display_height, blue)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        button(screen, img, "Zagraj ponownie!", 350, 550, 300, 50, blue, blue_light, "main")
        button(screen, img, "Zakończ.", 750, 550, 300, 50, blue, blue_light, quitgame)
        message_display(screen, "Twoje statystyki ", font_medium, display_width, int(display_height // 4), blue_dark)
        message_display(screen, "Zestrzelone: "+str(kill), font_medium, int(display_width*1/3), display_height//2,
                        blue_dark)
        text = font_medium.render("Poziom: " + str(level), True, blue_dark)
        screen.blit(text, (1100, 165))


def quitgame():
    pygame.quit()
    quit()


def main(img):
    """ USTAWIENIE DO POPRAWNEGO DZIAŁA FUNKCJI PAUZY """
    global pause

    screen_main = pygame.display.set_mode((display_width, display_height))

    ''' ROZPOCZĘCIE GRANIA MUZYKI '''
    music(0, "play", main_music)

    ''' DEFINIOWANIE POZYCJI MONSTERA '''
    x_monster = 625
    y_monster = 300

    ''' DEFINIOWANIE POZYCJI WROGÓW '''
    pos_enemies = [[0, 0], [1325, 0], [1325, 675], [0, 675]]

    ''' DEFINIOWANIE PRĘDKOŚCI WROGÓW '''
    x_change_e = 2
    y_change_e = 1

    ''' DEFINIOWANIE STATYSTYK W GRZE '''
    kill = 0
    hit = 0
    level = 1

    ''' DEFINIOWANIE POCZĄTKOWEJ POZYCJI WROGA'''
    enemy = random.randrange(0, 4)

    while True:
        ''' STAŁE POZYSKIWANIE DANYCH NA TEMAT DZIAŁANIA MYSZKI '''
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        ''' EVENTY W PYGAME '''
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_p:
                    pause = True
                    paused(screen_main, img)

        ''' PRZYGOTOWANIE EKRANU '''
        screen_main.fill(white)
        monster(screen_main, x_monster, y_monster, img)
        kill_count(screen_main, kill)
        hp(screen_main, hit)
        levels(screen_main, level)
        spawn_enemy(screen_main, enemy, pos_enemies[enemy][0], pos_enemies[enemy][1])

        ''' ZMIANA POZYCJI WROGÓW '''
        if enemy == 0:
            pos_enemies[0][0] += x_change_e
            pos_enemies[0][1] += y_change_e
        elif enemy == 1:
            pos_enemies[1][0] -= x_change_e
            pos_enemies[1][1] += y_change_e
        elif enemy == 2:
            pos_enemies[2][0] -= x_change_e
            pos_enemies[2][1] -= y_change_e
        elif enemy == 3:
            pos_enemies[3][0] += x_change_e
            pos_enemies[3][1] -= y_change_e

        ''' ZDERZENIE WROGA Z POTWORKIEM I WSZYSTKIE AKCJE Z TYM ZWIĄZANE, CZYLI:
            - RESETOWANIE POZYCI PO ZABÓJSTWIE,
            - LOSOWANIE POZYCJI KOLEJNEGO WROGA,
            - ZMIEJSZANIE ILOŚCI ŻYĆ,
            - LOSOWANIE PRĘDKOŚCI PRZECIWNIKA,
            - ZARZĄDZANIE DŹWIEKAMI '''
        if (pos_enemies[0][0] + enemy_width > x_monster) and (pos_enemies[0][1] + enemy_height > y_monster):
            music(2, "play", hurt_sound)
            reset_enemy_pos(pos_enemies, 0)
            enemy = random.randrange(0, 4)
            hit += 1
            x_change_e, y_change_e = set_enemy_speed(1)

        elif (pos_enemies[1][0] < x_monster + monster_width) and (pos_enemies[1][1] + enemy_height > y_monster):
            music(2, "play", hurt_sound)
            reset_enemy_pos(pos_enemies, 1)
            enemy = random.randrange(0, 4)
            hit += 1
            x_change_e, y_change_e = set_enemy_speed(1)

        elif (pos_enemies[2][0] < x_monster + monster_width) and (pos_enemies[2][1] < y_monster + monster_height):
            music(2, "play", hurt_sound)
            reset_enemy_pos(pos_enemies, 2)
            enemy = random.randrange(0, 4)
            hit += 1
            x_change_e, y_change_e = set_enemy_speed(1)

        elif (pos_enemies[3][0] + enemy_width > x_monster) and (pos_enemies[3][1] < y_monster + monster_height):
            music(2, "play", hurt_sound)
            reset_enemy_pos(pos_enemies, 3)
            enemy = random.randrange(0, 4)
            hit += 1
            x_change_e, y_change_e = set_enemy_speed(1)

        ''' ZABIJANIE POTWORÓW I WSZYSTKIE AKCJI Z TYM ZWIĄZANE, CZYLI:
            - RESETOWANIE POZYCI PO ZABÓJSTWIE,
            - LOSOWANIE POZYCJI KOLEJNEGO WROGA,
            - ZWIĘKSZANIE LICZNIKA ZABÓJSTW,
            - LOSOWANIE PRĘDKOŚCI PRZECIWNIKA,
            - ZARZĄDZANIE DŹWIEKAMI '''
        if pos_enemies[0][0] + enemy_width > mouse[0] > pos_enemies[0][0] and \
                pos_enemies[0][1] + enemy_height > mouse[1] > pos_enemies[0][1]:
            if click[0] == 1:
                reset_enemy_pos(pos_enemies, 0)
                enemy = random.randrange(0, 4)
                kill += 1
                x_change_e, y_change_e = set_enemy_speed(1)
                if kill % 2 == 0:
                    music(1, "play", kill_sound)

        elif pos_enemies[1][0] + enemy_width > mouse[0] > pos_enemies[1][0] and\
                pos_enemies[1][1] + enemy_height > mouse[1] > pos_enemies[1][1]:
            if click[0] == 1:
                reset_enemy_pos(pos_enemies, 1)
                enemy = random.randrange(0, 4)
                kill += 1
                x_change_e, y_change_e = set_enemy_speed(1)
                if kill % 2 == 0:
                    music(1, "play", kill_sound)

        elif pos_enemies[2][0] + enemy_width > mouse[0] > pos_enemies[2][0] and\
                pos_enemies[2][1] + enemy_height > mouse[1] > pos_enemies[2][1]:
            if click[0] == 1:
                reset_enemy_pos(pos_enemies, 2)
                enemy = random.randrange(0, 4)
                kill += 1
                x_change_e, y_change_e = set_enemy_speed(1)
                if kill % 2 == 0:
                    music(1, "play", kill_sound)

        elif pos_enemies[3][0] + enemy_width > mouse[0] > pos_enemies[3][0] and\
                pos_enemies[3][1] + enemy_height > mouse[1] > pos_enemies[3][1]:
            if click[0] == 1:
                reset_enemy_pos(pos_enemies, 3)
                enemy = random.randrange(0, 4)
                kill += 1
                x_change_e, y_change_e = set_enemy_speed(1)
                if kill % 2 == 0:
                    music(1, "play", kill_sound)

        ''' ZWIĘKSZANIE TRUDNOŚCI GRY '''
        if kill > 9:
            x_change_e, y_change_e = set_enemy_speed(2)
            level = 2
        if kill > 19:
            x_change_e, y_change_e = set_enemy_speed(3)
            level = 3
        if kill > 29:
            x_change_e, y_change_e = set_enemy_speed(4)
            level = 4
        # POZIOM DLA PROSÓW ;)
        if kill > 99:
            x_change_e, y_change_e = set_enemy_speed(5)
            level = 9000

        ''' GDY WYCZERPIEMY LIMIT ŻYĆ GRA SIĘ KOŃCZY '''
        if hit > 9:
            game_over(screen_main, img, kill, level)

        pygame.display.update()
        clock.tick(60)


pause = False
