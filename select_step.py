import pygame
import rects as r



def select_step(Event, Game_state, map, current_area, is_pf_success):
    gs_out = Game_state
    clicked_rect = 0
    if Game_state in range(0, 100): # title screen
        if Game_state == 0:
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_start.collidepoint(Event.pos):
                gs_out = 100
            if Event.type == pygame.MOUSEBUTTONUP and r.r_title.collidepoint(Event.pos):
                gs_out = -1
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_choose_level.collidepoint(Event.pos):
                gs_out = 1

        elif Game_state == 1:
            if Event.type == pygame.MOUSEBUTTONUP:
                if r.r_choose_1.collidepoint(Event.pos):
                    gs_out = 100
                elif r.r_choose_2.collidepoint(Event.pos):
                    gs_out = 200
                elif r.r_choose_3.collidepoint(Event.pos):
                    gs_out = 300
                elif r.r_choose_4.collidepoint(Event.pos):
                    gs_out = 400
                elif r.r_choose_5.collidepoint(Event.pos):
                    gs_out = 500
                elif r.r_choose_6.collidepoint(Event.pos):
                    gs_out = 600
                elif r.r_button_back.collidepoint(Event.pos):
                    gs_out = 0

    elif Game_state in range(100, 200):
        if Game_state == 100:  # welcome text
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 101

        elif Game_state == 101:  # UI description
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 102

        elif Game_state == 102:  # Load description
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 103

        elif Game_state == 103:  # Generator description
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 104

        elif Game_state == 104:  # System description
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 105

        elif Game_state == 105:  # Power balance
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 106

        elif Game_state == 106:  # Frequency and overload
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 107

        elif Game_state == 107:  # Under-load
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 108

        elif Game_state == 108:  # Display values
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 109

        elif Game_state == 109:  # Move sliders
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                if is_pf_success == 0:
                    gs_out = 110
                elif is_pf_success == 1:
                    gs_out = 111

        elif Game_state == 110:  # PF failure
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 109

        elif Game_state == 111:  # PF success
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 112

        elif Game_state == 112:  # Recap
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 113

        elif Game_state == 113:  # Next Module or Back to Title
            if Event.type == pygame.MOUSEBUTTONUP:
                if r.r_next_module.collidepoint(Event.pos):
                    gs_out = 200
                elif r.r_back_to_title.collidepoint(Event.pos):
                    gs_out = 0

    elif Game_state in range(200, 300): 
        if Game_state == 200:
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 201
        elif Game_state == 201:
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 202
        elif Game_state == 202:
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 203
        elif Game_state == 203:
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 204
        elif Game_state == 204:
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 205
        elif Game_state == 205:
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                if is_pf_success == 0:
                    gs_out = 206
                elif is_pf_success == 2:
                    gs_out = 207
                elif is_pf_success == 1:
                    gs_out = 208

        elif Game_state == 206:
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 205
        elif Game_state == 207:
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 205
        elif Game_state == 208:
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 209
        elif Game_state == 209:
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 210
        elif Game_state == 210:
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 211
        elif Game_state == 211:
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 0

    elif Game_state in range(600, 700):
        if Game_state == 600:
            if Event.type == pygame.MOUSEBUTTONDOWN and r.area_1.collidepoint(Event.pos):
                gs_out = 601
                current_area = 'area_1'
            elif Event.type == pygame.MOUSEBUTTONDOWN and r.area_2.collidepoint(Event.pos):
                gs_out = 601
                current_area = 'area_2'
            elif Event.type == pygame.MOUSEBUTTONDOWN and r.area_3.collidepoint(Event.pos):
                gs_out = 601
                current_area = 'area_3'
            elif Event.type == pygame.MOUSEBUTTONDOWN and r.area_4.collidepoint(Event.pos):
                gs_out = 601
                current_area = 'area_4'
            elif Event.type == pygame.MOUSEBUTTONDOWN and r.area_5.collidepoint(Event.pos):
                gs_out = 601
                current_area = 'area_5'
            elif Event.type == pygame.MOUSEBUTTONDOWN and r.area_6.collidepoint(Event.pos):
                gs_out = 601
                current_area = 'area_6'
            elif Event.type == pygame.MOUSEBUTTONDOWN and r.area_7.collidepoint(Event.pos):
                gs_out = 601
                current_area = 'area_7'
            elif Event.type == pygame.MOUSEBUTTONDOWN and r.area_8.collidepoint(Event.pos):
                gs_out = 601
                current_area = 'area_8'
            elif Event.type == pygame.MOUSEBUTTONDOWN and r.area_9.collidepoint(Event.pos):
                gs_out = 601
                current_area = 'area_9'
            elif Event.type == pygame.MOUSEBUTTONDOWN and r.area_10.collidepoint(Event.pos):
                gs_out = 601
                current_area = 'area_10'
            elif Event.type == pygame.MOUSEBUTTONDOWN and r.area_11.collidepoint(Event.pos):
                gs_out = 601
                current_area = 'area_11'
            elif Event.type == pygame.MOUSEBUTTONDOWN and r.area_12.collidepoint(Event.pos):
                gs_out = 601
                current_area = 'area_12'
            elif Event.type == pygame.MOUSEBUTTONDOWN and r.area_13.collidepoint(Event.pos):
                gs_out = 601
                current_area = 'area_13'
            elif Event.type == pygame.MOUSEBUTTONDOWN and r.area_14.collidepoint(Event.pos):
                gs_out = 601
                current_area = 'area_14'
            elif Event.type == pygame.MOUSEBUTTONDOWN and r.area_15.collidepoint(Event.pos):
                gs_out = 601
                current_area = 'area_15'
            

        # Change the area to whatever button is pressed
        elif Game_state == 601:
                if Event.type == pygame.MOUSEBUTTONDOWN and r.button_hydro.collidepoint(Event.pos):
                    gs_out = 600
                    map[current_area]['type'] = 'hydro'
                elif Event.type == pygame.MOUSEBUTTONDOWN and r.button_wind.collidepoint(Event.pos):
                    gs_out = 600
                    map[current_area]['type'] = 'wind'
                elif Event.type == pygame.MOUSEBUTTONDOWN and r.button_solar.collidepoint(Event.pos):
                    gs_out = 600
                    map[current_area]['type'] = 'solar'
                elif Event.type == pygame.MOUSEBUTTONDOWN and r.button_nuclear.collidepoint(Event.pos):
                    gs_out = 600
                    map[current_area]['type'] = 'nuclear'
                elif Event.type == pygame.MOUSEBUTTONDOWN and r.button_coal.collidepoint(Event.pos):
                    gs_out = 600
                    map[current_area]['type'] = 'coal'
                elif Event.type == pygame.MOUSEBUTTONDOWN and r.button_gas.collidepoint(Event.pos):
                    gs_out = 600
                    map[current_area]['type'] = 'gas'

    elif Game_state == 4:
        pass

    return [gs_out, map, current_area]
