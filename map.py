import images as i
import rects as r

map = {
    'area_1':{
        'type' : 'hydro', 
        },
    'area_2':{
        'type' : 'nuclear',
    },
    'area_3':{
        'type' : 'nuclear',
    },
    'area_4':{
        'type' : 'hydro',
    },
    'area_5':{
        'type' : 'hydro',
    },
    # Greenfield (gas)
    'area_6':{
        'type' : 'gas',
    },
    # Goreway
    'area_7':{
        'type' : 'gas',
    },
    # Lennox
    'area_8':{
        'type' : 'gas',
    },
    # Nanticoke (coal)
    'area_9':{
        'type' : 'coal',
    },
    # Lambton (coal)
    'area_10':{
        'type' : 'coal',
    },
    # Prince (wind but blank to start)
    'area_11':{
        'type' : 'blank',
    },
    # South Kent (wind but blank to start)
    'area_12':{
        'type' : 'blank',
    },
    # K2 Wind (wind but blank to start)
    'area_13':{
        'type' : 'blank',
    },
    # Nanticoke Solar (solar but blank to start)
    'area_14':{
        'type' : 'blank',
    },
    # Potential site
    'area_15':{
        'type' : 'blank',
    },
}

loads = {
    # Toronto
    'toronto':{
        'type' : 'blank',
        'image' : i.toronto,
        'rect' : r.toronto,
    },
    # Ottawa
    'ottawa':{
        'type' : 'blank',
        'image' : i.ottawa,
        'rect' : r.ottawa,
    },
    # Windsor
    'windsor':{
        'type' : 'blank',
        'image' : i.windsor,
        'rect' : r.windsor,
    },
    # Sudbury
    'sudbury':{
        'type' : 'blank',
        'image' : i.sudbury,
        'rect' : r.sudbury,
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
    elif (area == 'area_3'):
        rect = r.area_3
    elif (area == 'area_4'):
        rect = r.area_4
    elif (area == 'area_5'):
        rect = r.area_5
    elif (area == 'area_6'):
        rect = r.area_6
    elif (area == 'area_7'):
        rect = r.area_7
    elif (area == 'area_8'):
        rect = r.area_8
    elif (area == 'area_9'):
        rect = r.area_9
    elif (area == 'area_10'):
        rect = r.area_10
    elif (area == 'area_11'):
        rect = r.area_11
    elif (area == 'area_12'):
        rect = r.area_12
    elif (area == 'area_13'):
        rect = r.area_13
    elif (area == 'area_14'):
        rect = r.area_14
    elif (area == 'area_15'):
        rect = r.area_15
    return rect