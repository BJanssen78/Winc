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

#01 The language spoken the most in Switzerland is the same as in Spain.
fav_taal = fav_lang_Swits == fav_lang_Spain
#02 The most prevalent religion in Switzerland is the same as in Spain.
most_religions = most_religions_Spain == most_religions_Swits
#03 The name length of Spain's capital does not equal that of Switzerland.
length_capital = (len(capital_Spain)!= len(capital_Swits))
#04 Switzerland's GDP is greater than Spain's GDP.
swits_gdp_greater_than = gdp_swits > gdp_spain
#05 The population growth is less than 1% in Switzerland and Spain.
overall_growth_spain = growth_spain < '1%'
overall_growth_swits = growth_swits < '1%'
overall_growth = growth_spain and growth_swits < '1%'
#06 At least one of the two countries has a population count of over 10 million.
population_10mill_spain = populatie_spain > 10000000
population_10mill_swits = populatie_swits > 10000000
population = populatie_spain > 10000000 or populatie_swits >= 10000000

#07 Exactly one of the two countries has a population count of over 10 million.
population_at_least_one = populatie_swits and populatie_spain > 10000000

#print uitkomst
print (fav_taal) #01 false
print(most_religions) #02 true
print (length_capital) #03 true
print(swits_gdp_greater_than) #04 false
print(overall_growth) #05 false
print(population) #06 true
print(population_at_least_one) #07 true