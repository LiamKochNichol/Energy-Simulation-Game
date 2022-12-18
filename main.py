# import random
import pygame
import select_step as s
import images as i
import rects as r
import text as t
import panda_power as p
from sys import exit
from map import map, loads, choose_image, choose_rect

pygame.init()
pygame.font.init()
font_default = pygame.font.SysFont('timesnewroman', 48)
font_text = pygame.font.SysFont('timesnewroman', 30)
font_labels = pygame.font.SysFont('timesnewroman',40, bold=True)
font_info = pygame.font.SysFont('timesnewroman',36, bold=True)
font_info_tut5 = pygame.font.SysFont('timesnewroman',36)

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
gen_set_wind = 70 * 5
gen_cost = [10, 15]
line_flows = [0, 0, 0]
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
            if event.type == pygame.MOUSEBUTTONDOWN and r.r_slider_tut_tab1.collidepoint(event.pos):
                drag_tabs[0] = 1
                drag_start = event.pos[0]
            if event.type == pygame.MOUSEMOTION and drag_tabs[0] == 1:
                slider_move[0] = max(950, min(1450, event.pos[0])) - r.r_slider_tut_tab1.centerx
                gen_set[0] = int(round(100 * (r.r_slider_tut_tab1.centerx - 950) / (1450 - 950), 0))
            if event.type == pygame.MOUSEBUTTONUP:
                drag_tabs[0] = 0
            if event.type == pygame.MOUSEBUTTONDOWN and r.r_slider_tut_tab2.collidepoint(event.pos):
                drag_tabs[1] = 1
                drag_start = event.pos[0]
            if event.type == pygame.MOUSEMOTION and drag_tabs[1] == 1:
                slider_move[1] = max(950, min(1450, event.pos[0])) - r.r_slider_tut_tab2.centerx
                gen_set[1] = int(round(100 * (r.r_slider_tut_tab2.centerx - 950) / (1450 - 950), 0))
            if event.type == pygame.MOUSEBUTTONUP:
                drag_tabs[1] = 0

        if game_state == 111 and pf_done != 1:
            line_flows = p.PF_tut1(gen_set)
        elif game_state == 208 and pf_done != 1:
            line_flows = p.PF_tut1(gen_set)
        elif game_state == 305 and pf_done !=1:
            line_flows = p.PF_tut3_loss([50])[0]
            line_ratings = p.PF_tut3_loss([50])[1]
        elif game_state == 408 and pf_done !=1:
            gen_set[0] = 65
            gen_set[1] = 150 - gen_set[0]
            line_flows[0] = round(-1 / 2 * gen_set[1] + 1 / 3 * gen_set[0], 1)
            line_flows[1] = round(1 / 2 * gen_set[1] + 1 / 3 * gen_set[0], 1)
            line_flows[2] = round(1 / 2 * gen_set[1] + 2 / 3 * gen_set[0], 1)

        elif game_state == 412 and pf_done !=1:
            gen_set[0] = 85
            gen_set[1] = 150 - gen_set[0]
            line_flows[0] = round(-1 / 2 * gen_set[1] + 1 / 3 * gen_set[0], 1)
            line_flows[1] = round(1 / 2 * gen_set[1] + 1 / 3 * gen_set[0], 1)
            line_flows[2] = round(1 / 2 * gen_set[1] + 2 / 3 * gen_set[0], 1)


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
        screen.blit(i.table_1, r.r_table_1)
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
            is_slider = 1
            screen.blit(i.system_tut1, r.r_system_tut1)
            screen.blit(i.button_run.convert_alpha(), r.r_button_run)

            text_surf = font_text.render(t.text_109_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_109_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            screen.blit(i.slider_tut1, r.r_slider_tut1)
            screen.blit(i.slider_tut2, r.r_slider_tut2)
            r.r_slider_tut_tab1.move_ip((slider_move[0], 0))
            r.r_slider_tut_tab2.move_ip((slider_move[1], 0))
            screen.blit(i.slider_tut_tab1, r.r_slider_tut_tab1)
            screen.blit(i.slider_tut_tab2, r.r_slider_tut_tab2)
            slider_move = [0, 0]
            screen.blit(i.gen_min, (920, 790))
            screen.blit(i.gen_max, (1410, 790))
            screen.blit(i.gen_min, (920, 865))
            screen.blit(i.gen_max, (1410, 865))

            load_surf = font_labels.render(str(load_val) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(gen_set[0]) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(gen_set[1]) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))

            p_imbalance = gen_set[0] + gen_set[1] - load_val
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

            if line_flows[0] > 0:
                screen.blit(i.line_12_pos, r.r_line_12)
            elif line_flows[0] < 0:
                screen.blit(i.line_12_neg, r.r_line_12)
            else:
                pass
            if line_flows[1] > 0:
                screen.blit(i.line_23_pos, r.r_line_23)
            elif line_flows[1] < 0:
                screen.blit(i.line_23_neg, r.r_line_23)
            else:
                pass
            if line_flows[2] > 0:
                screen.blit(i.line_13_pos, r.r_line_13)
            elif line_flows[2] < 0:
                screen.blit(i.line_13_neg, r.r_line_13)
            else:
                pass

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

            if line_flows[0] > 0:
                screen.blit(i.line_12_pos, r.r_line_12)
            elif line_flows[0] < 0:
                screen.blit(i.line_12_neg, r.r_line_12)
            else:
                pass
            if line_flows[1] > 0:
                screen.blit(i.line_23_pos, r.r_line_23)
            elif line_flows[1] < 0:
                screen.blit(i.line_23_neg, r.r_line_23)
            else:
                pass
            if line_flows[2] > 0:
                screen.blit(i.line_13_pos, r.r_line_13)
            elif line_flows[2] < 0:
                screen.blit(i.line_13_neg, r.r_line_13)
            else:
                pass

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
            screen.blit(load_surf, (720, 750))
            screen.blit(gen1_surf, (412, 150))
            screen.blit(gen2_surf, (1012, 150))

            if line_flows[0] > 0:
                screen.blit(i.line_12_pos, r.r_line_12)
            elif line_flows[0] < 0:
                screen.blit(i.line_12_neg, r.r_line_12)
            else:
                pass
            if line_flows[1] > 0:
                screen.blit(i.line_23_pos, r.r_line_23)
            elif line_flows[1] < 0:
                screen.blit(i.line_23_neg, r.r_line_23)
            else:
                pass
            if line_flows[2] > 0:
                screen.blit(i.line_13_pos, r.r_line_13)
            elif line_flows[2] < 0:
                screen.blit(i.line_13_neg, r.r_line_13)
            else:
                pass

            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (260, 450))

            screen.blit(i.mask_blackout, (0, 0))
            screen.blit(i.blank_textbox, r.r_blank_textbox)
            screen.blit(i.next_module, r.r_next_module)
            screen.blit(i.back_to_title, r.r_back_to_title)

            pf_done = 0
            gen_set = [0, 0]
            r.r_slider_tut_tab1 = i.slider_tut_tab1.get_rect(center=(950, 762))
            r.r_slider_tut_tab2 = i.slider_tut_tab2.get_rect(center=(950, 837))

    elif game_state in range(200, 300):  # tutorial 2
        screen.fill((255, 255, 255))
        screen.blit(i.bg_10, (0, 0))
        screen.blit(i.fg_10, (0, 0))
        screen.blit(i.system_tut1, r.r_system_tut1)
        screen.blit(i.button_next.convert_alpha(), r.r_button_next)
        screen.blit(i.table_1,r.r_table_1)

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
            is_slider = 1
            screen.blit(i.button_run.convert_alpha(), r.r_button_run)

            text_surf = font_text.render(t.text_205_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_205_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            screen.blit(i.slider_tut1, r.r_slider_tut1)
            screen.blit(i.slider_tut2, r.r_slider_tut2)
            r.r_slider_tut_tab1.move_ip((slider_move[0], 0))
            r.r_slider_tut_tab2.move_ip((slider_move[1], 0))
            screen.blit(i.slider_tut_tab1, r.r_slider_tut_tab1)
            screen.blit(i.slider_tut_tab2, r.r_slider_tut_tab2)
            slider_move = [0, 0]
            screen.blit(i.gen_min, (920, 790))
            screen.blit(i.gen_max, (1410, 790))
            screen.blit(i.gen_min, (920, 865))
            screen.blit(i.gen_max, (1410, 865))

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
            screen.blit(cost_surf, r.r_cost)
            screen.blit(p_imbalance_surf, r.r_p_imbalance)

        elif game_state == 207:
            is_slider = 0

            text_surf = font_text.render(t.text_207_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            screen.blit(cost_surf, r.r_cost)
            screen.blit(p_imbalance_surf, r.r_p_imbalance)

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
            screen.blit(cost_surf, r.r_cost)

            if line_flows[0] > 0:
                screen.blit(i.line_12_pos, r.r_line_12)
            elif line_flows[0] < 0:
                screen.blit(i.line_12_neg, r.r_line_12)
            else:
                pass
            if line_flows[1] > 0:
                screen.blit(i.line_23_pos, r.r_line_23)
            elif line_flows[1] < 0:
                screen.blit(i.line_23_neg, r.r_line_23)
            else:
                pass
            if line_flows[2] > 0:
                screen.blit(i.line_13_pos, r.r_line_13)
            elif line_flows[2] < 0:
                screen.blit(i.line_13_neg, r.r_line_13)
            else:
                pass

            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (260, 450))

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
            screen.blit(cost_surf, r.r_cost)

            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (260, 450))
            if line_flows[0] > 0:
                screen.blit(i.line_12_pos, r.r_line_12)
            elif line_flows[0] < 0:
                screen.blit(i.line_12_neg, r.r_line_12)
            else:
                pass
            if line_flows[1] > 0:
                screen.blit(i.line_23_pos, r.r_line_23)
            elif line_flows[1] < 0:
                screen.blit(i.line_23_neg, r.r_line_23)
            else:
                pass
            if line_flows[2] > 0:
                screen.blit(i.line_13_pos, r.r_line_13)
            elif line_flows[2] < 0:
                screen.blit(i.line_13_neg, r.r_line_13)
            else:
                pass

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
            screen.blit(cost_surf, r.r_cost)

            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (260, 450))
            if line_flows[0] > 0:
                screen.blit(i.line_12_pos, r.r_line_12)
            elif line_flows[0] < 0:
                screen.blit(i.line_12_neg, r.r_line_12)
            else:
                pass
            if line_flows[1] > 0:
                screen.blit(i.line_23_pos, r.r_line_23)
            elif line_flows[1] < 0:
                screen.blit(i.line_23_neg, r.r_line_23)
            else:
                pass
            if line_flows[2] > 0:
                screen.blit(i.line_13_pos, r.r_line_13)
            elif line_flows[2] < 0:
                screen.blit(i.line_13_neg, r.r_line_13)
            else:
                pass

        elif game_state == 211:
            screen.blit(i.system_tut1, r.r_system_tut1)
            screen.blit(load_surf, (720, 750))
            screen.blit(gen1_surf, (412, 150))
            screen.blit(gen2_surf, (1012, 150))
            screen.blit(gen1cost_surf, (412, 100))
            screen.blit(gen2cost_surf, (1012, 100))
            screen.blit(cost_surf, r.r_cost)

            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (260, 450))
            if line_flows[0] > 0:
                screen.blit(i.line_12_pos, r.r_line_12)
            elif line_flows[0] < 0:
                screen.blit(i.line_12_neg, r.r_line_12)
            else:
                pass
            if line_flows[1] > 0:
                screen.blit(i.line_23_pos, r.r_line_23)
            elif line_flows[1] < 0:
                screen.blit(i.line_23_neg, r.r_line_23)
            else:
                pass
            if line_flows[2] > 0:
                screen.blit(i.line_13_pos, r.r_line_13)
            elif line_flows[2] < 0:
                screen.blit(i.line_13_neg, r.r_line_13)
            else:
                pass

            screen.blit(i.mask_blackout, (0, 0))
            screen.blit(i.blank_textbox, r.r_blank_textbox)
            screen.blit(i.next_module, r.r_next_module)
            screen.blit(i.back_to_title, r.r_back_to_title)

            gen_set = [0, 0]
            r.r_slider_tut_tab1 = i.slider_tut_tab1.get_rect(center=(950, 762))
            r.r_slider_tut_tab2 = i.slider_tut_tab2.get_rect(center=(950, 837))

    elif game_state in range(300, 400):  # tutorial 3

        screen.fill((255, 255, 255))
        screen.blit(i.bg_10, (0, 0))
        screen.blit(i.fg_10, (0, 0))
        screen.blit(i.button_next.convert_alpha(), r.r_button_next)
        screen.blit(i.system_tut1, r.r_system_tut1)
        screen.blit(i.table_1, r.r_table_1)
        screen.blit(i.table_2, r.r_table_2)

        if game_state == 300:
            text_surf = font_text.render(t.text_300_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_300_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        elif game_state == 301:
            text_surf = font_text.render(t.text_301_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_301_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_301_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)
            screen.blit(i.diagram_line,r.r_diagram_line)

        elif game_state == 302:
            text_surf = font_text.render(t.text_302_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_302_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_302_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

        elif game_state == 303:
            text_surf = font_text.render(t.text_303_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_303_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_303_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

        elif game_state == 304:
            text_surf = font_text.render(t.text_304_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_304_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_304_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)
            screen.blit(i.diagram_RL, r.r_diagram_RL)

        elif game_state == 305:
            pf_done= 1
            text_surf = font_text.render(t.text_305_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_305_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_305_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

        elif game_state == 306:

            text_surf = font_text.render(t.text_306_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_306_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            load_surf = font_labels.render(str(150) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(p.PF_tut3_loss([50])[2]) + "MW", False, (0, 0, 0))
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

            if line_flows[0] > 0:
                screen.blit(i.line_12_pos, r.r_line_12)
            elif line_flows[0] < 0:
                screen.blit(i.line_12_neg, r.r_line_12)
            else:
                pass
            if line_flows[1] > 0:
                screen.blit(i.line_23_pos, r.r_line_23)
            elif line_flows[1] < 0:
                screen.blit(i.line_23_neg, r.r_line_23)
            else:
                pass
            if line_flows[2] > 0:
                screen.blit(i.line_13_pos, r.r_line_13)
            elif line_flows[2] < 0:
                screen.blit(i.line_13_neg, r.r_line_13)
            else:
                pass

            cost_total = round(p.PF_tut3_loss([50])[2] * gen_cost[0] + 50 * gen_cost[1], 1)
            cost_surf = font_info.render("$" + str(cost_total), False, (0, 0, 0))
            screen.blit(cost_surf, r.r_cost)

        elif game_state == 307:
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

        elif game_state == 308:
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

        elif game_state == 309:
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
            screen.blit(i.button_choose_line, r.r_line_1_3)
            screen.blit(i.button_choose_line, r.r_line_2_3)
            
        elif game_state == 310:
            text_surf = font_text.render(t.text_310_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))

        elif game_state == 311:
            text_surf = font_text.render(t.text_311_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))

        elif game_state == 312:
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

        elif game_state == 313:
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

        elif game_state == 314:
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

        elif game_state == 315:
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
            screen.blit(i.gen_min, (920, 790))
            screen.blit(i.gen_max, (1410, 790))
            screen.blit(i.gen_min, (920, 865))
            screen.blit(i.gen_max, (1410, 865))

            line_flows[0]=round(-1/2*gen_set[1]+1/3*gen_set[0],1)
            line_flows[1]=round(1/2*gen_set[1]+1/3*gen_set[0],1)
            line_flows[2]=round(1/2*gen_set[1]+2/3*gen_set[0],1)

            load_surf = font_labels.render(str(load_val) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(gen_set[0]) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(gen_set[1]) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))    

            line_surf = font_labels.render(str(abs(round(-1/2*gen_set[1]+1/3*gen_set[0],1))) + " / 87.6MW", False, (0, 0, 0,))
            screen.blit(line_surf, (620, 320))
            line_surf = font_labels.render(str(round(1/2*gen_set[1]+1/3*gen_set[0],1)) + " / 87.6MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(1/2*gen_set[1]+2/3*gen_set[0],1)) + " / 87.6MW", False, (0, 0, 0))
            screen.blit(line_surf, (150, 450))

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
                if line_flows[0]>87.6 or line_flows[1]>87.6 or line_flows[2]>87.6:
                    is_pf_success=3
                elif cost_total == 1875:
                    is_pf_success=2
                else:
                    is_pf_success=4
            else:
                p_imbalance_color = (255, 0, 0)
                is_pf_success = 0
            p_imbalance_surf = font_info.render(str(p_imbalance) + "MW", False, p_imbalance_color)
            screen.blit(p_imbalance_surf, r.r_p_imbalance)

        elif game_state == 316:
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

        elif game_state == 317:
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
            load_surf = font_text.render(str(abs(round(line_flows[0], 1))), False, (0, 0, 0,))
            screen.blit(load_surf, (1820, 370))
            gen1_surf = font_text.render(str(round(line_flows[2], 1)), False, (250, 0, 0))
            screen.blit(gen1_surf, (1820, 415))
            gen2_surf = font_text.render(str(round(line_flows[1], 1)), False, (0, 0, 0))
            screen.blit(gen2_surf, (1820, 460))
            if line_flows[0] > 0:
                screen.blit(i.line_12_pos, r.r_line_12)
            elif line_flows[0] < 0:
                screen.blit(i.line_12_neg, r.r_line_12)
            else:
                pass
            if line_flows[1] > 0:
                screen.blit(i.line_23_pos, r.r_line_23)
            elif line_flows[1] < 0:
                screen.blit(i.line_23_neg, r.r_line_23)
            else:
                pass
            if line_flows[2] > 0:
                screen.blit(i.line_13_pos, r.r_line_13)
            elif line_flows[2] < 0:
                screen.blit(i.line_13_neg, r.r_line_13)
            else:
                pass

        elif game_state == 318:
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

        elif game_state == 319:
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
            load_surf = font_text.render(str(abs(round(line_flows[0], 1))), False, (0, 0, 0,))
            screen.blit(load_surf, (1820, 370))
            gen1_surf = font_text.render(str(round(line_flows[2], 1)), False, (0, 0, 0))
            screen.blit(gen1_surf, (1820, 415))
            gen2_surf = font_text.render(str(round(line_flows[1], 1)), False, (0, 0, 0))
            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (250, 450))
            screen.blit(gen2_surf, (1820, 460))
            if line_flows[0] > 0:
                screen.blit(i.line_12_pos, r.r_line_12)
            elif line_flows[0] < 0:
                screen.blit(i.line_12_neg, r.r_line_12)
            else:
                pass
            if line_flows[1] > 0:
                screen.blit(i.line_23_pos, r.r_line_23)
            elif line_flows[1] < 0:
                screen.blit(i.line_23_neg, r.r_line_23)
            else:
                pass
            if line_flows[2] > 0:
                screen.blit(i.line_13_pos, r.r_line_13)
            elif line_flows[2] < 0:
                screen.blit(i.line_13_neg, r.r_line_13)
            else:
                pass

        elif game_state == 320:
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
            load_surf = font_text.render(str(round(line_flows[0], 1)), False, (0, 0, 0,))
            screen.blit(load_surf, (1820, 370))
            gen1_surf = font_text.render(str(round(line_flows[2], 1)), False, (0, 0, 0))
            screen.blit(gen1_surf, (1820, 415))
            gen2_surf = font_text.render(str(round(line_flows[1], 1)), False, (0, 0, 0))
            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (250, 450))
            screen.blit(gen2_surf, (1820, 460))
            if line_flows[0] > 0:
                screen.blit(i.line_12_pos, r.r_line_12)
            elif line_flows[0] < 0:
                screen.blit(i.line_12_neg, r.r_line_12)
            else:
                pass
            if line_flows[1] > 0:
                screen.blit(i.line_23_pos, r.r_line_23)
            elif line_flows[1] < 0:
                screen.blit(i.line_23_neg, r.r_line_23)
            else:
                pass
            if line_flows[2] > 0:
                screen.blit(i.line_13_pos, r.r_line_13)
            elif line_flows[2] < 0:
                screen.blit(i.line_13_neg, r.r_line_13)
            else:
                pass
        elif game_state == 321:

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
            line_surf = font_labels.render(str(round(line_flows[0], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (700, 320))
            line_surf = font_labels.render(str(round(line_flows[1], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(line_flows[2], 1)) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (250, 450))
            screen.blit(gen2_surf, (1820, 460))
            if line_flows[0] > 0:
                screen.blit(i.line_12_pos, r.r_line_12)
            elif line_flows[0] < 0:
                screen.blit(i.line_12_neg, r.r_line_12)
            else:
                pass
            if line_flows[1] > 0:
                screen.blit(i.line_23_pos, r.r_line_23)
            elif line_flows[1] < 0:
                screen.blit(i.line_23_neg, r.r_line_23)
            else:
                pass
            if line_flows[2] > 0:
                screen.blit(i.line_13_pos, r.r_line_13)
            elif line_flows[2] < 0:
                screen.blit(i.line_13_neg, r.r_line_13)
            else:
                pass
            screen.blit(i.mask_blackout, (0, 0))
            screen.blit(i.blank_textbox, r.r_blank_textbox)
            screen.blit(i.next_module, r.r_next_module)
            screen.blit(i.back_to_title, r.r_back_to_title)

            gen_set = [0, 0]
            r.r_slider_tut_tab1 = i.slider_tut_tab1.get_rect(center=(950, 762))
            r.r_slider_tut_tab2 = i.slider_tut_tab2.get_rect(center=(950, 837))

    elif game_state in range(400, 500):  # tutorial 4

        screen.fill((255, 255, 255))
        screen.blit(i.bg_10, (0, 0))
        screen.blit(i.fg_10, (0, 0))
        screen.blit(i.button_next.convert_alpha(), r.r_button_next)
        screen.blit(i.system_tut1, r.r_system_tut1)
        screen.blit(i.table_1, r.r_table_1)
        screen.blit(i.table_2, r.r_table_2)
        screen.blit(i.table_3, r.r_table_3)

        if game_state == 400:
            text_surf = font_text.render(t.text_400_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_400_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        if game_state == 401:
            text_surf = font_text.render(t.text_401_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_401_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        if game_state == 402:
            text_surf = font_text.render(t.text_402_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_402_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        if game_state == 403:
            text_surf = font_text.render(t.text_403_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_403_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        if game_state == 404:
            text_surf = font_text.render(t.text_404_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_404_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            screen.blit(i.wind_fig, r.r_wind_fig)

        if game_state == 405:
            screen.blit(i.gen_wind, r.r_gen1_tut1)

            text_surf = font_text.render(t.text_405_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_405_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            is_slider = 0
            gen_set_wind = 0
            screen.blit(i.slider_tut1, r.r_slider_tut1)
            screen.blit(i.slider_tut2, r.r_slider_tut2)
            screen.blit(i.slider_wind_10, r.r_slider_wind_10)
            screen.blit(i.slider_tut_tab2, r.r_slider_tut_tab2)
            screen.blit(i.gen_min, (920, 790))
            screen.blit(i.gen_max, (1410, 790))
            screen.blit(i.gen_min, (920, 865))
            screen.blit(i.gen_max, (1410, 865))
            screen.blit(i.label_wind_10, (1255, 790))

            wind_forecast_surf = font_info.render(str(70) + "MW", False, (0, 0, 0))
            screen.blit(wind_forecast_surf, r.r_wind_forecast)

        elif game_state == 406:
            screen.blit(i.gen_wind, r.r_gen1_tut1)

            text_surf = font_text.render(t.text_406_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_406_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            pf_done = 0
            screen.blit(i.button_run.convert_alpha(), r.r_button_run)
            is_slider = 1
            screen.blit(i.slider_tut1, r.r_slider_tut1)
            screen.blit(i.slider_tut2, r.r_slider_tut2)
            r.r_slider_tut_tab2.move_ip((slider_move[1], 0))
            screen.blit(i.slider_wind_10, r.r_slider_wind_10)
            screen.blit(i.slider_tut_tab2, r.r_slider_tut_tab2)
            slider_move = [0, 0]
            screen.blit(i.gen_min, (920, 790))
            screen.blit(i.gen_max, (1410, 790))
            screen.blit(i.gen_min, (920, 865))
            screen.blit(i.gen_max, (1410, 865))
            screen.blit(i.label_wind_10, (1255, 790))

            gen_set[0] = 70
            gen_cost[0] = 8

            load_surf = font_labels.render(str(load_val) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(gen_set[0]) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(gen_set[1]) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))

            line_surf = font_labels.render(str(abs(round(-1 / 2 * gen_set[1] + 1 / 3 * gen_set[0], 1))) + " / 87.6MW", False, (0, 0, 0,))
            screen.blit(line_surf, (620, 320))
            line_surf = font_labels.render(str(round(1 / 2 * gen_set[1] + 1 / 3 * gen_set[0], 1)) + " / 87.6MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(round(1 / 2 * gen_set[1] + 2 / 3 * gen_set[0], 1)) + " / 87.6MW", False, (0, 0, 0))
            screen.blit(line_surf, (150, 450))

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
                is_pf_success = 1
            else:
                p_imbalance_color = (255, 0, 0)
                is_pf_success = 0
            p_imbalance_surf = font_info.render(str(p_imbalance) + "MW", False, p_imbalance_color)
            screen.blit(p_imbalance_surf, r.r_p_imbalance)
            wind_forecast_surf = font_info.render(str(70) + "MW", False, (0, 0, 0))
            screen.blit(wind_forecast_surf, r.r_wind_forecast)

        elif game_state == 407:
            is_slider = 0
            screen.blit(i.gen_wind, r.r_gen1_tut1)
            text_surf = font_text.render(t.text_407_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_407_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            screen.blit(cost_surf, r.r_cost)
            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))
            screen.blit(p_imbalance_surf, r.r_p_imbalance)
            screen.blit(i.mask_blackout, (0, 0))

            wind_forecast_surf = font_info.render(str(70) + "MW", False, (0, 0, 0))
            screen.blit(wind_forecast_surf, r.r_wind_forecast)

        elif game_state == 408:
            pf_done = 1
            is_slider = 0
            screen.blit(i.gen_wind, r.r_gen1_tut1)
            text_surf = font_text.render(t.text_408_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_408_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_408_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            r_redispatch_tab = r.r_slider_tut_tab2.move((25, 0))
            screen.blit(i.slider_tut1, r.r_slider_tut1)
            screen.blit(i.slider_tut2, r.r_slider_tut2)
            screen.blit(i.slider_wind_10, r.r_slider_wind_10)
            screen.blit(i.slider_tut_tab2, r_redispatch_tab)
            screen.blit(i.gen_min, (920, 790))
            screen.blit(i.gen_max, (1410, 790))
            screen.blit(i.gen_min, (920, 865))
            screen.blit(i.gen_max, (1410, 865))
            screen.blit(i.label_wind_actual1, (1235, 790))
            screen.blit(i.slider_wind_actual, r.r_slider_wind_actual1)

            line_surf = font_labels.render(str(abs(line_flows[0])) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (620, 320))
            line_surf = font_labels.render(str(line_flows[1]) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(line_flows[2]) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (150, 450))

            load_surf = font_text.render(str(round(line_flows[0], 1)), False, (0, 0, 0,))
            screen.blit(load_surf, (1820, 370))
            gen1_surf = font_text.render(str(round(line_flows[2], 1)), False, (0, 0, 0))
            screen.blit(gen1_surf, (1820, 415))
            gen2_surf = font_text.render(str(round(line_flows[1], 1)), False, (0, 0, 0))
            screen.blit(gen2_surf, (1820, 460))

            load_surf = font_labels.render(str(load_val) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(gen_set[0]) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(gen_set[1]) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))

            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))

            if line_flows[0] > 0:
                screen.blit(i.line_12_pos, r.r_line_12)
            elif line_flows[0] < 0:
                screen.blit(i.line_12_neg, r.r_line_12)
            else:
                pass
            if line_flows[1] > 0:
                screen.blit(i.line_23_pos, r.r_line_23)
            elif line_flows[1] < 0:
                screen.blit(i.line_23_neg, r.r_line_23)
            else:
                pass
            if line_flows[2] > 0:
                screen.blit(i.line_13_pos, r.r_line_13)
            elif line_flows[2] < 0:
                screen.blit(i.line_13_neg, r.r_line_13)
            else:
                pass

            screen.blit(cost_surf, r.r_cost)
            wind_forecast_surf = font_info.render(str(70) + "MW", False, (0, 0, 0))
            screen.blit(wind_forecast_surf, r.r_wind_forecast)
            wind_output_surf = font_info.render(str(65) + "MW", False, (0, 0, 0))
            screen.blit(wind_output_surf, r.r_wind_output)

        elif game_state == 409:
            screen.blit(i.gen_wind, r.r_gen1_tut1)
            text_surf = font_text.render(t.text_409_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_409_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            screen.blit(i.button_run.convert_alpha(), r.r_button_run)
            is_slider = 0
            screen.blit(i.slider_tut1, r.r_slider_tut1)
            screen.blit(i.slider_tut2, r.r_slider_tut2)
            screen.blit(i.slider_wind_25, r.r_slider_wind_25)
            screen.blit(i.slider_tut_tab2, r.r_slider_tut_tab2)
            screen.blit(i.gen_min, (920, 790))
            screen.blit(i.gen_max, (1410, 790))
            screen.blit(i.gen_min, (920, 865))
            screen.blit(i.gen_max, (1410, 865))
            screen.blit(i.label_wind_25, (1255, 790))

            load_surf = font_labels.render(str(load_val) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(70) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(80) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))

            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))

            screen.blit(cost_surf, r.r_cost)
            wind_forecast_surf = font_info.render(str(70) + "MW", False, (0, 0, 0))
            screen.blit(wind_forecast_surf, r.r_wind_forecast)

        elif game_state == 410:
            screen.blit(i.gen_wind, r.r_gen1_tut1)
            text_surf = font_text.render(t.text_410_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_410_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_410_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            r_redispatch_tab = r.r_slider_tut_tab2.move((100, 0))
            screen.blit(i.slider_tut1, r.r_slider_tut1)
            screen.blit(i.slider_tut2, r.r_slider_tut2)
            screen.blit(i.slider_wind_25, r.r_slider_wind_25)
            screen.blit(i.slider_tut_tab2, r_redispatch_tab)
            screen.blit(i.gen_min, (920, 790))
            screen.blit(i.gen_max, (1410, 790))
            screen.blit(i.gen_min, (920, 865))
            screen.blit(i.gen_max, (1410, 865))
            screen.blit(i.label_wind_actual2, (1155, 790))
            screen.blit(i.slider_wind_actual, r.r_slider_wind_actual2)

            load_surf = font_labels.render(str(load_val) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(45) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(100) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))

            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))

            if line_flows[0] > 0:
                screen.blit(i.line_12_pos, r.r_line_12)
            elif line_flows[0] < 0:
                screen.blit(i.line_12_neg, r.r_line_12)
            else:
                pass
            if line_flows[1] > 0:
                screen.blit(i.line_23_pos, r.r_line_23)
            elif line_flows[1] < 0:
                screen.blit(i.line_23_neg, r.r_line_23)
            else:
                pass
            if line_flows[2] > 0:
                screen.blit(i.line_13_pos, r.r_line_13)
            elif line_flows[2] < 0:
                screen.blit(i.line_13_neg, r.r_line_13)
            else:
                pass

            p_imbalance = round(45 + 100 - load_val, 1)
            p_imbalance_color = (255, 0, 0)
            p_imbalance_surf = font_info.render(str(p_imbalance) + "MW", False, p_imbalance_color)
            screen.blit(p_imbalance_surf, r.r_p_imbalance)

            wind_forecast_surf = font_info.render(str(70) + "MW", False, (0, 0, 0))
            screen.blit(wind_forecast_surf, r.r_wind_forecast)
            wind_output_surf = font_info.render(str(45) + "MW", False, (0, 0, 0))
            screen.blit(wind_output_surf, r.r_wind_output)

        elif game_state == 411:
            pf_done = 0
            screen.blit(i.gen_wind, r.r_gen1_tut1)
            text_surf = font_text.render(t.text_411_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)

            screen.blit(i.button_run.convert_alpha(), r.r_button_run)
            is_slider = 0
            screen.blit(i.slider_tut1, r.r_slider_tut1)
            screen.blit(i.slider_tut2, r.r_slider_tut2)
            screen.blit(i.slider_wind_25, r.r_slider_wind_25)
            screen.blit(i.slider_tut_tab2, r.r_slider_tut_tab2)
            screen.blit(i.gen_min, (920, 790))
            screen.blit(i.gen_max, (1410, 790))
            screen.blit(i.gen_min, (920, 865))
            screen.blit(i.gen_max, (1410, 865))
            screen.blit(i.label_wind_25, (1255, 790))

            load_surf = font_labels.render(str(load_val) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(70) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(80) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))

            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))

            wind_forecast_surf = font_info.render(str(70) + "MW", False, (0, 0, 0))
            screen.blit(wind_forecast_surf, r.r_wind_forecast)

        elif game_state == 412:
            pf_done = 1
            is_slider = 0
            screen.blit(i.gen_wind, r.r_gen1_tut1)
            text_surf = font_text.render(t.text_412_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_412_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_412_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            r_redispatch_tab = r.r_slider_tut_tab2.move((-50, 0))
            screen.blit(i.slider_tut1, r.r_slider_tut1)
            screen.blit(i.slider_tut2, r.r_slider_tut2)
            screen.blit(i.slider_wind_25, r.r_slider_wind_25)
            screen.blit(i.slider_tut_tab2, r_redispatch_tab)
            screen.blit(i.gen_min, (920, 790))
            screen.blit(i.gen_max, (1410, 790))
            screen.blit(i.gen_min, (920, 865))
            screen.blit(i.gen_max, (1410, 865))
            screen.blit(i.label_wind_actual3, (1355, 790))
            screen.blit(i.slider_wind_actual, r.r_slider_wind_actual3)

            line_surf = font_labels.render(str(abs(line_flows[0])) + "MW", False, (0, 0, 0,))
            screen.blit(line_surf, (680, 320))
            line_surf = font_labels.render(str(line_flows[1]) + "MW", False, (0, 0, 0))
            screen.blit(line_surf, (1100, 450))
            line_surf = font_labels.render(str(line_flows[2]) + " / 87.6MW", False, (255, 0, 0))
            screen.blit(line_surf, (150, 450))

            load_surf = font_text.render(str(round(line_flows[0], 1)), False, (0, 0, 0,))
            screen.blit(load_surf, (1820, 370))
            gen1_surf = font_text.render(str(round(line_flows[2], 1)), False, (0, 0, 0))
            screen.blit(gen1_surf, (1820, 415))
            gen2_surf = font_text.render(str(round(line_flows[1], 1)), False, (0, 0, 0))
            screen.blit(gen2_surf, (1820, 460))

            load_surf = font_labels.render(str(load_val) + "MW", False, (0, 0, 0,))
            screen.blit(load_surf, (720, 750))
            gen1_surf = font_labels.render(str(gen_set[0]) + "MW", False, (0, 0, 0))
            screen.blit(gen1_surf, (412, 150))
            gen2_surf = font_labels.render(str(gen_set[1]) + "MW", False, (0, 0, 0))
            screen.blit(gen2_surf, (1012, 150))

            load_surf = font_text.render(str('j0.006'), False, (0, 0, 0,))
            screen.blit(load_surf, (1650, 370))
            gen1_surf = font_text.render(str('j0.012'), False, (0, 0, 0))
            screen.blit(gen1_surf, (1650, 415))
            gen2_surf = font_text.render(str('j0.018'), False, (0, 0, 0))
            screen.blit(gen2_surf, (1650, 460))

            if line_flows[0] > 0:
                screen.blit(i.line_12_pos, r.r_line_12)
            elif line_flows[0] < 0:
                screen.blit(i.line_12_neg, r.r_line_12)
            else:
                pass
            if line_flows[1] > 0:
                screen.blit(i.line_23_pos, r.r_line_23)
            elif line_flows[1] < 0:
                screen.blit(i.line_23_neg, r.r_line_23)
            else:
                pass
            if line_flows[2] > 0:
                screen.blit(i.line_13_pos, r.r_line_13)
            elif line_flows[2] < 0:
                screen.blit(i.line_13_neg, r.r_line_13)
            else:
                pass

            wind_forecast_surf = font_info.render(str(70) + "MW", False, (0, 0, 0))
            screen.blit(wind_forecast_surf, r.r_wind_forecast)
            wind_output_surf = font_info.render(str(90) + "MW", False, (0, 0, 0))
            screen.blit(wind_output_surf, r.r_wind_output)

        elif game_state == 413:
            text_surf = font_text.render(t.text_413_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_413_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            screen.blit(i.demand_fig, r.r_demand_fig)

        elif game_state == 414:
            text_surf = font_text.render(t.text_414_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_414_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        elif game_state == 415:
            text_surf = font_text.render(t.text_415_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_415_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        elif game_state == 416:
            text_surf = font_text.render(t.text_416_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_416_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        elif game_state == 417:
            text_surf = font_text.render(t.text_417_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_417_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        elif game_state == 418:
            text_surf = font_text.render(t.text_418_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_418_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        elif game_state == 419:
            screen.blit(i.mask_blackout, (0, 0))
            screen.blit(i.blank_textbox, r.r_blank_textbox)
            screen.blit(i.next_module, r.r_next_module)
            screen.blit(i.back_to_title, r.r_back_to_title)

            gen_set = [0, 0]
            r.r_slider_tut_tab1 = i.slider_tut_tab1.get_rect(center=(950, 762))
            r.r_slider_tut_tab2 = i.slider_tut_tab2.get_rect(center=(950, 837))

    elif game_state in range(500, 600):  # tutorial 5
        screen.fill((255, 255, 255))
        screen.blit(i.bg_10, (0, 0))
        screen.blit(i.button_next.convert_alpha(), r.r_button_next)
        screen.blit(i.table_4, r.r_table_4)

        if game_state == 500:
            text_surf = font_text.render(t.text_500_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_500_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

        if game_state == 501:
            text_surf = font_text.render(t.text_501_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_501_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_501_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(i.graph_net_zero, r.r_visual_center)

        if game_state == 502:
            text_surf = font_text.render(t.text_502_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_502_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_502_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(i.plant_coal_tut, r.r_visual_left)
            screen.blit(i.photo_coal_tut, r.r_visual_right)
            screen.blit(i.table_4_values, r.r_table_4, area=(0, 0, 400, 115))

        if game_state == 503:
            text_surf = font_text.render(t.text_503_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_503_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            screen.blit(i.plant_coal_tut, r.r_visual_left)
            screen.blit(i.photo_coal_tut, r.r_visual_right)
            screen.blit(i.table_4_values, r.r_table_4, area=(0, 0, 400, 115))

        if game_state == 504:
            text_surf = font_text.render(t.text_504_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_504_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_504_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(i.plant_gas_tut, r.r_visual_left)
            screen.blit(i.photo_gas_tut, r.r_visual_right)
            screen.blit(i.table_4_values, r.r_table_4, area=(0, 0, 400, 190))

        if game_state == 505:
            text_surf = font_text.render(t.text_505_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_505_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_505_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(i.plant_gas_tut, r.r_visual_left)
            screen.blit(i.photo_gas_tut, r.r_visual_right)
            screen.blit(i.table_4_values, r.r_table_4, area=(0, 0, 400, 190))

        if game_state == 506:
            text_surf = font_text.render(t.text_506_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_506_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_506_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(i.diagram_CCS, r.r_visual_center)
            screen.blit(i.table_4_values, r.r_table_4, area=(0, 0, 400, 370))

        if game_state == 507:
            text_surf = font_text.render(t.text_507_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_507_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_507_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(i.plant_hydro_tut, r.r_visual_left)
            screen.blit(i.photo_hydro_tut, r.r_visual_right)
            screen.blit(i.table_4_values, r.r_table_4, area=(0, 0, 400, 420))

        if game_state == 508:
            text_surf = font_text.render(t.text_508_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_508_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_508_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(i.plant_nuclear_tut, r.r_visual_left)
            screen.blit(i.photo_nuclear_tut, r.r_visual_right)
            screen.blit(i.table_4_values, r.r_table_4, area=(0, 0, 400, 460))

        if game_state == 509:
            text_surf = font_text.render(t.text_509_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_509_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_509_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(i.plant_wind_tut, r.r_visual_left)
            screen.blit(i.photo_wind_tut, r.r_visual_right)
            screen.blit(i.table_4_values, r.r_table_4, area=(0, 0, 400, 500))

        if game_state == 510:
            text_surf = font_text.render(t.text_510_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_510_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            screen.blit(i.plant_wind_tut, r.r_visual_left)
            screen.blit(i.photo_wind_tut, r.r_visual_right)
            screen.blit(i.table_4_values, r.r_table_4, area=(0, 0, 400, 500))

        if game_state == 511:
            text_surf = font_text.render(t.text_511_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_511_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            screen.blit(i.plant_solar_tut, r.r_plant_center)
            screen.blit(i.table_4_values, r.r_table_4)

        if game_state == 512:
            text_surf = font_text.render(t.text_512_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_512_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            screen.blit(i.plant_solar_tower_tut, r.r_visual_left)
            screen.blit(i.photo_solar_tower_tut, r.r_visual_right)
            screen.blit(i.table_4_values, r.r_table_4)

        if game_state == 513:
            text_surf = font_text.render(t.text_513_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_513_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_513_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(i.plant_solar_tut, r.r_visual_left)
            screen.blit(i.photo_solar_tut, r.r_visual_right)
            screen.blit(i.table_4_values, r.r_table_4)

        if game_state == 514:
            text_surf = font_text.render(t.text_514_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_514_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            text_surf = font_text.render(t.text_514_c, False, (0, 0, 0))
            screen.blit(text_surf, textbox_bot)

            screen.blit(i.graph_ontario_gen, r.r_visual_center)
            screen.blit(i.table_4_values, r.r_table_4)

        if game_state == 515:
            text_surf = font_text.render(t.text_515_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_515_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)

            screen.blit(i.graph_canada_gen, r.r_visual_center)
            screen.blit(i.table_4_values, r.r_table_4)

        if game_state == 516:
            text_surf = font_text.render(t.text_516_a, False, (0, 0, 0))
            screen.blit(text_surf, textbox_top)
            text_surf = font_text.render(t.text_516_b, False, (0, 0, 0))
            screen.blit(text_surf, textbox_mid)
            screen.blit(i.table_4_values, r.r_table_4)

        if game_state == 517:
            screen.blit(i.mask_blackout, (0, 0))
            screen.blit(i.blank_textbox, r.r_blank_textbox)
            screen.blit(i.next_module, r.r_next_module)
            screen.blit(i.back_to_title, r.r_back_to_title)
            screen.blit(i.table_4_values, r.r_table_4)


    elif game_state in range(600, 700):  # game - monthly
        if game_state == 600:
            # Render new map every time
            screen.fill((255, 255, 255))
            screen.blit(i.bg_20, (0, 0))

            for plant in map:
                plant_image = choose_image(map[plant]['type'])
                plant_rect = choose_rect(plant)
                screen.blit(plant_image, plant_rect)

            for load in loads:
                screen.blit(loads[load]['image'], loads[load]['rect'])

        if game_state == 601:
            # Create sidebar
            sidebar = pygame.Surface((375, screen_height))
            sidebar.set_alpha(128)
            sidebar.fill((255, 255, 255))
            screen.blit(sidebar, (0, 0))

            text_hydro_title = font_text.render(t.text_hydro_title, False, (0, 0, 0))
            screen.blit(text_hydro_title, (50, 110))
            text_hydro_cost = font_text.render(t.text_hydro_cost, False, (0, 0, 0))
            screen.blit(text_hydro_cost, (175, 150))
            text_hydro_emissions = font_text.render(t.text_hydro_emissions, False, (0, 0, 0))
            screen.blit(text_hydro_emissions, (175, 190))
            screen.blit(i.plant_hydro_button, r.button_hydro)

            text_wind_title = font_text.render(t.text_wind_title, False, (0, 0, 0))
            screen.blit(text_wind_title, (50, 260))
            text_wind_cost = font_text.render(t.text_wind_cost, False, (0, 0, 0))
            screen.blit(text_wind_cost, (175, 300))
            text_wind_emissions = font_text.render(t.text_wind_emissions, False, (0, 0, 0))
            screen.blit(text_wind_emissions, (175, 340))
            screen.blit(i.plant_wind_button, r.button_wind)

            text_solar_title = font_text.render(t.text_solar_title, False, (0, 0, 0))
            screen.blit(text_solar_title, (50, 410))
            text_solar_cost = font_text.render(t.text_solar_cost, False, (0, 0, 0))
            screen.blit(text_solar_cost, (175, 450))
            text_solar_emissions = font_text.render(t.text_solar_emissions, False, (0, 0, 0))
            screen.blit(text_solar_emissions, (175, 490))
            screen.blit(i.plant_solar_button, r.button_solar)

            text_nuclear_title = font_text.render(t.text_nuclear_title, False, (0, 0, 0))
            screen.blit(text_nuclear_title, (50, 560))
            text_nuclear_cost = font_text.render(t.text_nuclear_cost, False, (0, 0, 0))
            screen.blit(text_nuclear_cost, (175, 600))
            text_nuclear_emissions = font_text.render(t.text_nuclear_emissions, False, (0, 0, 0))
            screen.blit(text_nuclear_emissions, (175, 640))
            screen.blit(i.plant_nuclear_button, r.button_nuclear)

            text_coal_title = font_text.render(t.text_coal_title, False, (0, 0, 0))
            screen.blit(text_coal_title, (50, 710))
            text_coal_cost = font_text.render(t.text_coal_cost, False, (0, 0, 0))
            screen.blit(text_coal_cost, (175, 750))
            text_coal_emissions = font_text.render(t.text_coal_emissions, False, (0, 0, 0))
            screen.blit(text_coal_emissions, (175, 790))
            screen.blit(i.plant_coal_button, r.button_coal)

            text_gas_title = font_text.render(t.text_gas_title, False, (0, 0, 0))
            screen.blit(text_gas_title, (50, 860))
            text_gas_cost = font_text.render(t.text_gas_cost, False, (0, 0, 0))
            screen.blit(text_gas_cost, (175, 900))
            text_gas_emissions = font_text.render(t.text_gas_emissions, False, (0, 0, 0))
            screen.blit(text_gas_emissions, (175, 940))
            screen.blit(i.plant_gas_button, r.button_gas)

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


