# import random
import pygame
import select_step as s
import images as i
import rects as r
import text as t
import panda_power as p
from sys import exit
from map import map, choose_image, choose_rect

pygame.init()
pygame.font.init()
font_default = pygame.font.SysFont('timesnewroman', 48)
font_text = pygame.font.SysFont('timesnewroman', 30)
font_labels = pygame.font.SysFont('timesnewroman',40, bold=True)
font_info = pygame.font.SysFont('timesnewroman',36, bold=True)
#print(pygame.font.get_fonts())
# setting game --------------------------------------------------------------------------

# loading assets ------------------------------------------------------------------------
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Capstone Game")  # name that appears on window
pygame.display.set_icon(i.window_icon) # Set window icon to wind turbines

clock = pygame.time.Clock()
game_state = 0
current_time = 0

is_pf_success = 0
is_slider = 0
slider_move = [0, 0]
drag_tabs = [0, 0]
drag_start = 0
gen_set = [0, 0]
gen_cost = [10, 15]
textbox_top = (20, 920)
textbox_mid = (20, 955)
textbox_bot = (20, 990)
load_val = 150
pf_done = 0

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
        if event.type == pygame.KEYUP:  # quit
            if event.key == pygame.K_q:
                pygame.quit()
                exit()
            elif event.key == pygame.K_t:
                game_state = 0

        step_select = s.select_step(event, game_state, map, current_area, is_pf_success)
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

        if game_state == 111 and pf_done != 1:
            line_flows = p.PF_tut1(gen_set)
        elif game_state == 208 and pf_done != 1:
            line_flows = p.PF_tut1(gen_set)
        elif game_state==306 and pf_done !=1:
            line_flows = p.PF_tut3([100,50],load_val)[0]
            line_ratings = p.PF_tut3([100,50],load_val)[1]
            pf_balance=p.PF_tut3_loss([100,50])[2]
        elif game_state==323 and pf_done !=1:
            line_flows = p.PF_tut3(gen_set,load_val)[0]
            line_ratings = p.PF_tut3(gen_set,load_val)[1]
        

    #  event loop end

    #  display and UI
    if game_state in range(0, 100):  # title screen
        if game_state == 0:
            screen.blit(i.bg_00, (0, 0))
            screen.blit(i.title, r.r_title)
            screen.blit(i.button_start, r.r_button_start)
            screen.blit(i.button_choose_level, r.r_button_choose_level)

        elif game_state == 1:
            screen.blit(i.bg_00, (0, 0))
            screen.blit(i.mask_all, (0, 0))
            screen.blit(i.choose_leveL_box, r.r_choose_level_box)
            screen.blit(i.button_back, r.r_button_back)
            screen.blit(i.choose_1, r.r_choose_1)
            screen.blit(i.choose_2, r.r_choose_2)
            screen.blit(i.choose_3, r.r_choose_3)
            screen.blit(i.choose_4, r.r_choose_4)
            screen.blit(i.choose_5, r.r_choose_5)
            screen.blit(i.choose_6, r.r_choose_6)

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

            screen.blit(i.load_tut1, r.r_load_tut1)

        elif game_state == 103:
            text_surf = font_text.render(t.text_103_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_103_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_103_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(i.load_tut1, r.r_load_tut1)
            screen.blit(i.gen1_tut1, r.r_gen1_tut1)
            screen.blit(i.gen2_tut1, r.r_gen2_tut1)

        elif game_state == 104:
            text_surf = font_text.render(t.text_104_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_104_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_104_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(i.system_tut1, r.r_system_tut1)

        elif game_state == 105:
            text_surf = font_text.render(t.text_105_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_105_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            screen.blit(i.system_tut1, r.r_system_tut1)

        elif game_state == 106:
            text_surf = font_text.render(t.text_106_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_106_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            screen.blit(i.system_tut1, r.r_system_tut1)

        elif game_state == 107:
            text_surf = font_text.render(t.text_107_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_107_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_107_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(i.system_tut1, r.r_system_tut1)

        elif game_state == 108:
            screen.blit(i.system_tut1, r.r_system_tut1)

            text_surf = font_text.render(t.text_108_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_108_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_108_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            load_surf = font_labels.render(str(load_val) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(gen_set[0]) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(gen_set[1]) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))

            p_imbalance = gen_set[0] + gen_set[1] - load_val
            if p_imbalance == 0:
                p_imbalance_color = (0, 255, 0)
            else:
                p_imbalance_color = (255, 0, 0)
            p_imbalance_surf = font_info.render(str(p_imbalance) + "MW", False, p_imbalance_color)
            screen.blit(p_imbalance_surf, r.r_p_imbalance)

        elif game_state == 109:
            screen.blit(i.system_tut1, r.r_system_tut1)
            screen.blit(i.button_run.convert_alpha(), r.r_button_run)

            text_surf = font_text.render(t.text_109_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_109_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            is_slider = 1
            screen.blit(i.slider_tut1, r.r_slider_tut1)
            screen.blit(i.slider_tut2, r.r_slider_tut2)
            r.r_slider_tut_tab1.move_ip((slider_move[0], 0))
            r.r_slider_tut_tab2.move_ip((slider_move[1], 0))
            screen.blit(i.slider_tut_tab1, r.r_slider_tut_tab1)
            screen.blit(i.slider_tut_tab2, r.r_slider_tut_tab2)
            slider_move = [0, 0]

            load_surf = font_labels.render(str(load_val) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(gen_set[0]) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(gen_set[1]) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))

            p_imbalance = round(gen_set[0] + gen_set[1] - load_val, 1)
            if p_imbalance == 0:
                p_imbalance_color = (0, 255, 0)
                is_pf_success = 1
            else:
                p_imbalance_color = (255, 0, 0)
                is_pf_success = 0
            p_imbalance_surf = font_info.render(str(p_imbalance) + "MW", False, p_imbalance_color)
            screen.blit(p_imbalance_surf, r.r_p_imbalance)

        elif game_state == 110:
            is_slider = 0
            is_pf_success = 0
            screen.blit(i.system_tut1, r.r_system_tut1)
            screen.blit(i.mask_blackout, (0, 0))
            if current_time%2 <= 1:
                screen.blit(i.button_retry1.convert_alpha(), r.r_button_retry)
            else:
                screen.blit(i.button_retry2.convert_alpha(), r.r_button_retry)

            text_surf = font_text.render(t.text_110_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_110_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_110_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            load_surf = font_labels.render(str(load_val) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(gen_set[0]) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(gen_set[1]) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))

            screen.blit(p_imbalance_surf, (1600, 120))

        elif game_state == 111:
            pf_done = 1
            is_slider = 0
            screen.blit(i.system_tut1, r.r_system_tut1)

            text_surf = font_text.render(t.text_111_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top) # successful power flow
            text_surf = font_text.render(t.text_111_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            load_surf = font_labels.render(str(load_val) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(gen_set[0]) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(gen_set[1]) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))

            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (260, 450))

        elif game_state == 112:
            pf_done = 0
            screen.blit(i.system_tut1, r.r_system_tut1)

            load_surf = font_labels.render(str(load_val) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(gen_set[0]) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(gen_set[1]) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))

            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (260, 450))

            text_surf = font_text.render(t.text_112_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_112_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        elif game_state == 113:
            screen.blit(i.system_tut1, r.r_system_tut1)
            screen.blit(i.mask_blackout, (0, 0))
            screen.blit(load_surf, (720, 750))
            screen.blit(gen1_surf, (412, 150))
            screen.blit(gen2_surf, (1012, 150))
            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (260, 450))

            screen.blit(i.blank_textbox, r.r_blank_textbox)
            screen.blit(i.next_module, r.r_next_module)
            screen.blit(i.back_to_title, r.r_back_to_title)

            gen_set = [0, 0]

    elif game_state in range(200, 300):  # tutorial 2
        screen.fill((255, 255, 255))
        screen.blit(i.bg_10, (0, 0))
        screen.blit(i.fg_10, (0, 0))
        screen.blit(i.system_tut1, r.r_system_tut1)
        screen.blit(i.button_next.convert_alpha(), r.r_button_next)

        if game_state == 200:
            text_surf = font_text.render(t.text_200_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_200_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_200_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

        elif game_state == 201:
            text_surf = font_text.render(t.text_201_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_201_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_201_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

        elif game_state == 202:
            text_surf = font_text.render(t.text_202_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_202_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        elif game_state == 203:
            text_surf = font_text.render(t.text_203_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_203_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        elif game_state == 204:
            text_surf = font_text.render(t.text_204_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_204_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        elif game_state == 205:
            screen.blit(i.button_run.convert_alpha(), r.r_button_run)

            text_surf = font_text.render(t.text_205_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_205_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            is_slider = 1
            screen.blit(i.slider_tut1, r.r_slider_tut1)
            screen.blit(i.slider_tut2, r.r_slider_tut2)
            r.r_slider_tut_tab1.move_ip((slider_move[0], 0))
            r.r_slider_tut_tab2.move_ip((slider_move[1], 0))
            screen.blit(i.slider_tut_tab1, r.r_slider_tut_tab1)
            screen.blit(i.slider_tut_tab2, r.r_slider_tut_tab2)
            slider_move = [0, 0]

            load_surf = font_labels.render(str(load_val) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(gen_set[0]) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(gen_set[1]) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))

            gen1cost_surf = font_labels.render("$" + str(gen_cost[0]) + "/MW", False, (0, 0, 0))
            screen.blit(gen1cost_surf, (412, 100))
            gen2cost_surf = font_labels.render("$" + str(gen_cost[1]) + "/MW", False, (0, 0, 0))
            screen.blit(gen2cost_surf, (1012, 100))

            cost_total = round(gen_set[0] * gen_cost[0] + gen_set[1] * gen_cost[1], 1)
            cost_surf = font_info.render("$" + str(cost_total), False, (0, 0, 0))
            screen.blit(cost_surf, r.r_cost)

            p_imbalance = round(gen_set[0] + gen_set[1] - load_val, 1)
            if p_imbalance == 0:
                p_imbalance_color = (0, 255, 0)
                if cost_total == 1750:
                    is_pf_success = 1
                else:
                    is_pf_success = 2
                print(is_pf_success)
            else:
                p_imbalance_color = (255, 0, 0)
                is_pf_success = 0
            p_imbalance_surf = font_info.render(str(p_imbalance) + "MW", False, p_imbalance_color)
            screen.blit(p_imbalance_surf, r.r_p_imbalance)

        elif game_state == 206:
            screen.blit(i.button_run.convert_alpha(), r.r_button_run)
            screen.blit(i.mask_blackout, (0, 0))
            if current_time%2 <= 1:
                screen.blit(i.button_retry1.convert_alpha(), r.r_button_retry)
            else:
                screen.blit(i.button_retry2.convert_alpha(), r.r_button_retry)

            text_surf = font_text.render(t.text_206_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_206_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            is_slider = 0

            screen.blit(load_surf, (720, 750))
            screen.blit(gen1_surf, (412, 150))
            screen.blit(gen2_surf, (1012, 150))
            screen.blit(gen1cost_surf, (412, 100))
            screen.blit(gen2cost_surf, (1012, 100))
            screen.blit(cost_surf, (1600, 170))
            screen.blit(p_imbalance_surf, (1600, 120))

        elif game_state == 207:
            is_slider = 0

            text_surf = font_text.render(t.text_207_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            screen.blit(cost_surf, (1600, 170))
            screen.blit(p_imbalance_surf, (1600, 120))

            screen.blit(load_surf, (720, 750))
            screen.blit(gen1_surf, (412, 150))
            screen.blit(gen2_surf, (1012, 150))
            screen.blit(gen1cost_surf, (412, 100))
            screen.blit(gen2cost_surf, (1012, 100))

        elif game_state == 208:
            pf_done = 1
            is_slider = 0

            text_surf = font_text.render(t.text_208_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_208_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            screen.blit(load_surf, (720, 750))
            screen.blit(gen1_surf, (412, 150))
            screen.blit(gen2_surf, (1012, 150))
            screen.blit(gen1cost_surf, (412, 100))
            screen.blit(gen2cost_surf, (1012, 100))

            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (260, 450))

            screen.blit(cost_surf, (1600, 170))

        elif game_state == 209:
            text_surf = font_text.render(t.text_209_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_209_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_209_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(load_surf, (720, 750))
            screen.blit(gen1_surf, (412, 150))
            screen.blit(gen2_surf, (1012, 150))
            screen.blit(gen1cost_surf, (412, 100))
            screen.blit(gen2cost_surf, (1012, 100))

            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (260, 450))

        elif game_state == 210:
            text_surf = font_text.render(t.text_210_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_210_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_210_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(load_surf, (720, 750))
            screen.blit(gen1_surf, (412, 150))
            screen.blit(gen2_surf, (1012, 150))
            screen.blit(gen1cost_surf, (412, 100))
            screen.blit(gen2cost_surf, (1012, 100))

            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (260, 450))

        elif game_state == 211:
            screen.blit(i.system_tut1, r.r_system_tut1)
            screen.blit(i.mask_blackout, (0, 0))
            screen.blit(load_surf, (720, 750))
            screen.blit(gen1_surf, (412, 150))
            screen.blit(gen2_surf, (1012, 150))
            screen.blit(gen1cost_surf, (412, 100))
            screen.blit(gen2cost_surf, (1012, 100))

            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (260, 450))

            screen.blit(i.blank_textbox, r.r_blank_textbox)
            screen.blit(i.next_module, r.r_next_module)
            screen.blit(i.back_to_title, r.r_back_to_title)

            gen_set = [0, 0]

    elif game_state in range(300, 400):  # tutorial 3

        screen.fill((255, 255, 255))
        screen.blit(i.bg_10, (0, 0))
        screen.blit(i.fg_10, (0, 0))
        screen.blit(i.button_next.convert_alpha(), r.r_button_next)
        screen.blit(i.system_tut1, r.r_system_tut1)

        if game_state==300:
            text_surf = font_text.render(t.text_300_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_300_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
        elif game_state==301:
            text_surf = font_text.render(t.text_301_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_301_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_301_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)
        elif game_state==302:
            text_surf = font_text.render(t.text_302_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_302_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_302_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)
        elif game_state==303:
            text_surf = font_text.render(t.text_303_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_303_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_303_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)
        elif game_state==304:
            text_surf = font_text.render(t.text_304_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_304_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_304_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)
        elif game_state==305:
            text_surf = font_text.render(t.text_305_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_305_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_305_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)
        elif game_state==306:
            pf_done=1
            text_surf = font_text.render(t.text_306_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_306_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            load_surf = font_labels.render(str(pf_balance) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(100) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(50) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))

            load_surf = font_text.render(str('0.001+j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1630, 370))
            gen1_surf = font_text.render(str('0.003+j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1630, 415))
            gen2_surf = font_text.render(str('0.004+j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1630, 460))

            load_surf = font_text.render(str(round(line_flows[0], 1)), False, (0, 0, 0,))
            screen.blit(load_surf, (1820, 370))
            gen1_surf = font_text.render(str(round(line_flows[2], 1)), False, (0, 0, 0))
            screen.blit(gen1_surf, (1820, 415))
            gen2_surf = font_text.render(str(round(line_flows[1], 1)), False, (0, 0, 0))
            screen.blit(gen2_surf, (1820, 460))

            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (260, 450))
        elif game_state==307:
            pf_done=0
            text_surf = font_text.render(t.text_307_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_307_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_307_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)
            load_surf = font_text.render(str('0.001+j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1630, 370))
            gen1_surf = font_text.render(str('0.003+j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1630, 415))
            gen2_surf = font_text.render(str('0.004+j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1630, 460))
            load_surf = font_text.render(str(round(line_flows[0], 1)), False, (0, 0, 0,))
            screen.blit(load_surf, (1820, 370))
            gen1_surf = font_text.render(str(round(line_flows[2], 1)), False, (0, 0, 0))
            screen.blit(gen1_surf, (1820, 415))
            gen2_surf = font_text.render(str(round(line_flows[1], 1)), False, (0, 0, 0))
            screen.blit(gen2_surf, (1820, 460))

        elif game_state==308:
            text_surf = font_text.render(t.text_308_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_308_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_308_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            line_surf = font_labels.render(str('j0.006') + "p.u.", False, (0, 0, 0,))
            screen.blit(line_surf, (650, 320))
            line_surf = font_labels.render(str('j0.012') + "p.u.", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str('j0.018') + "p.u.", False, (0, 0, 0))
            screen.blit(line_surf, (200, 450))
            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))
            load_surf = font_text.render(str(round(line_flows[0], 1)), False, (0, 0, 0,))
            screen.blit(load_surf, (1820, 370))
            gen1_surf = font_text.render(str(round(line_flows[2], 1)), False, (0, 0, 0))
            screen.blit(gen1_surf, (1820, 415))
            gen2_surf = font_text.render(str(round(line_flows[1], 1)), False, (0, 0, 0))
            screen.blit(gen2_surf, (1820, 460))

        elif game_state==309:
            text_surf = font_text.render(t.text_309_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_309_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))
            load_surf = font_labels.render(str(150) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(75) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(75) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))
            screen.blit(i.choose_2, r.r_line_1_3)
            screen.blit(i.choose_3, r.r_line_2_3)
            
        elif game_state==310:
            text_surf = font_text.render(t.text_310_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))
        elif game_state==311:
            text_surf = font_text.render(t.text_311_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))
        elif game_state==312:
            text_surf = font_text.render(t.text_312_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_312_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_312_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)
            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))
        elif game_state==313:
            text_surf = font_text.render(t.text_313_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_313_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_313_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)
            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))
        elif game_state==314:
            text_surf = font_text.render(t.text_314_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_314_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_314_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)
            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))
            line_surf = font_labels.render(str('87.6') + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str('87.6') + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str('87.6') + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (250, 450))
        elif game_state==315:
            pf_done=0
            text_surf = font_text.render(t.text_315_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            screen.blit(i.button_run.convert_alpha(), r.r_button_run)
            is_slider = 1
            screen.blit(i.slider_tut1, r.r_slider_tut1)
            screen.blit(i.slider_tut2, r.r_slider_tut2)
            r.r_slider_tut_tab1.move_ip((slider_move[0], 0))
            r.r_slider_tut_tab2.move_ip((slider_move[1], 0))

            screen.blit(i.slider_tut_tab1, r.r_slider_tut_tab1)
            screen.blit(i.slider_tut_tab2, r.r_slider_tut_tab2)
            slider_move = [0, 0]

            a=round(-1/2*gen_set[1]+1/3*gen_set[0],1)
            b=round(1/2*gen_set[1]+1/3*gen_set[0],1)
            c=round(1/2*gen_set[1]+2/3*gen_set[0],1)

            load_surf = font_labels.render(str(load_val) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(gen_set[0]) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(gen_set[1]) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))    
            line_surf = font_labels.render(str(round(-1/2*gen_set[1]+1/3*gen_set[0],1)) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(1/2*gen_set[1]+1/3*gen_set[0],1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(1/2*gen_set[1]+2/3*gen_set[0],1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (250, 450))

            gen1cost_surf = font_labels.render("$" + str(gen_cost[0]) + "/MW", False, (0, 0, 0))
            screen.blit(gen1cost_surf, (412, 100))
            gen2cost_surf = font_labels.render("$" + str(gen_cost[1]) + "/MW", False, (0, 0, 0))
            screen.blit(gen2cost_surf, (1012, 100))

            cost_total = round(gen_set[0] * gen_cost[0] + gen_set[1] * gen_cost[1], 1)
            cost_surf = font_info.render("$" + str(cost_total), False, (0, 0, 0))
            screen.blit(cost_surf, r.r_cost)
            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))
            p_imbalance = round(gen_set[0] + gen_set[1] - load_val, 1)
            if p_imbalance == 0:
                p_imbalance_color = (0, 255, 0)
                if a>87.6 or b>87.6 or c>87.6:
                    is_pf_success=3
                elif cost_total<=1880:
                    is_pf_success=2
                else:
                    is_pf_success=4
            else:
                p_imbalance_color = (255, 0, 0)
                is_pf_success = 0
            p_imbalance_surf = font_info.render(str(p_imbalance) + "MW", False, p_imbalance_color)
            screen.blit(p_imbalance_surf, r.r_p_imbalance)

        elif game_state==316:
            text_surf = font_text.render(t.text_316_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_316_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))
        elif game_state==317:
            text_surf = font_text.render(t.text_317_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_317_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_317_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))
            load_surf = font_text.render(str(round(line_flows[0], 1)), False, (0, 0, 0,))
            screen.blit(load_surf, (1820, 370))
            gen1_surf = font_text.render(str(round(line_flows[2], 1)), False, (250, 0, 0))
            screen.blit(gen1_surf, (1820, 415))
            gen2_surf = font_text.render(str(round(line_flows[1], 1)), False, (0, 0, 0))
            screen.blit(gen2_surf, (1820, 460))

        elif game_state==318:
            text_surf = font_text.render(t.text_318_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_318_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_318_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)
            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))
        elif game_state==319:
            text_surf = font_text.render(t.text_319_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_319_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))
            load_surf = font_text.render(str(round(line_flows[0], 1)), False, (0, 0, 0,))
            screen.blit(load_surf, (1820, 370))
            gen1_surf = font_text.render(str(round(line_flows[2], 1)), False, (0, 0, 0))
            screen.blit(gen1_surf, (1820, 415))
            gen2_surf = font_text.render(str(round(line_flows[1], 1)), False, (0, 0, 0))
            screen.blit(gen2_surf, (1820, 460))
        elif game_state==320:
            text_surf = font_text.render(t.text_320_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_320_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_320_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)
            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))

    elif game_state in range(400, 500):  # tutorial 4
        pass
    elif game_state in range(500, 600):  # game - daily
        pass
    elif game_state in range(600, 700):  # game - monthly
        if game_state == 600:
            # Render new map every time
            screen.fill((255, 255, 255))
            screen.blit(i.bg_20, (0, 0))

            for plant in map:
                plant_image = choose_image(map[plant]['type'])
                plant_rect = choose_rect(plant)
                screen.blit(plant_image, plant_rect)

        if game_state == 601:
            # Create sidebar
            sidebar = pygame.Surface((300, screen_height))
            sidebar.set_alpha(128)
            sidebar.fill((255, 255, 255))
            screen.blit(sidebar, (0, 0))

            screen.blit(i.plant_hydro, r.button_hydro)
            screen.blit(i.plant_wind, r.button_wind)
            screen.blit(i.plant_solar, r.button_solar)
            screen.blit(i.plant_nuclear, r.button_nuclear)
            screen.blit(i.plant_coal, r.button_coal)
            screen.blit(i.plant_gas, r.button_gas)

        elif game_state == 602:
            pass

    elif game_state in range(700, 800):  # options
        pass
    #  display and UI end
    else:
        pygame.quit()
        exit()

    current_time = round(pygame.time.get_ticks()/1000, 1)   # display time on the right, for testing purposes
    time_surf = font_default.render(str(current_time), False, (0, 0, 0))
    screen.blit(time_surf, (20, 20))

    pygame.display.update()
    clock.tick(30)


