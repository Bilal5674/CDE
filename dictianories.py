# In dictionaries we wil use key and values.

data = {'color':'red','point':5}
type(data)
data['point']
data.keys()
data.values()

xyz = {'color':'blue'}
print(xyz['color'])
print(xyz.get('color','Not Found'))

xyz['color'] = 'red'
xyz['color']

new_point = data['point']
print(f"You score {new_point} points!")

# Adding New Key-Value Pairs
data = {'color':'brown','point':10}
print(data)
data['x_position'] = 0
data['y_position'] = 25
print(data)
data.update({'new_key':'value','key2':'value2'})
print(data)

# Starting with an Empty Dictionary
data = dict()
data['color'] = 'yellow'
data['price'] = 20
data

# Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

