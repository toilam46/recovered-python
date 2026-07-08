#Filter odd numbers from a list using filter() function and lambda function
li = [1, 2, 2, 3, 4, 5, 6, 7, 8, 1]

def filter_odd(values):
    return list(filter(lambda x: x % 2 != 0, values))

if __name__ == "__main__":
    print(filter_odd(li))
