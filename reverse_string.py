newstring = ''
oldstring = 'Newton'
for char in oldstring:
	newstring = char + newstring
	print(f'char:{char} | newString:{newstring}')
print(newstring)
