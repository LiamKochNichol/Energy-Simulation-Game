import pygame

bg_00 = pygame.image.load("sprites/bg_0.jpg")
title = pygame.image.load("sprites/name_title.png")

bg_10 = pygame.image.load("sprites/bg_1.png")
mask_tut1_3 = pygame.image.load("sprites/mask_tut1_3.png")
mask_tut1_3.set_alpha(155)
fg_10 = pygame.image.load("sprites/fg_1.png")

button_start = pygame.image.load("sprites/button_start.png")
button_next = pygame.image.load("sprites/button_next.png")
slider_tut1 = pygame.image.load("sprites/slider_tut_1.png")
slider_tut2 = pygame.image.load("sprites/slider_tut_1.png")
slider_tut_tab1 = pygame.image.load("sprites/slider_tut_tab_1.png")
slider_tut_tab2 = pygame.image.load("sprites/slider_tut_tab_1.png")
notice_101_a = pygame.image.load("sprites/notice_101_a.png")
notice_101_b = pygame.image.load("sprites/notice_101_b.png")
load_tut1 = pygame.image.load("sprites/load_tut1.png")
load_tut1.set_colorkey((255, 255, 255))

button_run = pygame.image.load("sprites/button_run.png")

text_sample = pygame.image.load("sprites/text_sample.png")
text_sample2 = pygame.image.load("sprites/text_sample2.png")
text_sample3 = pygame.image.load("sprites/text_sample3.png")
text_sample4 = pygame.image.load("sprites/text_sample4.png")
text_sample5 = pygame.image.load("sprites/text_sample5.png")

window_icon = pygame.image.load("sprites/window_icon.png")

# Testing features
bg_20 = pygame.image.load("sprites/ontario_map.png")
temp_nuclear = pygame.image.load("sprites/plant_nuclear.png")
nuclear_image = pygame.transform.scale(temp_nuclear, (100,100))

# Blank area
blank_area = pygame.Surface((100,100))
blank_area.set_alpha(128)
blank_area.fill((255,255,255))

# Other power plants
plant_wind = pygame.transform.scale(pygame.image.load("sprites/plant_wind.png"), (100,100))
plant_solar = pygame.transform.scale(pygame.image.load("sprites/plant_solar.png"), (100,100))
plant_nuclear = pygame.transform.scale(pygame.image.load("sprites/plant_nuclear.png"), (100,100))
plant_hydro = pygame.transform.scale(pygame.image.load("sprites/plant_hydro.png"), (100,100))
plant_gas = pygame.transform.scale(pygame.image.load("sprites/plant_gas.png"), (100,100))
plant_coal = pygame.transform.scale(pygame.image.load("sprites/plant_coal.png"), (100,100))