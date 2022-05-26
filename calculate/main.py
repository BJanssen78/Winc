# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line

#items list
broccoli = leek = 2
potato = 3
brussel_sprout = 7
#end item list

sum_one_each = broccoli + leek + potato + brussel_sprout

avg_price = sum_one_each / 4

#shopping list
num_potatoes = 7
num_broccolis = 5
num_leeks = 2
num_brussel_sprouts = 10
#end shopping list

sum_total = broccoli * num_broccolis + potato * num_potatoes + leek * num_leeks + brussel_sprout * num_brussel_sprouts

discount_percentage = 30

discounted_sum_total = sum_total - sum_total / 100 * discount_percentage

print (discounted_sum_total)