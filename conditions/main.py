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
    action = ''
    # check of de koeien naar de schuur moeten
    if (weather == 'rainy' or time_of_day == 'night') and location == 'pasture':
        action += 'take cows to cowshed'  
    # check of er gemolken moet worden
    if cow_milking_status == True and location == 'cowshed':
        action += 'milk cows'
        if weather != 'rainy':
            action += '\ntake cows back to pasture'  
    # check op de juiste locatie            
    if cow_milking_status == True and location == 'pasture':
        action += 'take cows to cowshed\nmilk cows'
        # extra check of ze terug moeten
        if weather != 'rainy' and slurry_tank == False:
            action += '\ntake cows back to pasture'    
              
    if (weather != 'sunny' or weather != 'windy') and location == 'cowshed' and slurry_tank == True:
        action += 'fertilize pasture'
        if weather != 'rainy':
            action += '\ntake cows back to pasture'
                  
    if (weather != 'sunny' or weather != 'windy') and location == 'pasture' and slurry_tank == True:
        action += '2take cows to cowshed\nfertilize pasture'
        if weather != 'rainy':
            action += '\ntake cows back to pasture'      
            
    if weather == 'sunny' and season == 'spring' and grass_status == True and location != 'pasture':
        action += 'mow grass'
        return (action)   
    if action != '': #extra controle
        # print(action) #extra toevoeging om te zien of wincpy nu werkt.
        return(action)
    else:
        action = 'wait'
        return (action)

                
# farm_action('sunny','day',True,'pasture','spring',False,True);
print (farm_action('sunny', 'day', True, 'cowshed', 'spring', False, True));

