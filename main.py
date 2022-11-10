# import random
import pygame
import select_step as s
import images as i
import rects as r
from sys import exit

pygame.init()
pygame.font.init()
font_default = pygame.font.SysFont('None', 70)
# setting game --------------------------------------------------------------------------

# loading assets ------------------------------------------------------------------------
screen_width = 1366
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Capstone Game")  # Window title
pygame.display.set_icon(i.window_icon) # Set window icon to wind turbines

clock = pygame.time.Clock()
game_state = 0

# section end -------------------------------------------------------------------------------

while True:  # Main Loop
    #  power flow computation start
    pass
    # power flow computation end

    #  Event loop
    for event in pygame.event.get():
        # Close the game when close button is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        game_state = s.select_step(event, game_state)
    #  event loop end

    #  display and UI
    if game_state in range(0, 100):  # title screen
        screen.blit(i.bg_00, (0, 0))
        screen.blit(i.title, (200, 100))
        screen.blit(i.button_start, r.r_button_start)

    elif game_state in range(100, 200):  # tutorial 1
        screen.fill((255, 255, 255))
        screen.blit(i.bg_10, (0, 0))
        screen.blit(i.button_next, r.r_button_next)

        if game_state == 100:
            screen.blit(i.text_sample, (0, 625))

        elif game_state == 101:
            screen.blit(i.text_sample2, (0, 625))

        elif game_state == 102:
            screen.blit(i.text_sample3, (0, 625))
            screen.blit(i.mask_tut1_3, (0, 0))

        elif game_state == 103:
            screen.blit(i.text_sample4, (0, 625))

        elif game_state == 104:
            screen.blit(i.text_sample5, (0, 625))


    elif game_state in range(200, 300):  # tutorial 2 (TEST FOR NOW)
        screen.fill((255, 255, 255))
        screen.blit(i.bg_20, (0,0))

        if (game_state == 200):
            # Nuclear plant
            nuclear_image = i.nuclear_image.copy()
            nuclear_image.fill((255, 255, 255, 128))
            screen.blit(nuclear_image, r.nuclear_rect)
        elif (game_state == 201):
            nuclear_image = i.nuclear_image
            #nuclear_image.fill((0, 0, 0))
            screen.blit(i.nuclear_image, r.nuclear_rect)
    


    elif game_state in range(300, 400):  # tutorial 3
        pass
    elif game_state in range(400, 500):  # tutorial 4
        pass
    elif game_state in range(500, 600):  # game - daily
        pass
    elif game_state in range(600, 700):  # game - monthly
        pass
    elif game_state in range(700, 800):  # options
        pass
    #  display and UI end

    current_time = round(pygame.time.get_ticks()/1000, 1)   # display time on the right, for testing purposes
    time_surf = font_default.render(str(current_time), False, (0, 0, 0))
    screen.blit(time_surf, (1220, 20))

    pygame.display.update()
    clock.tick(30)


