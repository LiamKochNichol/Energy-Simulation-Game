import pygame
import images as i

r_button_start = i.button_start.get_rect(center=(683, 600))
r_button_next = i.button_next.get_rect(center=(1050, 700))
r_button_run = i.button_run.get_rect(center=(1050, 600))

# Nuclear power plant rect
nuclear_rect = i.nuclear_image.get_rect()
nuclear_rect.center = (100,100)