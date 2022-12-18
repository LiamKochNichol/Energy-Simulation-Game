import pygame

window_icon = pygame.image.load("sprites/window_icon.png")

bg_00 = pygame.image.load("sprites/bg_0.jpg")
title = pygame.image.load("sprites/title.png")

bg_10 = pygame.image.load("sprites/bg_1.png")
mask_blackout = pygame.image.load("sprites/mask_blackout.png")
mask_blackout.set_alpha(155)
mask_all = pygame.image.load("sprites/mask_all.png")
mask_all.set_alpha(100)
fg_10 = pygame.image.load("sprites/fg_1.png")

table_1 = pygame.image.load("sprites/table_1.png")
table_2 = pygame.image.load("sprites/table_2.png")

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
pygame.font.init()
font_gen_limits = pygame.font.SysFont('timesnewroman',20)
gen_min = font_gen_limits.render('0MW',  False, (0, 0, 0))
gen_max = font_gen_limits.render('100MW',  False, (0, 0, 0))
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

line_12_pos = pygame.image.load("sprites/line_12_pos.png")
line_12_pos.set_colorkey((255, 255, 255))
line_12_neg = pygame.image.load("sprites/line_12_neg.png")
line_12_neg.set_colorkey((255, 255, 255))
line_13_pos = pygame.image.load("sprites/line_13_pos.png")
line_13_pos.set_colorkey((255, 255, 255))
line_13_neg = pygame.image.load("sprites/line_13_neg.png")
line_13_neg.set_colorkey((255, 255, 255))
line_23_pos = pygame.image.load("sprites/line_23_pos.png")
line_23_pos.set_colorkey((255, 255, 255))
line_23_neg = pygame.image.load("sprites/line_23_neg.png")
line_23_neg.set_colorkey((255, 255, 255))

blank_textbox = pygame.image.load("sprites/blank_textbox.png")
next_module = pygame.image.load("sprites/next_module.png")
back_to_title = pygame.image.load("sprites/back_to_title.png")

# tutorial 3
diagram_line = pygame.image.load("sprites/diagram_line.png")
diagram_RL = pygame.image.load("sprites/diagram_RL.png")
button_choose_line = pygame.image.load("sprites/button_choose_line.png")

# tutorial 4
gen_wind = pygame.image.load("sprites/gen_wind_tut4.png")
gen_wind.set_colorkey((255, 255, 255))
wind_fig = pygame.image.load("sprites/wind_fig_tut4.png")
slider_wind_10 = pygame.image.load("sprites/slider_wind_10.png")
slider_wind_25 = pygame.image.load("sprites/slider_wind_25.png")
slider_wind_10.set_colorkey((255, 255, 255))
slider_wind_25.set_colorkey((255, 255, 255))
slider_wind_actual = pygame.image.load("sprites/slider_wind_actual.png")
slider_wind_actual.set_colorkey((255, 255, 255))
label_wind_10 = font_gen_limits.render('70±10MW',  False, (0, 0, 0))
label_wind_25 = font_gen_limits.render('70±25MW',  False, (0, 0, 0))
label_wind_actual1 = font_gen_limits.render('65MW',  False, (0, 0, 0))
label_wind_actual2 = font_gen_limits.render('45MW',  False, (0, 0, 0))
label_wind_actual3 = font_gen_limits.render('85MW',  False, (0, 0, 0))
demand_fig = pygame.image.load("sprites/demand_fig_tut4.png")
table_3 = pygame.image.load("sprites/table_3.png")

# tutorial 5
table_4 = pygame.image.load("sprites/table_4.png")
graph_net_zero = pygame.image.load("sprites/graph_net_zero.png")
graph_ontario_gen = pygame.image.load("sprites/graph_ontario_gen.png")
graph_canada_gen = pygame.image.load("sprites/graph_canada_gen.png")
diagram_CCS = pygame.image.load("sprites/photo_CCS.png")

plant_coal_tut = pygame.image.load("sprites/plant_coal.png")
plant_gas_tut = pygame.image.load("sprites/plant_gas.png")
plant_hydro_tut = pygame.image.load("sprites/plant_hydro.png")
plant_nuclear_tut = pygame.image.load("sprites/plant_nuclear.png")
plant_wind_tut = pygame.image.load("sprites/plant_wind.png")
plant_solar_tut = pygame.image.load("sprites/plant_solar.png")
plant_solar_tower_tut = pygame.image.load("sprites/plant_solar_tower.png")

photo_coal_tut = pygame.image.load("sprites/photo_coal.jpg")
photo_gas_tut = pygame.image.load("sprites/photo_gas.jpg")
photo_hydro_tut = pygame.image.load("sprites/photo_hydro.jpg")
photo_nuclear_tut = pygame.image.load("sprites/photo_nuclear.jpg")
photo_wind_tut = pygame.image.load("sprites/photo_wind.jpg")
photo_solar_tut = pygame.image.load("sprites/photo_solar_PV.jpg")
photo_solar_tower_tut = pygame.image.load("sprites/photo_solar_tower.jpg")

table_4_values = pygame.image.load("sprites/table_4_values.png")
table_4_values.set_colorkey((255, 255, 255))
# Testing features

temp_nuclear = pygame.image.load("sprites/plant_nuclear.png")
nuclear_image = pygame.transform.scale(temp_nuclear, (100,100))

# Blank area
blank_area = pygame.Surface((75,75))
blank_area.set_alpha(128)
blank_area.fill((0,0,0))

# Power plant buttons
plant_wind_button = pygame.transform.scale(pygame.image.load("sprites/plant_wind.png"), (100,100))
plant_solar_button = pygame.transform.scale(pygame.image.load("sprites/plant_solar.png"), (100,100))
plant_nuclear_button = pygame.transform.scale(pygame.image.load("sprites/plant_nuclear.png"), (100,100))
plant_hydro_button = pygame.transform.scale(pygame.image.load("sprites/plant_hydro.png"), (100,100))
plant_gas_button = pygame.transform.scale(pygame.image.load("sprites/plant_gas.png"), (100,100))
plant_coal_button = pygame.transform.scale(pygame.image.load("sprites/plant_coal.png"), (100,100))

# Other power plants
plant_wind = pygame.transform.scale(pygame.image.load("sprites/plant_wind.png"), (75,75))
plant_solar = pygame.transform.scale(pygame.image.load("sprites/plant_solar.png"), (75,75))
plant_nuclear = pygame.transform.scale(pygame.image.load("sprites/plant_nuclear.png"), (75,75))
plant_hydro = pygame.transform.scale(pygame.image.load("sprites/plant_hydro.png"), (75,75))
plant_gas = pygame.transform.scale(pygame.image.load("sprites/plant_gas.png"), (75,75))
plant_coal = pygame.transform.scale(pygame.image.load("sprites/plant_coal.png"), (75,75))

# Transmission Map
bg_20 = pygame.transform.scale(pygame.image.load("sprites/transmission_map_ON.png"), (1920,1080))

# Loads
toronto = pygame.transform.scale(pygame.image.load("sprites/Load_Toronto.png"), (100,100))
ottawa = pygame.transform.scale(pygame.image.load("sprites/Load_Ottawa.png"), (100,100))
windsor = pygame.transform.scale(pygame.image.load("sprites/Load_Windsor.png"), (100,100))
sudbury = pygame.transform.scale(pygame.image.load("sprites/Load_Sudbury.png"), (100,100))