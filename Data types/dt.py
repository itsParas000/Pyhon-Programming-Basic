# print data types


# int Data Type
x = 5
print(type(x))

# str (String) Data Types
y = "Hello World"
print(type(y))

# float Data Types 
a = 20.5
print(type(a))

# Bool Data Types
b = True
print(type(b))

# byte Data Type
c = b"Hello"
print(type(c))


# mutable and immutable in python


# 1. List (List is mutable we can change it any time by adding and removing)

my_list = [1, 2, 3]
# 3 ways to add elements into list
my_list.append(4)
my_list.extend([7])
my_list.insert(4,90)
print(my_list)


# 3 ways to Remove Element from List
my_list.remove(90)
my_list.pop(4)
del my_list[2]
print(my_list)




# Change elements
my_list[0] = 20


# 2. Tuple (Tuple is Immuatble we can't add and remove elements)

my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4, )
print('\n Original',my_tuple)
print('\n New Tuple',new_tuple)


# 3. Dict (Dict is mutable we can change the element from it)

my_dict = {'a':1, 'b':2, 'c':3}
my_dict['d'] = 4
my_dict['a'] = 0
del my_dict['a']
my_dict.pop('b')
print(my_dict)


# 4. Set (Set is muatble we can change element by adding and removing)

my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(1)
print(my_set)