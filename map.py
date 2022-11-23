import images as i
import rects as r

map = {
    'area_1':{
        'type' : 'blank', 
        },
    'area_2':{
        'type' : 'blank',
    },
}

def choose_image(plant):
    if (plant == 'hydro'):
        image = i.plant_hydro
    elif (plant == 'wind'):
        image = i.plant_wind
    elif (plant == 'solar'):
        image = i.plant_solar
    elif (plant == 'nuclear'):
        image = i.plant_nuclear
    elif (plant == 'coal'):
        image = i.plant_coal
    elif (plant == 'gas'):
        image = i.plant_gas
    else:
        image = i.blank_area
    return image

def choose_rect(area):
    rect = 0
    if (area == 'area_1'):
        rect = r.area_1
    elif (area == 'area_2'):
        rect = r.area_2
    return rect