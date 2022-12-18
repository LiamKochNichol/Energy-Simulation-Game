import pygame
import images as i

r_title = i.title.get_rect(center=(960, 300))
r_button_start = i.button_start.get_rect(center=(960, 750))
r_button_choose_level = i.button_choose_level.get_rect(center=(960, 860))
r_button_next = i.button_next.get_rect(center=(1720, 990))
r_button_run = i.button_run.get_rect(center=(1720, 990))
r_button_retry = i.button_retry1.get_rect(center = (1720, 990))

r_p_imbalance = pygame.Rect(0, 0, 100, 40)
r_p_imbalance.center = (1700, 160)

r_cost = pygame.Rect(0, 0, 100, 40)
r_cost.center = (1710, 250)

r_wind_forecast = pygame.Rect(0, 0, 100, 40)
r_wind_forecast.center = (1720, 595)

r_wind_output = pygame.Rect(0, 0, 100, 40)
r_wind_output.center = (1720, 685)

r_table_1 = i.slider_tut1.get_rect(midtop=(1795, 85))
r_table_2 = i.slider_tut1.get_rect(midtop=(1795, 293))
r_table_3 = i.slider_tut1.get_rect(midtop=(1795, 520))
r_table_4 = i.table_4.get_rect(midtop=(1710, 100))

r_choose_level_box = i.choose_leveL_box.get_rect(center=(960, 540))
r_button_back = i.button_back.get_rect(center=(960, 770))
r_choose_1 = i.choose_1.get_rect(center=(560, 370))
r_choose_2 = i.choose_2.get_rect(center=(960, 370))
r_choose_3 = i.choose_3.get_rect(center=(1360, 370))
r_choose_4 = i.choose_4.get_rect(center=(560, 600))
r_choose_5 = i.choose_5.get_rect(center=(960, 600))
r_choose_6 = i.choose_6.get_rect(center=(1360, 600))

# Tutorial 1
r_slider_tut1 = i.slider_tut1.get_rect(topleft=(950, 750))
r_slider_tut2 = i.slider_tut2.get_rect(topleft=(950, 825))
r_slider_tut_tab1 = i.slider_tut_tab1.get_rect(center=(950, 762))
r_slider_tut_tab2 = i.slider_tut_tab2.get_rect(center=(950, 837))
r_notice_101_a = i.notice_101_a.get_rect(center=(750, 450))
r_notice_101_b = i.notice_101_b.get_rect(center=(1720, 450))
r_load_tut1 = i.load_tut1.get_rect(midtop=(750, 649))
r_gen1_tut1 = i.gen1_tut1.get_rect(topleft=(412, 199))
r_gen2_tut1 = i.gen2_tut1.get_rect(topleft=(1012, 199))
r_system_tut1 = i.system_tut1.get_rect(midbottom=(750, 750))

r_line_12 = i.line_12_pos.get_rect(midtop=(740, 369))
r_line_13 = i.line_13_pos.get_rect(topleft=(418, 389))
r_line_23 = i.line_23_pos.get_rect(topleft=(849, 389))

r_blank_textbox = i.blank_textbox.get_rect(center=(960, 540))
r_next_module = i.next_module.get_rect(midtop=(960, 400))
r_back_to_title = i.back_to_title.get_rect(midtop=(960, 560))

#tutorial 3
r_line_1_2 = i.choose_1.get_rect(center=(750, 250))
r_line_1_3 = i.choose_2.get_rect(center=(265, 530))
r_line_2_3 = i.choose_3.get_rect(center=(1250, 530))

r_diagram_line = i.diagram_line.get_rect(bottomleft=(0, 900))
r_diagram_RL = i.diagram_RL.get_rect(bottomleft=(0, 900))


#tutorial 4
r_slider_wind_10 =i.slider_wind_10.get_rect(center=(1300, 762))
r_slider_wind_25 =i.slider_wind_25.get_rect(center=(1300, 762))
r_slider_wind_actual1 = i.slider_wind_actual.get_rect(center=(1275, 762))
r_slider_wind_actual2 = i.slider_wind_actual.get_rect(center=(1175, 762))
r_slider_wind_actual3 = i.slider_wind_actual.get_rect(center=(1375, 762))
r_wind_fig = i.wind_fig.get_rect(bottomleft=(0, 900))
r_demand_fig = i.demand_fig.get_rect(bottomleft=(0, 900))

#tutorial 5
r_visual_center = i.graph_net_zero.get_rect(center=(750, 450))
r_visual_left = i.plant_solar_tut.get_rect(center=(454, 450))
r_visual_right = i.plant_solar_tut.get_rect(center=(1056, 450))
r_plant_center = i.plant_solar_tut.get_rect(center=(750, 450))

# Nuclear power plant rect
nuclear_rect = i.nuclear_image.get_rect()
nuclear_rect.center = (100,100)

# Sidebar buttons
button_hydro = i.plant_hydro_button.get_rect()
button_hydro.center = (100,190)
button_wind = i.plant_wind_button.get_rect()
button_wind.center = (100,340)
button_solar = i.plant_solar_button.get_rect()
button_solar.center = (100,490)
button_nuclear = i.plant_nuclear_button.get_rect()
button_nuclear.center = (100,640)
button_coal = i.plant_coal_button.get_rect()
button_coal.center = (100,790)
button_gas = i.plant_gas_button.get_rect()
button_gas.center = (100,940)

# Initialize Generators and Loads
# Toronto
toronto = i.toronto.get_rect()
toronto.center = (1075,650)
# Ottawa
ottawa = i.ottawa.get_rect()
ottawa.center = (1675,325)
# Windsor
windsor = i.windsor.get_rect()
windsor.center = (500,1000)
# Sudbury
sudbury = i.sudbury.get_rect()
sudbury.center = (825,100)
# Sir Adam Beck (hydro)
area_1 = i.blank_area.get_rect()
area_1.center = (1150,825)
# Bruce Nuclear
area_2 = i.blank_area.get_rect()
area_2.center = (725,560)
# Darlington (nuclear)
area_3 = i.blank_area.get_rect()
area_3.center = (1175,650)
# Des Joachims (hydro)
area_4 = i.blank_area.get_rect()
area_4.center = (1350,150)
# Wells (hydro)
area_5 = i.blank_area.get_rect()
area_5.center = (450,100)
# Greenfield (gas)
area_6 = i.blank_area.get_rect()
area_6.center = (600,850)
# Goreway (gas)
area_7 = i.blank_area.get_rect()
area_7.center = (1000,600)
# Lennox (gas)
area_8 = i.blank_area.get_rect()
area_8.center = (1600,550)
# Nanticoke (coal)
area_9 = i.blank_area.get_rect()
area_9.center = (1000,900)
# Lakeview (coal)
area_10 = i.blank_area.get_rect()
area_10.center = (1000,750)
# Prince (wind but blank to start)
area_11 = i.blank_area.get_rect()
area_11.center = (325,75)
# South Kent (wind but blank to start)
area_12 = i.blank_area.get_rect()
area_12.center = (775,900)
# K2 Wind (wind but blank to start)
area_13 = i.blank_area.get_rect()
area_13.center = (725,700)
# Nanticoke Solar (solar but blank to start)
area_14 = i.blank_area.get_rect()
area_14.center = (900,800)
# Potential site near Georgian bay
area_15 = i.blank_area.get_rect()
area_15.center = (1000,400)
