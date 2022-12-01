import pygame
import rects as r



def select_step(Event, Game_state, map, current_area, is_pf_success):
    gs_out = Game_state
    clicked_rect = 0
    if Game_state in range(0, 100): # title screen
        if Event.type == pygame.MOUSEBUTTONUP and r.r_button_start.collidepoint(Event.pos):
            gs_out = 100
        if Event.type == pygame.MOUSEBUTTONUP and r.r_title.collidepoint(Event.pos):
            gs_out = -1

    elif Game_state in range(100, 200):
        if Game_state == 100:  # welcome text
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 101

        if Game_state == 101:  # UI description
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 102

        if Game_state == 102:  # Load description
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 103

        if Game_state == 103:  # Generator description
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 104

        if Game_state == 104:  # System description
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 105

        if Game_state == 105:  # Power balance
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 106

        if Game_state == 106:  # Frequency and overload
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 107

        if Game_state == 107:  # Under-load
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 108

        if Game_state == 108:  # Display values
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 109

        if Game_state == 109:  # Move sliders
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                if is_pf_success == False:
                    gs_out = 110
                elif is_pf_success == True:
                    gs_out = 111

        if Game_state == 110:  # PF failure
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 109

        if Game_state == 111:  # PF success
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 112

        if Game_state == 112:  # Recap
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 113

        if Game_state == 113:  # Onto the next module
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 114

        if Game_state == 114:  # welcome text
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 100

    elif Game_state in range(200, 300): 
        if Game_state == 200:
            if Event.type == pygame.MOUSEBUTTONDOWN and r.area_1.collidepoint(Event.pos):
                gs_out = 201
                current_area = 'area_1'
            elif Event.type == pygame.MOUSEBUTTONDOWN and r.area_2.collidepoint(Event.pos):
                gs_out = 201
                current_area = 'area_2'

        # Change the area to whatever button is pressed
        elif Game_state == 201:
                if Event.type == pygame.MOUSEBUTTONDOWN and r.button_hydro.collidepoint(Event.pos):
                    gs_out = 200
                    map[current_area]['type'] = 'hydro'
                elif Event.type == pygame.MOUSEBUTTONDOWN and r.button_wind.collidepoint(Event.pos):
                    gs_out = 200
                    map[current_area]['type'] = 'wind'
                elif Event.type == pygame.MOUSEBUTTONDOWN and r.button_solar.collidepoint(Event.pos):
                    gs_out = 200
                    map[current_area]['type'] = 'solar'
                elif Event.type == pygame.MOUSEBUTTONDOWN and r.button_nuclear.collidepoint(Event.pos):
                    gs_out = 200
                    map[current_area]['type'] = 'nuclear'
                elif Event.type == pygame.MOUSEBUTTONDOWN and r.button_coal.collidepoint(Event.pos):
                    gs_out = 200
                    map[current_area]['type'] = 'coal'
                elif Event.type == pygame.MOUSEBUTTONDOWN and r.button_gas.collidepoint(Event.pos):
                    gs_out = 200
                    map[current_area]['type'] = 'gas'

    elif Game_state == 3:
        pass
    elif Game_state == 4:
        pass

    return [gs_out, map, current_area]
