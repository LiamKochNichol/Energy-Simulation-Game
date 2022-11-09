import pygame
import rects as r


def select_step(Event, Game_state):
    gs_out = Game_state
    if Game_state in range(0, 100):
        if Event.type == pygame.MOUSEBUTTONUP and r.r_button_start.collidepoint(Event.pos):
            gs_out = 100

    elif Game_state in range(100, 200):
        if Game_state == 100:  # welcome text
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 101

        if Game_state == 101:  # welcome text
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 102

        if Game_state == 102:  # welcome text
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 103

        if Game_state == 103:  # welcome text
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 104

        if Game_state == 104:  # welcome text
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 105

        if Game_state == 105:  # welcome text
            if Event.type == pygame.MOUSEBUTTONUP and r.r_button_next.collidepoint(Event.pos):
                gs_out = 101

    elif Game_state == 2:
        pass
    elif Game_state == 3:
        pass
    elif Game_state == 4:
        pass

    return gs_out
