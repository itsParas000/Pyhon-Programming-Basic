# Loops Are in Python

# While loop

# While loop with equal
print('Print with Equal')
i = 1
while i < 6:
    print(i)
    i += 1
    

# While loop without equal
print('\n Without Equal')
i = 1
while i <= 6:
    print(i)
    i += 1
    
    
# Brake Statement
print('With the Break Statement')
i = 1
while i <6:
    print(i)
    if i == 3:
        break
    i +=1
    



# Continue statement

print('\n With continue statement')
i = 0
while i <= 6:
    i += 1
    if i == 3:
        continue
    print(i)
    
    
    

# else Statement

print('\n  With else Statement')
i = 0
while i < 6:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')

