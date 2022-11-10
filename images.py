import pygame

bg_00 = pygame.image.load("sprites/bg_0.jpg")
title = pygame.image.load("sprites/name_title.png")

bg_10 = pygame.image.load("sprites/bg_1.png")
mask_tut1_3 = pygame.image.load("sprites/mask_tut1_3.png")
mask_tut1_3.set_alpha(155)

button_start = pygame.image.load("sprites/button_start.png")
button_next = pygame.image.load("sprites/button_next.png")
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