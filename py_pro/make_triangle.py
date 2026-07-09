def make_triangle(n):
    """
    Create a triangle of asterisks with n rows.
    Args:
        n (int): The number of rows in the triangle.
    Returns:
        str: A string representation of the triangle.
    Add code to print the triangle for a given number of rows.
    """
    triangle = ""
    for i in range(1, n + 1):
        triangle += "*" * i + "\n"
    return triangle

if __name__ == "__main__":
    rows = 5
    print(make_triangle(rows))

