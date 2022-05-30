from sre_constants import JUMP


output = '''dit moet een multiline zijn,
dit zou dus "gewoon" moeten werken.
En we gaan gewoon \n door met het typen, van deze tekst,
om te zien of\tdit gaat werken\n
het lijkt gewoon te werken \a \b zoals 'bedoeld' is\n\n'''

single_output = 'hier een enkele quote \' op de line'

print (output, single_output)

#operant les
'Hello' + 'world'
'Jump! ' * 5
"""
'Samuel' in 'We went out for dinner with with Anne, Samuel and Bob.'
'Shane' in 'We went out for dinner with with Anne, Samuel and Bob.'
5 in 'We were lucky that they had a table for 5.'
str(5) in 'We were lucky that they had a table for 5.'
"""
waltz = 'onetwothree'
waltz[0:3]
# We don't need to specify the 0 if we start at the beginning
waltz[:3]
waltz[3:6]
waltz[6:11]
# Same goes for the end -- we can leave it empty
waltz[6:]
# We can specify a step size if we don't want a continuous slice
waltz[0:11:2]

print(waltz)

sentence = 'The length of this string is:'
print(sentence, len(sentence))
print('Wait.. You just made it longer!')

print('\n\n')

answer = 42
qa = f'The answer is.. {answer}'
qa2 = (qa + answer)
qa3 = (qa and answer)
