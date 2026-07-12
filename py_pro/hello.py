print("Hello from python on WSL! This is a test to see if it works with the new WSLg support for GUI applications.")
print(2 ** 0.5)

a = ['m','b']
b = ['c', 'd','m']

print('id of a is: ', id(a))
c = [item.upper() for item in b if item in a]
print('id of c is diff. from that of a: ',id(c))

print('With colon [:] the modified list is the same as its original. No need to create a new list.\
c ''s list comprehension')
b[:] = [item.upper() for item in b if item in a ]
print(id(a))
print(b)


print('\nAnother example of list comprehension;')
square = []
for x in range(10):
    square.append(x**2)
print(square)

square = [x**2 for x in range(10) if x % 2 == 0]
print(square)


print('Click the triangle icon in the upper right corner to run the code in a new terminal window. You can also run it from the command line with: python3 hello.py')
