# For Loop in python

# with set
print('\n with set')
fruits = ['apple', 'banana', 'watermelon', 'chiku']
for i in fruits:
    print(i)
    
    
    
    
# With string
print('\n With stringS')
for x in 'String':
    print(x)
    


# With break statement
print('\n With break statement')
fruits1 = ['apple', 'banana', 'chiku', 'lemon', 'orange']
for x in fruits1:
    print(x)
    if x == 'banana':
        break
    
    

# Exit the loop when x is "banana", but this time the break comes before the print:
print('\n Exit the loop when x is "banana", but this time the break comes before the print:')
fruits2 = ['apple', 'banana', 'chiku', 'lemon', 'orange']
for x in fruits2:
    if x == 'banana':
        break
    print(x)


# With the continue statement we can stop the current iteration of the loop, and continue with the next:
print('\n With the continue statement we can stop the current iteration of the loop, and continue with the next:')
fruits2 = ['apple', 'banana', 'chiku', 'lemon', 'orange']
for x in fruits2:
    if x == 'banana':
        continue
    print(x)


# range function

print('\n Range Function')
for x in range(6):
    print(x)
    

print('\n Using start parameter')
for x in range(1,6):
    print(x)