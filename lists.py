# Collection of multiple data are called list.

name = ['ali','khan','adil','zaman']
print(name)
type(name)
name[2]
name[1:]
name[-1]

data = [0.5,'abcd',65,True]        # we have add multiple type of data in one list.
data

num = [12,43,87,56]

# we have made two list working together

together = [name, num]
print(together)

# lists are mutiable. It means it will change the values.
num.append(99)
num.insert(2,77)
num.remove(56)
num.reverse()
num

# if i delete value by index number i will use pop() function. See example below.
num.pop(1)
num

# when we use pop() without given index value it will remove last value.
num.pop()
num

# To remove or delete multiple values at one time w will use "del" function.
del num[1:]
num

# To add multiple values at same time we use extend function.
num.extend([12,54,76,85])
num

# We perform other multiple operations like.
min(num)
max(num)
sum(num)

cities = ['karachi','lahore','islamabad','multan','sukur']
cities[1].upper()       # Result in upper-case
cities[2].title()       # Result in Captailize

AllTypes = ['string',1,True,5.5,['list','inside','list'],{'age':20}]
type(AllTypes)
AllTypes[5]['age']

"bilal arshad".title()

# Override list value
motorcycles = ['honda','yamha','suzuki']
print(motorcycles)
motorcycles[0] = 'unique'

# Add list value
motorcycles.append('honda')
motorcycles

# Inserting list value
motorcycles.insert(2,'super power')
motorcycles

# Removing an Item Using the pop() Method
bikes = ['honda', 'yamaha', 'suzuki'] 
print(bikes)
popped_motorcycle = bikes.pop()
print(bikes)
print(popped_motorcycle)