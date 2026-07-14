'''given a String S, you need to print its characters at even indices(index starts at 0).
'''
S = input("Enter a string: ")
print(''.join(ch for i, ch in enumerate(S) if i % 2 == 0))