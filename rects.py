import pygame
import images as i

r_button_start = i.button_start.get_rect(center=(960, 800))
r_button_next = i.button_next.get_rect(center=(1720, 990))
r_button_run = i.button_run.get_rect(center=(1050, 600))
r_slider_tut1 = i.slider_tut1.get_rect(topleft=(950, 750))
r_slider_tut2 = i.slider_tut2.get_rect(topleft=(950, 825))
r_slider_tut_tab1 = i.slider_tut_tab1.get_rect(center=(950, 762))
r_slider_tut_tab2 = i.slider_tut_tab2.get_rect(center=(950, 837))
r_slider_list = [r_slider_tut_tab1, r_slider_tut_tab2]
r_title = i.title.get_rect(center=(960, 250))
r_notice_101_a = i.notice_101_a.get_rect(center=(750, 450))
r_notice_101_b = i.notice_101_b.get_rect(center=(1720, 450))
