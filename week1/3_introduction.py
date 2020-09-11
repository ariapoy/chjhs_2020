# this is the first comment
spam = 1  # and this is the second comment
# ... and now a third!
text = "# This is not a comment because it's inside quotes."
print(spam)
print(type(spam))
print(text)
print(type(text))
# variables and values
x = 5
print(x)
print(hex(id(x)))
y_range = range(2 ** 16)
# list(y_range)[-1] danger code!
width = 20
height = 5 * 9
print(width * height)
try:
    print(n)
except Exception as e:
    print(e)

# Numbers: int and float
print(2 + 2)
print(50 - 5 * 6)
print((50 - 5 * 6) / 4)
print(8 / 5)
print(17 / 3)
print(17 // 3)
print(17 % 3)
print(5 * 3 + 2)
print(2 ** 2)
print(2 ** 7)
print(4 * 3.75 - 1)
# _
tax = 12.5 / 100
price = 100.50
print(tax * price)
tax_dot_price = tax * price
print(price + tax_dot_price)
print(round(tax_dot_price, 2))
c = 3 + 4j
print(c)
print(c.conjugate())
print(abs(c))
# Strings: str
print('spam eggs')
print('doesn\'t')
print("doesn't")
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')
# >>> '"Isn\'t," they said.'
print('C:\some\name')
print(r'C:\some\name')
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print(3 * 'un' + 'ium')
print('Py' 'thon')
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
prefix = 'Py'
print(prefix + 'thon')
word = 'Python'
print(word[0])
print(word[5])
print(word[-1])
print(word[-1])
print(word[0: 2])
print(word[2: 5])
print(word[:2] + word[2:])
print(word[2:])
print(word[:-2])
print(len(word))
try:
    print(word[42])
except Exception as e:
    print(e)
print(word[4:42])
print(word[42:])
try:
    word[0] = 'J'
except Exception as e:
    print(e)
print('J' + word[1:])
# format and f-string
i = 256 * 256
print('The value of i is', i)
print('The value of i is {0}'.format(i))
print(f'The value of i is {i}')
# Lists
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3:])
print(squares[:])
print(squares + [36, 49, 64, 81, 100])
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)
cubes + [8 ** 3]
print(cubes)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)
print(len(cubes))
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(len(x))
print(len(x[0]), len(x[1]))
print(x[0])
print(x[1][0])
# First programming
a, b = 0, 1
while a < 10:
    print(a)
    # a, b = a, a + b ctrl + c to stop it!
    a, b = b, a + b

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    # a, b = a, a + b ctrl + c to stop it!
    a, b = b, a + b
