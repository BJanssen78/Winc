#part 1

#01 Create a variable leek_price with an integer value of 2.
leek_price = 2
#02 Cast this into a string and use the +-operator to print a string like this one, only with the correct price in it:
leek = f'Leek is {leek_price} euro per kilo.'
print (leek)

#part 2

#01 We got an order for four leeks! Store the string 'leek 4' in a variable.
order_leek = 'leek 4'
#02 Use find and slicing to extract the number from this string.
amount_leek = order_leek[order_leek.find(' ')+1:]
#03 Cast it into an integer.
total_order = int(amount_leek)
#04 Use this and leek_price to compute the sum total and store it in sum_total. Print out the value for this variable.
sum_total = total_order * leek_price
print (sum_total)

#part 3

#01 Create one variable for the broccoli price and one for the order.
price_broccoli = 2.34
order_amount = 1.6
#02 Compute the total price for this order.

total_price_broccoli = round(price_broccoli * order_amount,2)
#03 Use the +-operator to assemble and print a string that looks like the following:
output_string_casting = (order_amount+'kg broccoli cost '+ total_price_broccoli)
print (output_string_casting)
