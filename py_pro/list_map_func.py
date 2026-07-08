#Square numbers in a list using map() function and lambda function
li = [1, 2, 2, 3, 4, 5, 6, 7, 8, 1]

def square_list(values):
    return list(map(lambda x: x * x, values))


if __name__ == "__main__":
    print(square_list(li))
