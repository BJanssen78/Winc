# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

from gettext import find

#part 1

#poging 1 van de opdracht strings
doelpunt_speler = ['Ruud Gullit', 'Marco van Basten']
doelpunt_tijd = ['32', '54']

#poging 2 van de opdracht strings, na de feedback van de leraar.
scorer1 = 'Ruud Gullit'
scorer2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

#scores = een test van mezelf om te zien wat de uitkomst is.
scorers = (doelpunt_speler[0]) + ' ' + (doelpunt_tijd[0]) + (', ') + (doelpunt_speler[1]) + ' ' + (doelpunt_tijd[1])
#poging 1 van de opdracht strings
report = (doelpunt_speler[0]) + ' scored in the ' + (doelpunt_tijd[0] + 'nd minute') + ('\n') + (doelpunt_speler[1]) + ' scored in the ' + (doelpunt_tijd[1] + 'th minute')
#poging 2 van de opdracht strings, na de feedback van de leraar.
report2 = f'{scorer1} scored in the {goal_0}nd minute \n{scorer2} scored in the {goal_1}th minute'

#In de assignment staat bij part 1 punt 4 dat de F of de + operator gebruikt moet worden.
#Ik heb nu beide in de code staan.

#poging 1 van de opdracht strings
print (report + '\n')
print (scorers + '\n')
print (report2 + '\n') #poging 2 van de opdracht strings, na de feedback van de leraar.

#Strings part 2

player = 'Gerard Vanenburg' #punt 1
first_name = player[:player.find(' ')] #punt 2
last_name_len = len(player[player.find(' ')+1:]) #punt 3
name_short = player[:1] + '.' + player[player.find(' '):] #punt4

#punt 5
chant2 = (first_name + '!' + ' ') * len(first_name)
size = len(chant2)
chant = chant2[:size - 1]
good_chant = chant[-1] != ' '

#count length from chant to check the values
size_chant = len(chant)
size_chant2 = len(chant2)


print (chant + '\n')
print (good_chant)


