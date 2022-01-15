"""
comment multiline
variable declaration
Data Types Primitive Numbers initialize
"""
num1 = 42

"""
comment multiline
variable declaration
Data Types Primitive Numbers initialize
"""
num2 = 2.3

"""
comment multiline
variable declaration
Data Types Primitive Boolean initialize
"""
boolean = True

"""
comment multiline
variable declaration
Data Types Primitive Strings initialize
"""
string = 'Hello World'

"""
comment multiline
variable declaration
Data Types Composite List initialize
"""
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

"""
comment multiline
variable declaration
Data Types Composite Dictionary initialize
"""
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

"""
comment multiline
variable declaration
Data Types Composite Tuples initialize
"""
fruit = ('blueberry', 'strawberry', 'banana')

"""
comment multiline
log statement
type check
Data Types Composite Tuples
"""
print(type(fruit))

"""
comment multiline
log statement
Data Types Composite List access value
"""
print(pizza_toppings[1])

"""
comment multiline
Data Types Composite List add value
"""
pizza_toppings.append('Mushrooms')

"""
comment multiline
log statement
Data Types Composite Dictionary access value
"""
print(person['name'])

"""
comment multiline
Data Types Composite Dictionary change value
"""
person['name'] = 'George'

"""
comment multiline
Data Types Composite Dictionary add value
"""
person['eye_color'] = 'blue'

"""
comment multiline
log statement
Data Types Composite Tuples access value
"""
print(fruit[2])


# conditional if, comment single line
if num1 > 45:
    # log statement, comment single line
    print("It's greater")
# conditional else, comment single line
else:
    # log statement, comment single line
    print("It's lower")

# conditional if, comment single line
if len(string) < 5:
    print("It's a short word!")
# conditional else if, comment single line
elif len(string) > 15:
    print("It's a long word!")
# conditional else, comment single line
else:
    print("Just right!")

# for loop, comment single line
for x in range(5):
    #log statement, comment single line
    print(x)
# for loop stop, comment single line

# for loop 
for x in range(2,5):
    #log statement, comment single line
    print(x)
# for loop stop, comment single line

# for loop
for x in range(2,10,3):
    #log statement, comment single line
    print(x)
# for loop stop, comment single line

# variable declaration , Data Types Primitive Number, comment single line
x = 0
# while loop start, comment single line
while(x < 5):
    # log statement, comment single line
    print(x)
    # while loop increment, comment single line
    x += 1
# while loop stop, comment single line

# Data Types Composite List delete value, comment single line
pizza_toppings.pop()
pizza_toppings.pop(1)

# log statement, comment single line, Data Types Composite Dictionary
print(person)

# Data Types Composite Dictionary delete value
person.pop('eye_color')

# log statement, comment single line, Data Types Composite Dictionary
print(person)

"""
for loop start sequence
Data Types Composite List
comment multiline
"""
for topping in pizza_toppings:
    # conditional if, comment single line
    if topping == 'Pepperoni':
        # for loop continue, comment single line
        continue

    # log statement, comment single line
    print('After 1st if statement')

    # conditional if, comment single line
    if topping == 'Olives':
        # for loop break, comment single line
        break
# for loop stop, comment single line

# function, comment single line
def print_hello_ten_times():
    """
    for loop start sequence
    comment multiline
    """
    for num in range(10):
        # log statement, return comment single line
        print('Hello')

# function call
print_hello_ten_times()

# function, parameter, comment single line
def print_hello_x_times(x):
    # for loop continue, argument, comment single line
    for num in range(x):
        # log statement, return, comment single line
        print('Hello')

# function call, argument
print_hello_x_times(4)

# function, parameter with default value, comment single line
def print_hello_x_or_ten_times(x = 10):
    # for loop continue, argument, comment single line
    for num in range(x):
        # log statement, return, comment single line
        print('Hello')

# function call comment single line
print_hello_x_or_ten_times()
# function call, argument, comment single line
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)