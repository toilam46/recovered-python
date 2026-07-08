# Given a list. Write a program to traverse the list and print each element in the list with a space between them.   
list = [23,5,7,12,39,76,45,67,89,34]
for i in list:
    print(i, end=" ")

#Find the length of the list without using the built-in function len().
count = 0
for i in list:
    count += 1
print("\nLength of the list is:", count)

#Find the length of the list by using the built-in function len().
print("Length of the list using built-in function len():", len(list))

# Print the sum of a list of numbers.
sum = 0
for i in list:
    sum += i
print("Sum of the list is:", sum)