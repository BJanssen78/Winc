# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

from gettext import find


spelers_NL = ["hans van breukelen", "berry van aerle", "frank rijkaard",
"ronald koeman", "adri van tiggelen", "gerard vanenburg", "jan wouters",
"arnold muchen", "erwin koeman", "ruud gullit", "marco van basten"]
spelers_NL_nr = ["1", "6", "17", "4", "2", "7", "20", "8", "13", "10", "12"]

spelers_SU = [
"Rinat Dasayev",
"Anatoliy Demyanenko",
"Sergei Aleinikov",
"Vagiz Khidiyatullin",
"Vasyl Rats",
"Hennadiy Lytovchenko",
"Oleksandr Zavarov",
"Oleksiy Mykhaylychenko",
"Sergey Gotsmanov",
"Oleh Protasov",
"Igor Belanov"]
spelers_SU_nr = ["1", "5", "7", "3", "6", "8", "9", "15", "18", "10", "11"]

doelpunt_speler = ["Ruud Gullit", "Marco van Basten"]
doelpunt_tijd = ["32", "54"]

scorers = (doelpunt_speler[0]) + ' ' + (doelpunt_tijd[0]) + (', ') + (doelpunt_speler[1]) + ' ' + (doelpunt_tijd[1])
report = (doelpunt_speler[0]) + ' scored in the ' + (doelpunt_tijd[0] + 'nd minute') + ('\n') + (doelpunt_speler[1]) + ' scored in the ' + (doelpunt_tijd[1] + 'th minute')

print (report)

player = 'Gerard Vanenburg'
first_name = player[:player.find(' ')]
last_name_len = len(player[player.find(' ')+1:])
name_short = player[:1] + '. ' + player[7:]
goal_0 = 32
goal_1 = 54
goal_2 = len(first_name) -2

chant = first_name + '!' + ' ' +((first_name + '! ') * goal_2) +  first_name +'!'
chant2 = len(chant[:chant.find('!')])
chant3 = chant2 * goal_2
good_chant = chant != 'Gerard! Gerard! Gerard! Gerard! Gerard! Gerard! '

print(2 != 3)
print(2 != 2)
print (chant)
print (chant2)
print (chant3)
print (spelers_NL+[spelers_NL_nr])