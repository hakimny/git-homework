#Nested Lists

x = [['pepper', 'zucchini', 'onion'],
     ['cabbage', 'lettuce', 'garlic'],
     ['apple', 'pear', 'banana']]

print(x[0])
print(x[0][1])
x[0].append(100)
x[1].append(200)
x[2].append(300)
print(f'x: {x}')
print(f'poping 2nd element of 2nd list :{x[1].pop(1)}')
print(f'x: {x}')
new_list = [0,1,2,3]
new_list.reverse()
print(f'reversed_list: {new_list}')

# Create list from String

str = "hello"
list = []
for char in str:
	list.append(char)
print(list)

# Slicing

string_for_slicing = "Observation date: 02-Feb-2013"
list_for_slicing = [["fluorine", "F"],
                    ["chlorine", "Cl"],
                    ["bromine", "Br"],
                    ["iodine", "I"],
                    ["astatine", "At"]]
start_slicing_index = len(string_for_slicing) - 4
print(string_for_slicing[start_slicing_index:])

for item in list_for_slicing:
	start_slicing_index = len(item) -4
	print(item[start_slicing_index:])

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
subset = primes[0:12:3]
print("subset", subset)
subset = primes[2:12:3]
print("subset", subset)

#Overloading

counts = [2, 4, 6, 8, 10]
repeats = counts * 2
print(repeats)
