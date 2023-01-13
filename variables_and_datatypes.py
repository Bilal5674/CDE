#intiger
2 + 3       # Direct Intiger

x = 5       # Store In Variable
x = 13      # We can easily override intiger values
x + 8

y = 6
8 + y

x + y
# For get the output of the previous operation we use "_" underscore.
_ + y       #Here we get output of previous operation and add the value of "y".

# String variables
name = "Hello"
print(name)

name + ' World'     # For addition with name

text = "youtube"
text[0]         # Fetch in array
text[5]
text[-1]        # When we start with "-" sign it will start from right to left (Reverse order).
text[-5]
text[0:4]       # When we put ":" between to values it means it will start from 1st value to 1 less from 2nd value(exclusive from 2nd value).
text[1:4]       # It start from "o" and ends on "t".
text[2:]        # In this case it will start from 2 and goes till the end.
text[:5]        # When we just give ending point it will start from "0" and end oneless from ending point. In this case it will go from 4.

# Once we assign a value in string operator. we cannot over and change it.
# if we change some letters like "youtube" to "my tube" then we do something like that see below:

"My " + text[3:7]
'''Or'''
"My " + text[3:]

# For find length of variale
myname = "Bilal Arshad"
len(myname)

#Floats
1.1 + 5.6

# Intiger and Floats
12 + 2.5

# Underscores in Numbers
universe_age = 10_000_000_000
type(universe_age)
print(universe_age)

# Multiple Assignment
x, y, z = 0, 1, 2

# Constants
MAX_CONNECTIONS = 5000

# Range
range(10)
type(range)

list(range(20))
