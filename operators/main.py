# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

#Setting variables
fav_lang_Spain = 'Spanish'
fav_lang_Swits = 'Swiss' #Zwitserland
most_religions_Spain = 'Roman Catholic'
most_religions_Swits = 'Roman Catholic'
capital_Spain = 'Madrid'
capital_Swits = 'Bern'
gdp_spain = 1714860000000
gdp_swits = 590710000000
growth_spain = '1,95%'
growth_swits = '0,65%'
populatie_spain = 47163418
populatie_swits = 8508698

#vergelijkingen
fav_taal = fav_lang_Swits == fav_lang_Spain #01
most_religions = most_religions_Spain == most_religions_Swits #02
length_capital = (len(capital_Spain)!= len(capital_Swits)) #03
swits_gdp_greater_than = gdp_swits > gdp_spain #04
overall_growth_spain = growth_spain < '1%'
overall_growth_swits = growth_swits < '1%'
population_10mill_spain = populatie_spain > 10000000
population_10mill_swits = populatie_swits > 10000000

#print uitkomst
print (fav_taal) #01 false
print(most_religions) #02 true
print(swits_gdp_greater_than) #03 false
print(overall_growth_spain) #04 false
print(overall_growth_swits) #05 true
print(population_10mill_spain) #06 
print(population_10mill_swits)