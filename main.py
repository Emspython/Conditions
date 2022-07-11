# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

# List of Factors to check

weather = ['rainy', 'sunny','windy','neutral']
time_of_day = ['day', 'night']
cow_milking_status = ['day', 'night'] # True/False
location_of_the_cows = ['pasture', 'cowshed']
season = ['winter','spring', 'summer', 'fall']
slurry_tank = ['full', 'not full'] # True/False
gras_status = ['long', 'short']

# Actions
#take cows to cowshed when on pasture at night OR the cows are standing in the rain

#milk_cows when need milking AND the cows are in cowshed 

#fertilize pasture when the cows are in the cowshed AND the weather is not sunny OR windy

#mow_grass the grass is long AND its spring AND the weather is sunny AND WHEN the cows are not on the pasture

#wait IF no Action applies

###take cows to cowshed take cows back to pasture

def farm_action(weather,time_of_day,cow_milking_status,location_of_the_cows,season,slurry_tank,gras_status):
    if(location_of_the_cows == 'pasture' and time_of_day == 'night' and location_of_the_cows == 'pasture' and weather == 'rainy'):
        return "take cows to cowshed"
    elif(cow_milking_status == True and location_of_the_cows == 'cowshed'):
        return('milk cows')
    elif(cow_milking_status == True and location_of_the_cows != 'cowshed'):
        return('take cows to cowshed\nmilk cows\ntake cows back to pasture')
    elif(slurry_tank == True and location_of_the_cows == 'cowshed' and weather != 'sunny' and 'windy'):
        return('fertilize pasture')
    elif(gras_status == True and season == 'spring' and weather == 'sunny' and location_of_the_cows != 'pasture'):
        return('mow grass')
    else:
        return('wait')
    
print(farm_action('sunny', 'day', True, 'pasture','spring',False, True))

    

