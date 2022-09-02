# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line



def greet(name):
    greetings = 'Hello, '
    return f'{greetings}{name}!'

greetints = greet('Fred')
print(greetints)

def add(a,b,c):
    calc1 = a + b + c
    return calc1

sum = add(2,10,8.5)
print(sum)

def positive(number):
    is_positive = number > 0
    return is_positive

match = positive(2)
match2 = positive(-1)

def negative(number):
    is_negative = number < 0
    return is_negative

match3 = negative(2)
match4 = negative(-1)
print(match3)
print(match4)