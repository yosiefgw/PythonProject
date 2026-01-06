string_1 = 'Good'
string_2 = " day"
string_3 = string_1 + string_2
print(string_3)
print('Hello ' + 'World')
print(len(string_3))
my_string = 'Hello World'
print(my_string[4])
print(my_string[1:7]) # from position 1 to 5
print(my_string[:5]) # from start to position 5
print(my_string[2:]) # from position 2 to the end
print('*' * 10)
print('Hi' * 10)
title = 'The Good, The Bad, and the Ugly'
print(title.split(' '))
my_string = 'Count, the number     of spaces'
print("my_string.count(' '):", my_string.count(' '))
welcome_message = 'Hello World!'
print(welcome_message.replace("Hello", "Goodbye"))
print('Edward Alun Rawlings'.find('Alun'))
print('Edward John Rawlings'.find('Alun'))
msg = 'Hello Lloyd you are ' + str(21)
print(msg)
print('James' == 'James') # prints True
print('James' == 'John') # prints False
print('James' != 'John') # prints True
print('James' == 'james') # prints False
some_string = 'Hello World'
print('Testing a String')
print('-' * 20)
print('some_string', some_string)
print("some_string.startswith('H')",
some_string.startswith('H'))
print("some_string.startswith('h')",
some_string.startswith('h'))
print("some_string.endswith('d')", some_string.endswith('d'))
print('some_string.istitle()', some_string.istitle())
print('some_string.isupper()', some_string.isupper())
print('some_string.islower()', some_string.islower())
print('some_string.isalpha()', some_string.isalpha())
print('String conversions')
print('-' * 20)
print('some_string.upper()', some_string.upper())
print('some_string.lower()', some_string.lower())
print('some_string.title()', some_string.title())
print('some_string.swapcase()', some_string.swapcase())
print('String leading, trailing spaces', " xyz ".strip())
print(some_string.isupper)
print(some_string.isupper())
format_string = 'Hello {}!'
print(format_string.format('Phoebe'))
# Allows multiple values to populate the string
name = "Adam"
age = 20
print("{} is {} years old".format( name, age ))
# Can specify an index for the substitution
format_string = "Hello {1} {0}, you got {2}%"
print(format_string.format('Smith', 'Carol', 75))
x = 1
print(x)
print(type(x))
x = 100000000000000000000000000000000000000000000000000000000001
print(x)
print(type(x))
total = int('100')
print(total)
age = int(input('Please enter your age:'))
print(type(age))
print(age)
i = int(1.7)
print(i)
exchange_rate = 1.83
print(exchange_rate)
print(type(exchange_rate))
int_value = 1
string_value = '1.5'
float_value = float(int_value)
print('int value as a float:', float_value)
print(type(float_value))
float_value = float(string_value)
print('string value as a float:', float_value)
print(type(float_value))
exchange_rate = float(input("Please enter the exchange rate to use: "))
print(exchange_rate)
print(type(exchange_rate))
c1 = 1j
c2 = 2j
print('c1:', c1, ', c2:', c2)
print(type(c1))
print(c1.real)
print(c1.imag)
all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))
print(int(True))
print(int(False))
print(bool(1))
print(bool(0))
winner = None
print('winner:', winner)
print('winner is None:', winner is None)
print('winner is not None:', winner is not None)
print(type(winner))
print('Set winner to True')
winner = True
print('winner:', winner)
print('winner is None:', winner is None)
print('winner is not None:', winner is not None)
print(type(winner))

