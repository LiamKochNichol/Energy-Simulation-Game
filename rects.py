import pygame
import images as i

r_button_start = i.button_start.get_rect(center=(683, 600))
r_button_next = i.button_next.get_rect(center=(1050, 700))
r_button_run = i.button_run.get_rect(center=(1050, 600))
r_slider_tut = i.slider_tut.get_rect(center=(860, 560))
r_slider_tut_tab1 = i.slider_tut_tab1.get_rect(center=(666, 510))
r_slider_tut_tab2 = i.slider_tut_tab2.get_rect(center=(666, 580))
r_slider_list = [r_slider_tut_tab1, r_slider_tut_tab2]

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
