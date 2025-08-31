i = 0
while i < 11:
    print(i)
    i +=1

print('\nDesencding:')
j = 10
while i >=0:
    print(i)
    i -=1
    
print('\nTriangle:')
for i in range(1,8):
    line = ''
    for j in range(i):
        line += '#'
    print(line)

print('\nTriangle2')
for i in range(1,8):
    print('#'*i)

print('\nVariation 2:')
for i in range(1, 11): # print the row
    l = '#' 
    for j in range(1, 11): # print the column
        l += '#' # add another '#' each iteration
    print(l)

print('\nNew Pattern:')
i = 0
while i < 11:
    print (i)
    i += 1 
    while j < i:
        j *= i
    print (i)

