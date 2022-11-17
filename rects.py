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