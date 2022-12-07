# import random
import pygame
import select_step as s
import images as i
import rects as r
import text as t
from sys import exit
from map import map, choose_image, choose_rect

pygame.init()
pygame.font.init()
font_default = pygame.font.SysFont('timesnewroman', 48)
font_text = pygame.font.SysFont('timesnewroman', 30)
print(pygame.font.get_fonts())
# setting game --------------------------------------------------------------------------

# loading assets ------------------------------------------------------------------------
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Capstone Game")  # name that appears on window
pygame.display.set_icon(i.window_icon) # Set window icon to wind turbines

clock = pygame.time.Clock()
game_state = 0

is_slider = 0
slider_move = [0, 0]
drag_tabs = [0, 0]
drag_start = 0
gen_set = [0, 0]
textbox_top = (20, 920)
textbox_mid = (20, 955)
textbox_bot = (20, 990)
# section end -------------------------------------------------------------------------------

# Initialize variable to select which area is being changed
current_area = 'area_1'

while True:  # Main Loop
    #  power flow computation start
    pass
    # power flow computation end

    #  event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYUP:  # doesn't work
            if event.key == pygame.K_f:
                pygame.quit()
                exit()
        step_select = s.select_step(event, game_state, map, current_area)
        game_state = step_select[0]
        map = step_select[1]
        current_area = step_select[2]

        if is_slider:
            for k in range(0,len(r.r_slider_list)):
                if event.type == pygame.MOUSEBUTTONDOWN and r.r_slider_list[k].collidepoint(event.pos):
                    drag_tabs[k] = 1
                    drag_start = event.pos[0]
                if event.type == pygame.MOUSEMOTION and drag_tabs[k] == 1:
                    slider_move[k] = max(950, min(1450, event.pos[0])) - r.r_slider_list[k].centerx
                    gen_set[k] = round(100 * (r.r_slider_list[k].centerx - 950) / (1450 - 950), 1)
                if event.type == pygame.MOUSEBUTTONUP:
                    drag_tabs[k] = 0

    #  event loop end

    #  display and UI
    if game_state in range(0, 100):  # title screen
        screen.blit(i.bg_00, (0, 0))
        screen.blit(i.title, r.r_title)
        screen.blit(i.button_start, r.r_button_start)

        
    elif game_state in range(100, 200):  # tutorial 1

        screen.fill((255, 255, 255))
        screen.blit(i.bg_10, (0, 0))
        screen.blit(i.fg_10, (0, 0))
        screen.blit(i.button_next.convert_alpha(), r.r_button_next)

        if game_state == 100:
            text_surf = font_text.render(t.text_100_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_100_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        elif game_state == 101:
            text_surf = font_text.render(t.text_101_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_101_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_101_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(i.notice_101_a, r.r_notice_101_a)
            screen.blit(i.notice_101_b, r.r_notice_101_b)

        elif game_state == 102:
            text_surf = font_text.render(t.text_102_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_102_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_102_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(i.load_tut1, (500, 625))

        elif game_state == 103:
            screen.blit(i.load_tut1, (500, 625))

        elif game_state == 104:
            screen.blit(i.load_tut1, (500, 625))

        elif game_state == 105:
            screen.blit(i.text_sample5, (0, 625))
            is_slider = 1
            screen.blit(i.slider_tut1, r.r_slider_tut1)
            screen.blit(i.slider_tut2, r.r_slider_tut2)
            r.r_slider_tut_tab1.move_ip((slider_move[0], 0))
            r.r_slider_tut_tab2.move_ip((slider_move[1], 0))
            screen.blit(i.slider_tut_tab1, r.r_slider_tut_tab1)
            screen.blit(i.slider_tut_tab2, r.r_slider_tut_tab2)
            slider_move = [0, 0]

            gen1_surf = font_default.render(str(gen_set[0]), False, (0, 0, 0))
            screen.blit(gen1_surf, (1220, 50))
            gen2_surf = font_default.render(str(gen_set[1]), False, (0, 0, 0))
            screen.blit(gen2_surf, (1220, 100))

    elif game_state in range(200, 300):  # tutorial 2

        if (game_state == 200):
            # Render new map every time
            screen.fill((255, 255, 255))
            screen.blit(i.bg_20, (0,0))

            for plant in map:
                plant_image = choose_image(map[plant]['type'])
                plant_rect = choose_rect(plant)
                screen.blit(plant_image, plant_rect)
                

        if (game_state == 201):
            # Create sidebar
            sidebar = pygame.Surface((300,screen_height))
            sidebar.set_alpha(128)
            sidebar.fill((255,255,255))
            screen.blit(sidebar,(0,0))

            screen.blit(i.plant_hydro, r.button_hydro)
            screen.blit(i.plant_wind, r.button_wind)
            screen.blit(i.plant_solar, r.button_solar)
            screen.blit(i.plant_nuclear, r.button_nuclear)
            screen.blit(i.plant_coal, r.button_coal)
            screen.blit(i.plant_gas, r.button_gas)

        elif (game_state == 202):
            pass

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
    else:
        pygame.quit()
        exit()

    current_time = round(pygame.time.get_ticks()/1000, 1)   # display time on the right, for testing purposes
    time_surf = font_default.render(str(current_time), False, (0, 0, 0))
    screen.blit(time_surf, (1800, 20))

    pygame.display.update()
    clock.tick(30)


