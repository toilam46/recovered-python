#create a new list using odd-indexed elements from the first list and even-indexed elements from the second list
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
new_list = [list1[i] for i in range(1, len(list1), 2)] + [list2[i] for i in range(0, len(list2), 2)]    
print(new_list)  # Output: [2, 4, 6, 8, 10] 
