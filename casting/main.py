# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

leek_price = 2
new_string = f'Leek is {leek_price} euro per kilo.'
print(new_string)

leek_order = 'leek 4'
amount_leek = int(leek_order[leek_order.find(' ')+1:])
sum_total = amount_leek * leek_price

broccoli_price = 2.34
order_broccoli = 'broccoli 1.6'
amount_broccoli = (order_broccoli[order_broccoli.find(' ')+1:])
sum_broccoli_total = amount_broccoli * broccoli_price
