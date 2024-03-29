import pygame
import random
import karmienie
import bronienie
from pygame.locals import *

pygame.init()

display_width = 1000
display_height = 600

display_width_game = 1400
display_height_game = 750

intro_screen = pygame.image.load('screens/pic01.png')
wybor_postaci = pygame.image.load('screens/CHOOSEv1.png')
menu_glowne = pygame.image.load('screens/szablon.png')

monsters = []

for i in range(1, 7, 1):
    pic = pygame.image.load('monsters_icons_img/MONSTER'+str(i)+'_game.png')
    monsters.append(pic)

# monster1 = pygame.image.load('monsters_icons_img/MONSTER1_game.png')
# monster2 = pygame.image.load('monsters_icons_img/MONSTER2_game.png')
# monster3 = pygame.image.load('monsters_icons_img/MONSTER3_game.png')
# monster4 = pygame.image.load('monsters_icons_img/MONSTER4_game.png')
# monster5 = pygame.image.load('monsters_icons_img/MONSTER5_game.png')
# monster6 = pygame.image.load('monsters_icons_img/MONSTER6_game.png')

monsters_big = []

for i in range(1, 7, 1):
    pic_big = pygame.image.load('monsters_img/MONSTER'+str(i)+'_edit.png')
    monsters_big.append(pic_big)

# monster_big1 = pygame.image.load('monsters_img/MONSTER1_edit.png')
# monster_big2 = pygame.image.load('monsters_img/MONSTER2_edit.png')
# monster_big3 = pygame.image.load('monsters_img/MONSTER3_edit.png')
# monster_big4 = pygame.image.load('monsters_img/MONSTER4_edit.png')
# monster_big5 = pygame.image.load('monsters_img/MONSTER5_edit.png')
# monster_big6 = pygame.image.load('monsters_img/MONSTER6_edit.png')

packet1 = [monsters[0], monsters_big[0]]
packet2 = [monsters[1], monsters_big[1]]
packet3 = [monsters[2], monsters_big[2]]
packet4 = [monsters[3], monsters_big[3]]
packet5 = [monsters[4], monsters_big[4]]
packet6 = [monsters[5], monsters_big[5]]

# packet1 = [monster1, monster_big1]
# packet2 = [monster2, monster_big2]
# packet3 = [monster3, monster_big3]
# packet4 = [monster4, monster_big4]
# packet5 = [monster5, monster_big5]
# packet6 = [monster6, monster_big6]


packets = [packet1, packet2, packet3, packet4, packet5, packet6]

monsters = {
    monsters[0]: {
        "name": "Spiteling",
        "type": "Water",
        "weight": 6.9,
        "height": 0.7
    },
    monsters[1]: {
        "name": "Vampling",
        "type": "Fire",
        "weight": 13.7,
        "height": 1.3
    },
    monsters[2]: {
        "name": "Cinder",
        "type": "Ground",
        "weight": 12.9,
        "height": 1.1
    },
    monsters[3]: {
        "name": "Vextaur",
        "type": "Flying",
        "weight": 5.4,
        "height": 0.9
    },
    monsters[4]: {
        "name": "Wazow",
        "type": "Fighting",
        "weight": 1.4,
        "height": 1.0
    },
    monsters[5]: {
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

screen_game = pygame.display.set_mode((display_width_game, display_height_game))
screen = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()

pygame.display.set_caption("FavPet")


def button(text, x, y, w, h, ia_c, a_c, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, a_c, (x, y, w, h))
        if click[0] == 1 and action is not None:
            if action == "karmienie":
                main_karmienie(character)
            elif action == "obrona":
                main_bronienie(character)
            elif action == "menu":
                menu(monsters[character], character)
            else:
                action()
    else:
        pygame.draw.rect(screen, ia_c, (x, y, w, h))
    message_display(text, font_small, (x+(w//2)) * 2, (y+(h//2)) * 2, white)


def message_display(text, size, place_width, place_height, tone):
    text_surface = size.render(text, True, tone)
    text_rect = text_surface.get_rect()
    text_rect.center = ((place_width//2), (place_height//2))
    screen.blit(text_surface, text_rect)


def unpaused_bronienie():
    bronienie.music(0, "play", bronienie.main_music)
    global pause
    pause = False


def unpaused_karmienie():
    karmienie.music(0, "play", karmienie.jazz_music)
    global pause
    pause = False


def paused_karmienie():
    while pause:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        karmienie.music(0, "stop", karmienie.jazz_music)
        message_display("Pauza...", font_big, karmienie.display_width, karmienie.display_height, blue)
        button("Kontynuuj", 350, 550, 300, 50, blue, blue_light, unpaused_karmienie)
        button("Wróć do menu...", 750, 550, 300, 50, blue, blue_light, "menu")
        pygame.display.update()


def paused_bronienie():
    while pause:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        bronienie.music(0, "stop", bronienie.main_music)
        message_display("Pauza...", font_big, bronienie.display_width, bronienie.display_height - 200, blue)
        button("Kontynuuj", 350, 550, 300, 50, blue, blue_light, unpaused_bronienie)
        button("Wróć do menu...", 750, 550, 300, 50, blue, blue_light, "menu")
        pygame.display.update()


def game_over_karmienie(count, level):
    karmienie.music(0, "stop", karmienie.jazz_music)
    screen_game.fill(white)
    message_display("PRZEGRAŁEŚ :(", font_big, display_width_game, display_height_game, blue)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        button("Zagraj ponownie!", 150, 550, 300, 50, blue, blue_light, "karmienie")
        button("Wróć do menu...", 500, 550, 300, 50, blue, blue_light, "menu")
        button("Wyjdź.", 850, 550, 300, 50, blue, blue_light, quitgame)
        message_display("Twoje statystyki: ", font_medium, display_width_game, int(display_height_game // 4), blue_dark)
        message_display("Zjedzone: " + str(count), font_medium, int(display_width_game * 1 / 3),
                        display_height_game // 2, blue_dark)
        text = font_medium.render("Poziom: " + str(level), True, blue_dark)
        screen_game.blit(text, (1050, 165))
        pygame.display.update()


def game_over_bronienie(kill, level):
    bronienie.music(0, "stop", bronienie.main_music)
    screen_game.fill(white)
    message_display("PRZEGRAŁEŚ :(", font_big, display_width_game, display_height_game, blue)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        button("Zagraj ponownie!", 150, 550, 300, 50, blue, blue_light, "obrona")
        button("Wróć do menu...", 500, 550, 300, 50, blue, blue_light, "menu")
        button("Wyjdź.", 850, 550, 300, 50, blue, blue_light, quitgame)
        message_display("Twoje statystyki ", font_medium, display_width_game, int(display_height_game // 4), blue_dark)
        message_display("Zestrzelone: "+str(kill), font_medium, int(display_width_game*1/3), display_height_game//2,
                        blue_dark)
        text = font_medium.render("Poziom: " + str(level), True, blue_dark)
        screen_game.blit(text, (1100, 165))
        pygame.display.update()


def play_or_end():
    while pause:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        karmienie.music(0, "stop", karmienie.jazz_music)
        message_display("Nakarmiłeś FavPeta!", font_big, display_width_game, display_height_game // 2, blue)
        message_display("Czy chcesz dalej kontynuować grę?", font_medium, display_width_game, display_height_game,
                        blue_dark)
        button("Kontynuuj", 350, 550, 300, 50, blue, blue_light, unpaused_karmienie)
        button("Wróć do menu....", 750, 550, 300, 50, blue, blue_light, "menu")
        pygame.display.update()


def quitgame():
    pygame.quit()
    quit()


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


def menu(creature, img):
    while True:
        pygame.display.set_mode((display_width, display_height))
        screen.blit(menu_glowne, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        for j in range(0, 6, 1):
            if img == packets[j][0]:
                screen.blit(packets[j][1], (35, 80))
        statystyki = font_medium.render("Statystyki:", True, blue_dark)
        screen.blit(statystyki, (600, 20))
        name = font_small.render("Imię zwierzątka:   "+str(creature["name"]), True, blue_dark)
        screen.blit(name, (450, 100))
        typ = font_small.render("Typ:   "+str(creature["type"]), True, blue_dark)
        screen.blit(typ, (450, 150))
        weight = font_small.render("Waga:   "+str(creature["weight"])+" kg", True, blue_dark)
        screen.blit(weight, (450, 200))
        height = font_small.render("Wzrost:   "+str(creature["height"])+" m", True, blue_dark)
        screen.blit(height, (450, 250))
        aktywnosci = font_medium.render("Aktywności: ", True, blue_dark)
        screen.blit(aktywnosci, (590, 340))
        button("Karmienie", 450, 420, 200, 50, blue, blue_dark, "karmienie")
        button("Obrona", 750, 420, 200, 50, blue, blue_dark, "obrona")
        button("Wyjdź", 600, 500, 200, 50, blue, blue_dark, quitgame)
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
        screen.blit(intro_screen, (0, 0))
        message_display("Kliknij SPACE, aby kontynuować...", font_medium, 1080, 730, blue_dark)
        pygame.display.update()


def main_karmienie(img):
    """ USTAWIENIE DO POPRAWNEGO DZIAŁANIA FUNKCJI PAUZY """
    global pause

    """ USTAWIENIE DLA LEPSZEGO KOMFORTU GRY """
    pygame.display.set_mode((display_width_game, display_height_game))

    """ ODPALENIE GŁÓWNEGO MOTYWU MUZYCZNEGO """
    karmienie.music(0, "play", karmienie.jazz_music)

    """ WYJŚCIOWE USTAWIENIA POZYCJI STWORKA """
    x_monster = int(display_width_game * 0.43)
    y_monster = int(display_height_game * 0.80)

    """ PARAMETR DO STEROWANIA POTWORKIEM """
    x_change = 0

    """ LOSOWE USTAWIENIE PIERWSZEGO ELEMENTU """
    object_startx = random.randrange(0 + 55, display_width_game - karmienie.object_width - 51)
    object_starty = -display_height_game
    object_speed = 4
    objectimg = karmienie.which_object(karmienie.food)

    """ PARAMETRY DO ZMIANY STATYSTYK W TRAKCIE GRY """
    catched = 0
    missed = 0
    level = 1

    """ GŁÓWNA PĘTLA GRY """
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
                    paused_karmienie()
            if event.type == KEYUP:
                if event.key == K_a or event.key == K_d:
                    x_change = 0

        """ WYŚWIETLENIE NA EKRAN WSZYSTKICH POTRZEBNYCH STRUKTUR """
        screen_game.fill(white)
        karmienie.monster(screen_game, x_monster, y_monster, img)
        karmienie.objects(screen_game, object_startx, object_starty, objectimg)
        karmienie.levels(screen_game, level)
        karmienie.hp(screen_game, missed)
        karmienie.food_bar(screen_game, catched)
        karmienie.ate(screen_game, catched)

        """ ZMIANA POZYCJI STWORKA I ELEMENTÓW """
        object_starty += object_speed
        x_monster += x_change

        """ WARUNEK DLA WYJŚCIA POZA EKRAN """
        if x_monster > display_width_game - karmienie.monster_width - 51 or x_monster < 0 + 55:
            x_monster -= x_change

        """ WARUNEK DLA WYJŚCIA ELEMENTU POZA EKRAN(NIE ZŁAPANIE ELEMENTU) """
        if object_starty > display_height_game - karmienie.object_height:
            if objectimg != karmienie.food[6] and objectimg != karmienie.food[7]:
                missed += 1
            objectimg = karmienie.which_object(karmienie.food)
            object_starty = 0
            object_startx = random.randrange(0 + 55, display_width_game - karmienie.object_width - 51)

        """ WARUNEK DLA ZETKNIĘCIA SIĘ ELEMENTU ZE STWORKIEM(ZŁAPANIE ELEMENTU) """
        if object_starty + karmienie.object_height > y_monster:
            if x_monster + karmienie.monster_width > object_startx and x_monster < object_startx + \
                    karmienie.object_width:
                karmienie.music(1, "play", karmienie.bite_sound)
                if objectimg == karmienie.food[6]:
                    missed -= 1
                elif objectimg == karmienie.food[7]:
                    missed += 1
                else:
                    catched += 1
                if catched % 5 == 0:
                    if objectimg != karmienie.food[6] and objectimg != karmienie.food[7]:
                        level += 1
                        object_speed += 1
                objectimg = karmienie.which_object(karmienie.food)
                object_starty = 0
                object_startx = random.randrange(0 + 55, display_width_game - display_height_game - 51)

                """ WARUNEK DLA WYPEŁNIENIA PASKA GŁODU """
                if catched == 50:
                    pause = True
                    play_or_end()

        """ WARUNEK ZABEZPIECZAJĄCY ZMIENNĄ DLA NIEZŁAPANYCH ELEMENTÓW PRZED USTAWIENIEM NA WARTOŚĆ < 0 """
        if missed < 0:
            missed = 0

        """ WARUNEK DLA UTRATY WSZYSTKICH ŻYĆ """
        if missed > 9:
            game_over_karmienie(catched, level)

        pygame.display.update()
        clock.tick(60)


def main_bronienie(img):
    """ USTAWIENIE DO POPRAWNEGO DZIAŁANIA FUNKCJI PAUZY """
    global pause

    """ USTAWIENIE DLA LEPSZEGO KOMFORTU GRY """
    pygame.display.set_mode((display_width_game, display_height_game))

    ''' ROZPOCZĘCIE GRANIA MUZYKI '''
    bronienie.music(0, "play", bronienie.main_music)

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
                    paused_bronienie()

        ''' PRZYGOTOWANIE EKRANU '''
        screen_game.fill(white)
        bronienie.monster(screen_game, x_monster, y_monster, img)
        bronienie.kill_count(screen_game, kill)
        bronienie.hp(screen_game, hit)
        bronienie.levels(screen_game, level)
        bronienie.spawn_enemy(screen_game, enemy, pos_enemies[enemy][0], pos_enemies[enemy][1])

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
        if (pos_enemies[0][0] + bronienie.enemy_width > x_monster) and (pos_enemies[0][1] + bronienie.enemy_height >
                                                                        y_monster):
            bronienie.music(2, "play", bronienie.hurt_sound)
            bronienie.reset_enemy_pos(pos_enemies, 0)
            enemy = random.randrange(0, 4)
            hit += 1
            x_change_e, y_change_e = bronienie.set_enemy_speed(1)

        elif (pos_enemies[1][0] < x_monster + bronienie.monster_width) and (pos_enemies[1][1] + bronienie.enemy_height >
                                                                            y_monster):
            bronienie.music(2, "play", bronienie.hurt_sound)
            bronienie.reset_enemy_pos(pos_enemies, 1)
            enemy = random.randrange(0, 4)
            hit += 1
            x_change_e, y_change_e = bronienie.set_enemy_speed(1)

        elif (pos_enemies[2][0] < x_monster + bronienie.monster_width) and (pos_enemies[2][1] <
                                                                            y_monster + bronienie.monster_height):
            bronienie.music(2, "play", bronienie.hurt_sound)
            bronienie.reset_enemy_pos(pos_enemies, 2)
            enemy = random.randrange(0, 4)
            hit += 1
            x_change_e, y_change_e = bronienie.set_enemy_speed(1)

        elif (pos_enemies[3][0] + bronienie.enemy_width > x_monster) and (pos_enemies[3][1] <
                                                                          y_monster + bronienie.monster_height):
            bronienie.music(2, "play", bronienie.hurt_sound)
            bronienie.reset_enemy_pos(pos_enemies, 3)
            enemy = random.randrange(0, 4)
            hit += 1
            x_change_e, y_change_e = bronienie.set_enemy_speed(1)

        ''' ZABIJANIE POTWORÓW I WSZYSTKIE AKCJE Z TYM ZWIĄZANE, CZYLI:
            - RESETOWANIE POZYCI PO ZABÓJSTWIE,
            - LOSOWANIE POZYCJI KOLEJNEGO WROGA,
            - ZWIĘKSZANIE LICZNIKA ZABÓJSTW,
            - LOSOWANIE PRĘDKOŚCI PRZECIWNIKA,
            - ZARZĄDZANIE DŹWIEKAMI '''
        if pos_enemies[0][0] + bronienie.enemy_width > mouse[0] > pos_enemies[0][0] and \
                pos_enemies[0][1] + bronienie.enemy_height > mouse[1] > pos_enemies[0][1]:
            if click[0] == 1:
                bronienie.reset_enemy_pos(pos_enemies, 0)
                enemy = random.randrange(0, 4)
                kill += 1
                x_change_e, y_change_e = bronienie.set_enemy_speed(1)
                if kill % 2 == 0:
                    bronienie.music(1, "play", bronienie.kill_sound)

        elif pos_enemies[1][0] + bronienie.enemy_width > mouse[0] > pos_enemies[1][0] and\
                pos_enemies[1][1] + bronienie.enemy_height > mouse[1] > pos_enemies[1][1]:
            if click[0] == 1:
                bronienie.reset_enemy_pos(pos_enemies, 1)
                enemy = random.randrange(0, 4)
                kill += 1
                x_change_e, y_change_e = bronienie.set_enemy_speed(1)
                if kill % 2 == 0:
                    bronienie.music(1, "play", bronienie.kill_sound)

        elif pos_enemies[2][0] + bronienie.enemy_width > mouse[0] > pos_enemies[2][0] and\
                pos_enemies[2][1] + bronienie.enemy_height > mouse[1] > pos_enemies[2][1]:
            if click[0] == 1:
                bronienie.reset_enemy_pos(pos_enemies, 2)
                enemy = random.randrange(0, 4)
                kill += 1
                x_change_e, y_change_e = bronienie.set_enemy_speed(1)
                if kill % 2 == 0:
                    bronienie.music(1, "play", bronienie.kill_sound)

        elif pos_enemies[3][0] + bronienie.enemy_width > mouse[0] > pos_enemies[3][0] and\
                pos_enemies[3][1] + bronienie.enemy_height > mouse[1] > pos_enemies[3][1]:
            if click[0] == 1:
                bronienie.reset_enemy_pos(pos_enemies, 3)
                enemy = random.randrange(0, 4)
                kill += 1
                x_change_e, y_change_e = bronienie.set_enemy_speed(1)
                if kill % 2 == 0:
                    bronienie.music(1, "play", bronienie.kill_sound)

        ''' ZWIĘKSZANIE TRUDNOŚCI GRY '''
        if kill > 9:
            x_change_e, y_change_e = bronienie.set_enemy_speed(2)
            level = 2
        if kill > 19:
            x_change_e, y_change_e = bronienie.set_enemy_speed(3)
            level = 3
        if kill > 29:
            x_change_e, y_change_e = bronienie.set_enemy_speed(4)
            level = 4
        # POZIOM DLA PROSÓW ;)
        if kill > 99:
            x_change_e, y_change_e = bronienie.set_enemy_speed(5)
            level = 9000

        ''' GDY WYCZERPIEMY LIMIT ŻYĆ GRA SIĘ KOŃCZY '''
        if hit > 9:
            game_over_bronienie(kill, level)

        pygame.display.update()
        clock.tick(60)


pause = False

character = intro()
menu(monsters[character], character)
