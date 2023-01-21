import pygame
import random
import time
import os

pygame.init()
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
cwd = os.getcwd()
music = pygame.mixer.music.load(cwd + '\\Game Files\\Sounds\\background_song.mp3') 
hit = pygame.mixer.Sound(cwd + '\\Game Files\\Sounds\\270326__littlerobotsoundfactory__hit-01.wav')
pickup = pygame.mixer.Sound(cwd + '\\Game Files\\Sounds\\347172__davidsraba__coin-pickup-sound.wav')
gameover_sound = pygame.mixer.Sound(cwd + '\\Game Files\\Sounds\\253886__themusicalnomad__negative-beeps.wav')

# Main Sound
pygame.mixer.music.set_volume(0.15)
hit.set_volume(0.30)
pickup.set_volume(0.30)
gameover_sound.set_volume(0.37)

# Sound Settings
pygame.mixer.music.set_volume(0.50)
hit.set_volume(0.40)
pickup.set_volume(0.40)
gameover_sound.set_volume(1.0)

pygame.mixer.music.play(-1)

gameover = False
chosen_char = False
border_coords = tuple()

# Colors
red = (255, 0, 0)
blue = (0, 0, 220)
bright_blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (242, 245, 66)


def quick_load(img):
    return pygame.image.load(img).convert_alpha()


# Images
border_img = quick_load(cwd + '\\Game Files\\Images\\Borders\\andrea_border_active.png')
small_icon = quick_load(cwd + '\\Game Files\\Images\\Etc\\small_icon.png')
heart_img = quick_load(cwd + '\\Game Files\\Images\\Etc\\heart.png')
game_over_text = quick_load(cwd + '\\Game Files\\Images\\Etc\\gameover.png')
main_background = quick_load(cwd + '\\Game Files\\Images\\Backgrounds\\char_select.png')
main_menu_background = quick_load(cwd + '\\Game Files\\Images\\Backgrounds\\main_menu_bg.png')
golden_border = quick_load(cwd + '\\Game Files\\Images\\Borders\\gold_border.png')
htp_background = quick_load(cwd + '\\Game Files\\Images\\Backgrounds\\htp.png')
about_bg = quick_load(cwd + '\\Game Files\\Images\\Backgrounds\\about.png')
# Philip Images
philip = {
    'char': quick_load(cwd + '\\Game Files\\Images\\Leads\\philip.png'),
    'obstacle': quick_load(cwd + '\\Game Files\\Images\\Obstacles\\philip_obstacle.png'),
    'catch': quick_load(cwd + '\\Game Files\\Images\\Catch\\philip_catch.png'),
    'background': quick_load(cwd + '\\Game Files\\Images\\Backgrounds\\philip_bg.png'),
    'inactive': quick_load(cwd + '\\Game Files\\Images\\Borders\\philip_border_inactive.png'),
    'active': quick_load(cwd + '\\Game Files\\Images\\Borders\\philip_border_active.png')
}
# Jessica Images
jessica = {
    'char': quick_load(cwd + '\\Game Files\\Images\\Leads\\jessica.png'),
    'obstacle': quick_load(cwd + '\\Game Files\\Images\\Obstacles\\jessica_obstacle.png'),
    'catch': quick_load(cwd + '\\Game Files\\Images\\Catch\\jessica_catch.png'),
    'background': quick_load(cwd + '\\Game Files\\Images\\Backgrounds\\jessica_bg.png'),
    'inactive': quick_load(cwd + '\\Game Files\\Images\\Borders\\jessica_border_inactive.png'),
    'active': quick_load(cwd + '\\Game Files\\Images\\Borders\\jessica_border_active.png')
}
# Andrea Images
andrea = {
    'char': quick_load(cwd + '\\Game Files\\Images\\Leads\\andrea.png'),
    'obstacle': quick_load(cwd + '\\Game Files\\Images\\Obstacles\\andrea_obstacle.png'),
    'catch': quick_load(cwd + '\\Game Files\\Images\\Catch\\andrea_catch.png'),
    'background': quick_load(cwd + '\\Game Files\\Images\\Backgrounds\\andrea_bg.png'),
    'inactive': quick_load(cwd + '\\Game Files\\Images\\Borders\\andrea_border_inactive.png'),
    'active': quick_load(cwd + '\\Game Files\\Images\\Borders\\andrea_border_active.png')
}
# Eric Images
eric = {
    'char': quick_load(cwd + '\\Game Files\\Images\\Leads\\eric.png'),
    'obstacle': quick_load(cwd + '\\Game Files\\Images\\Obstacles\\eric_obstacle.png'),
    'catch': quick_load(cwd + '\\Game Files\\Images\\Catch\\eric_catch.png'),
    'background': quick_load(cwd + '\\Game Files\\Images\\Backgrounds\\eric_bg.png'),
    'inactive': quick_load(cwd + '\\Game Files\\Images/Borders/eric_border_inactive.png'),
    'active': quick_load(cwd + '\\Game Files/Images/Borders/eric_border_active.png')
}
# Button Images
buttons = {
    'PLAY AGAIN': [quick_load(cwd + '\\Game Files/Buttons/play_again_inactive.png'), quick_load(cwd + '\\Game Files/Buttons/play_again_active.png')],
    'QUIT': [quick_load(cwd + '\\Game Files/Buttons/quit_inactive.png'), quick_load(cwd + '\\Game Files/Buttons/quit_active.png')],
    'MENU': [quick_load(cwd + '\\Game Files/Buttons/menu_inactive.png'), quick_load(cwd + '\\Game Files/Buttons/menu_active.png')],
    'START': [quick_load(cwd + '\\Game Files/Buttons/start_inactive.png'), quick_load(cwd + '\\Game Files/Buttons/start_active.png'), quick_load(cwd + '\\Game Files/Buttons/start_disabled.png')],
    'MAIN START': [quick_load(cwd + '\\Game Files/Buttons/main_start_inactive.png'), quick_load(cwd + '\\Game Files/Buttons/main_start_active.png')],
    'HTP': [quick_load(cwd + '\\Game Files/Buttons/htp_inactive.png'), quick_load(cwd + '\\Game Files/Buttons/htp_active.png')],
    'ABOUT': [quick_load(cwd + '\\Game Files/Buttons/about_inactive.png'), quick_load(cwd + '\\Game Files/Buttons/about_active.png')],
    'BACK': [quick_load(cwd + '\\Game Files/Buttons/cancel_inactive.png'), quick_load(cwd + '\\Game Files/Buttons/cancel_active.png')]
}

person = None

# Other Stuff
pygame.display.set_caption('2020 Boeing HSI Game')
pygame.display.set_icon(small_icon)


def quitgame():
    pygame.quit()
    quit()


def update_score(score):
    font = pygame.font.Font(cwd + '\\Game Files/Fonts/fipps.otf', 40)
    color = black
    text_surf, text_rect = text_objects(str(score), font, color)
    text_rect.center = (screen_width // 2, 60)
    screen.blit(text_surf, text_rect)


def character(x, y):
    screen.blit(character_img, (x, y))


def obstacle(x, y):
    screen.blit(obstacle_img, (x, y))


def catch(x, y):
    screen.blit(catch_img, (x, y))


def heart(x, y):
    screen.blit(heart_img, (x, y))


def text_objects(message, style, color):
    text_surf = style.render(message, True, color)
    return text_surf, text_surf.get_rect()


def update_variable(char):
    global character_img, obstacle_img, catch_img, background, character_width, character_height, obstacle_width, obstacle_height, catch_width, catch_height
    global person

    person = char
    character_img = person['char']
    obstacle_img = person['obstacle']
    catch_img = person['catch']
    background = person['background']

    character_width, character_height = character_img.get_rect().size
    obstacle_width, obstacle_height = obstacle_img.get_rect().size
    catch_width, catch_height = obstacle_img.get_rect().size


def set_char(char):
    global chosen_char
    chosen_char = True
    if char == philip:
        update_variable(philip)
    elif char == jessica:
        update_variable(jessica)
    elif char == eric:
        update_variable(eric)
    elif char == andrea:
        update_variable(andrea)


def button(inactive_img, active_img, x, y, action=None):
    global person
    global border_coords
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    button_w, button_h = inactive_img.get_rect().size
    if x < mouse[0] < x + button_w and y < mouse[1] < y + button_h:
        screen.blit(active_img, (x, y))
        if click[0] == 1 and action != None:
            action()
    else:
        screen.blit(inactive_img, (x, y))
    if person != None:
        screen.blit(golden_border, border_coords)


def set_philip():
    global border_coords
    set_char(philip)
    border_coords = (755, 100)


def set_jessica():
    global border_coords
    set_char(jessica)
    border_coords = (265, 100)


def set_andrea():
    global border_coords
    set_char(andrea)
    border_coords = (510, 100)


def set_eric():
    global border_coords
    set_char(eric)
    border_coords = (20, 100)


def crash():
    global person
    person = None
    gameover_sound.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        screen.blit(game_over_text, (0, 100))

        button(buttons['PLAY AGAIN'][0], buttons['PLAY AGAIN'][1], 330, 280, game)
        button(buttons['MENU'][0], buttons['MENU'][1], 330, 380, main_menu)
        button(buttons['QUIT'][0], buttons['QUIT'][1], 330, 480, quitgame)

        pygame.display.update()
        clock.tick(15)


def about():
    about = True
    while about:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        screen.blit(about_bg, (0, 0))
        button(buttons['BACK'][0], buttons['BACK'][1], 20, 20, main_menu)
        pygame.display.update()
        clock.tick(15)


def htp():
    htp = True
    while htp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        screen.blit(htp_background, (0, 0))
        button(buttons['BACK'][0], buttons['BACK'][1], 20, 20, main_menu)
        pygame.display.update()
        clock.tick(15)


def main_menu():
    time.sleep(0.30)
    global gameover
    gameover = True
    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        screen.blit(main_menu_background, (0, 0))
        button(buttons['MAIN START'][0], buttons['MAIN START'][1], 250, 220, menu)
        button(buttons['HTP'][0], buttons['HTP'][1], 250, 320, htp)
        button(buttons['ABOUT'][0], buttons['ABOUT'][1], 250, 420, about)

        pygame.display.update()
        clock.tick(15)


def menu():
    time.sleep(0.30)
    global gameover, chosen_char, person
    chosen_char = False
    gameover = True
    person = None
    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        screen.blit(main_background, (0, 0))

        button(eric['inactive'], eric['active'], 20, 100, set_eric)
        button(jessica['inactive'], jessica['active'], 265, 100, set_jessica)
        button(philip['inactive'], philip['active'], 755, 100, set_philip)
        button(andrea['inactive'], andrea['active'], 510, 100, set_andrea)

        if chosen_char:
            button(buttons['START'][0], buttons['START'][1], 377, 510, game)
        elif not chosen_char:
            button(buttons['START'][2], buttons['START'][2], 377, 510)

        pygame.display.update()
        clock.tick(15)


def game():
    global gameover
    pygame.event.clear()
    character_x = (screen_width-character_width)//2
    character_y = screen_height - character_height
    lives = 3
    speed = 15
    score = 0

    num_obstacles = 3
    obstacle_x = []
    obstacle_y = []
    obstacle_speed = []

    catch_x = random.randrange(0, screen_width)
    catch_y = -catch_height - random.randrange(0, 100)
    catch_speed = 7

    for i in range(num_obstacles):
        obstacle_x.append(random.randrange(0, screen_width))
        obstacle_y.append(-(obstacle_height + random.randrange(100, 200)))
        obstacle_speed.append(random.randrange(7, 13))

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a] and character_x > 0:
            character_x -= speed
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d] and character_x + character_width < screen_width:
            character_x += speed

        screen.blit(background, (0, 0))

        for i in range(num_obstacles):
            obstacle(obstacle_x[i], obstacle_y[i])
            obstacle_y[i] += obstacle_speed[i]

        character(character_x, character_y)
        catch(catch_x, catch_y)
        catch_y += catch_speed

        update_score(score)

        for j in range(num_obstacles):
            if obstacle_y[j] > screen_height:
                obstacle_y[j] = -obstacle_height
                obstacle_x[j] = random.randrange(0, screen_width)
                obstacle_speed[j] = random.randrange(7, 10)

            if character_y < obstacle_y[j] + obstacle_height-30:
                if character_x <= obstacle_x[j] <= character_x + character_width or character_x <= obstacle_x[j] + obstacle_width <= character_x + character_width:
                    hit.play()
                    if lives > 1:
                        obstacle_x[j] = random.randrange(0, screen_width)
                        obstacle_y[j] = -obstacle_height
                        obstacle_speed[j] = random.randrange(7, 10)
                        lives -= 1
                    elif lives == 1:
                        crash()

        tmp = 55
        for z in range(lives):
            heart(screen_width-tmp, 5)
            tmp += 55

        if character_y < catch_y+30:
            if character_x <= catch_x <= character_x + character_width or character_x <= catch_x + catch_width <= character_x + character_width:
                pickup.play()
                catch_x = random.randrange(0, screen_width-catch_width)
                catch_y = -catch_height
                score += 1

        if catch_y > screen_height:
            catch_x = random.randrange(0, screen_width-catch_width)
            catch_y = -catch_height

        pygame.display.update()
        clock.tick(60)


main_menu()
