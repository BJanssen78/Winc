# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

#lijst met factors om te checken.


f_weather = ['rainy','sunny','windy','neutral']
f_time_of_day = ['day','night']
f_cow_milking_status = ['need milking','Don\'t need milking']#True or False
f_location = ['pasture','cowshed']
f_season = ['winter','spring','summer','fall']
f_slurry_tank = ['Full','Not full']#True or False
f_grass_status = ['Long','Short']#True or False
#einde lijst, verwijderen na succes.

def farm_action(weather,time_of_day,cow_milking_status,location,season,slurry_tank,grass_status):
    if weather == 'rainy' or time_of_day == 'night' and location == 'pasture':
        print('Take cows to cowshed')
        action = 'Take cows to cowshed'
        return action
    elif cow_milking_status == True and location == 'cowshed':
        print('milk cows')
        action = 'milk cows' + '\n'
        return action
    elif weather != 'sunny' or weather != 'windy' and location == 'cowshed' and slurry_tank == True:
        print('fertilize pasture')
        action = 'fertilize pasture'
        return action
    elif weather == 'sunny' and season == 'spring' and grass_status == True and location != 'pasture':
        print('mow grass')
        action = 'mow grass'
        return action
    else:
        print('wait')
        return False
results = f"""{farm_action('sunny','day',True,'cowshed','spring',False,True)}
{farm_action('sunny','day',True,'cowshed','spring',False,True)}"""
