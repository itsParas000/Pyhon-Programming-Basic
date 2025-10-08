# creating first function

print('\n Basic Function')
def my_function1():
    print('hello from a function')

my_function1()


# With Arguments
print('\n With Arguments')

def my_function(fname):
    print('hello!! ' + fname)
    
my_function('paras')
my_function('nishant')
my_function('sona')




# Function Paasing a list as argument
print('\n Function Paasing a list as argument')
def my_function2(food):
    for x in food:
        print(x)

fruits = ['apple', 'banana', 'chiku']

my_function2(fruits)


# Return Values
print('\n Return Values')

def my_function3(x):
    return 5 * x

print(my_function3(3))
print(my_function3(5))
print(my_function3(9))