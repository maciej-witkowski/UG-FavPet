import pygame
import random
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

hp_bar = pygame.image.load('bars/hpbar_horizontal.png')
hp_cover = pygame.image.load('bars/white_pallet.png')

enemy1 = pygame.image.load('enemy_img/enemy1icon.png')
enemy2 = pygame.image.load('enemy_img/enemy2icon.png')
enemy3 = pygame.image.load('enemy_img/enemy3icon.png')
enemy4 = pygame.image.load('enemy_img/enemy5icon.png')

enemies = [enemy1, enemy2, enemy3, enemy4]

choose_screen = pygame.display.set_mode((1000, 600))


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


def music(channel, action, file):
    if action == "play":
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound(file))
    elif action == "stop":
        pygame.mixer.Channel(channel).stop()
