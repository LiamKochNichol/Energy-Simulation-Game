import pygame
import images as i

r_button_start = i.button_start.get_rect(center=(960, 750))
r_button_choose_level = i.button_choose_level.get_rect(center=(960, 860))
r_button_next = i.button_next.get_rect(center=(1720, 990))
r_button_run = i.button_run.get_rect(center=(1720, 990))
r_button_retry = i.button_retry1.get_rect(center = (1720, 990))

r_p_imbalance = pygame.Rect(0, 0, 100, 40)
r_p_imbalance.center = (1700, 160)

r_cost = pygame.Rect(0, 0, 100, 40)
r_cost.center = (1710, 250)

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
r_slider_list = [r_slider_tut_tab1, r_slider_tut_tab2]
r_title = i.title.get_rect(center=(960, 250))
r_notice_101_a = i.notice_101_a.get_rect(center=(750, 450))
r_notice_101_b = i.notice_101_b.get_rect(center=(1720, 450))
r_load_tut1 = i.load_tut1.get_rect(midtop=(750, 649))
r_gen1_tut1 = i.gen1_tut1.get_rect(topleft=(412, 199))
r_gen2_tut1 = i.gen2_tut1.get_rect(topleft=(1012, 199))
r_system_tut1 = i.system_tut1.get_rect(midbottom=(750, 750))


r_blank_textbox = i.blank_textbox.get_rect(center=(960, 540))
r_next_module = i.next_module.get_rect(midtop=(960, 400))
r_back_to_title = i.back_to_title.get_rect(midtop=(960, 560))

# Nuclear power plant rect
nuclear_rect = i.nuclear_image.get_rect()
nuclear_rect.center = (100,100)

# Sidebar buttons
button_hydro = i.plant_hydro.get_rect()
button_hydro.center = (100,100)
button_wind = i.plant_wind.get_rect()
button_wind.center = (100,210)
button_solar = i.plant_solar.get_rect()
button_solar.center = (100,320)
button_nuclear = i.plant_nuclear.get_rect()
button_nuclear.center = (100,430)
button_coal = i.plant_coal.get_rect()
button_coal.center = (100,540)
button_gas = i.plant_gas.get_rect()
button_gas.center = (100,650)


# Initialize blank
area_1 = i.blank_area.get_rect()
area_1.center = (450,450)

area_2 = i.blank_area.get_rect()
area_2.center = (600,600)
