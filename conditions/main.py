# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line




def farm_action(weather,time_of_day,milking_status,location,season,slurry_tank_full,grass_status_long):
    if weather == 'rain' or time_of_day == 'night':
        print('Take cows to cowshed')
        return True
    elif milking_status == 'full' and location == 'cowshed':
        print('Start milking cows')
        return True
    elif milking_status == 'full' and location == 'pasture':
        print('Bring cows to cowshed for milking')
        return True
    elif slurry_tank_full == 'full' and location == 'cowshed' and weather != 'sunny' or 'windy':
        print('Fertilize pasture')
        return True
    elif grass_status_long == 'Long' and weather == 'sunny' and season == 'Spring' and location == 'cowshed':
        print('Start mowing the grass')
        return True
    else:
        print('Wait')
        return False