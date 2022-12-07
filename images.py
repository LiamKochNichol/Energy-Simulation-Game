import pygame

bg_00 = pygame.image.load("sprites/bg_0.jpg")
title = pygame.image.load("sprites/name_title.png")

bg_10 = pygame.image.load("sprites/bg_1.png")
mask_blackout = pygame.image.load("sprites/mask_blackout.png")
mask_blackout.set_alpha(155)
mask_all = pygame.image.load("sprites/mask_all.png")
mask_all.set_alpha(100)
fg_10 = pygame.image.load("sprites/fg_1.png")

button_start = pygame.image.load("sprites/button_start.png")
button_choose_level = pygame.image.load("sprites/button_choose.png")
button_next = pygame.image.load("sprites/button_next.png")
button_run = pygame.image.load("sprites/button_run.png")
button_retry1 = pygame.image.load("sprites/button_retry_1.png")
button_retry2 = pygame.image.load("sprites/button_retry_2.png")

# Choose your level assets
choose_leveL_box = pygame.image.load("sprites/choose_level_box.png")
button_back = pygame.image.load("sprites/button_back.png")
choose_1 = pygame.image.load("sprites/choose_1.png")
choose_2 = pygame.image.load("sprites/choose_2.png")
choose_3 = pygame.image.load("sprites/choose_3.png")
choose_4 = pygame.image.load("sprites/choose_4.png")
choose_5 = pygame.image.load("sprites/choose_5.png")
choose_6 = pygame.image.load("sprites/choose_6.png")

# Tutorial 1 assets
slider_tut1 = pygame.image.load("sprites/slider_tut_1.png")
slider_tut2 = pygame.image.load("sprites/slider_tut_1.png")
slider_tut_tab1 = pygame.image.load("sprites/slider_tut_tab_1.png")
slider_tut_tab2 = pygame.image.load("sprites/slider_tut_tab_1.png")
notice_101_a = pygame.image.load("sprites/notice_101_a.png")
notice_101_b = pygame.image.load("sprites/notice_101_b.png")
load_tut1 = pygame.image.load("sprites/load_tut1.png")
load_tut1.set_colorkey((255, 255, 255))
gen1_tut1 = pygame.image.load("sprites/gen_c_tut1.png")
gen1_tut1.set_colorkey((255, 255, 255))
gen2_tut1 = pygame.image.load("sprites/gen_c_tut1.png")
gen2_tut1.set_colorkey((255, 255, 255))
system_tut1 = pygame.image.load("sprites/system_tut1.png")
system_tut1.set_colorkey((255, 255, 255))

blank_textbox = pygame.image.load("sprites/blank_textbox.png")
next_module = pygame.image.load("sprites/next_module.png")
back_to_title = pygame.image.load("sprites/back_to_title.png")

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