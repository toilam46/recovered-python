
from typing import List, Dict, Set, Tuple, Any, Sequence, Mapping, Optional, Callable, Union, TypeVar
# This code demonstrates the use of Python's typing module to specify types for variables. All are passed without any errors, as the types are correctly assigned.

x: List[List[int]] = [[1,2], [3,4]]

y: Dict[str, str] = {'a': "apple", 'b': "banana"}

z: Set[int] = {1, 2, 3}

w: Tuple[int, str] = (5, "five")

# Now, let's define a function that uses type annotations for its parameters and return type.
Vector = List[float]
def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]
scaled_vector = scale(2.0, [1.0, 2.0, 3.0])
print(scaled_vector)  # Output: [2.0, 4.0, 6.0] 

# Now make my own custom type for a list of vectors.
Vectors = List[Vector]
def foo(v: Vectors) -> Vector:
    return [sum(vector) for vector in v]
result = foo([[1.0, 2.0], [3.0, 4.0]])
print(result)  # Output: [3.0, 7.0]

# Any type can be used when you want to allow any type of value. However, it's generally better to be specific about types to catch potential errors.   
def process_data(data: Any) -> None:
    print(f"Processing data: {data}")
process_data("Hello, World!")  # Output: Processing data: Hello, World!
process_data(123)  # Output: Processing data: 123
process_data([1, 2, 3])  # Output: Processing data: [1, 2, 3]  

# Sequence and Mapping are more general types that can be used when you want to allow any sequence (like lists, tuples) or mapping (like dictionaries) without specifying the exact types of their elements.
def print_sequence(seq: Sequence[int]) -> None:
    for item in seq:
        print(item)
print_sequence([1, 2, 3])  # Output: 1 2 3
def print_mapping(mapping: Mapping[str, int]) -> None:
    for key, value in mapping.items():
        print(f"{key}: {value}")
print_mapping({'a': 1, 'b': 2})  # Output: a: 1 b: 2  

#Now Callable and Union types can be used to specify that a variable can be a function or one of several types, respectively.
def add(x: int, y: int) -> int:
    return x + y
def apply_operation(operation: Callable[[int, int], int], a: int, b: int) -> int:
    return operation(a, b)
result = apply_operation(add, 5, 3)
print(result)  # Output: 8
def process_value(value: Union[int, str]) -> None:
    if isinstance(value, int):
        print(f"Processing integer: {value}")
    elif isinstance(value, str):
        print(f"Processing string: {value}")
process_value(42)  # Output: Processing integer: 42
process_value("Hello")  # Output: Processing string: Hello  

#Lambda functions can also be annotated with types.
def apply_function(func: Callable[[int], int], value: int) -> int:
    return func(value)
result = apply_function(lambda x: x * 2, 5)
print(result)  # Output: 10 

#Now Typevar can be used to create generic types that can work with any type.
T = TypeVar('T')
def identity(value: T) -> T:
    return value
print(identity(42))  # Output: 42
print(identity("Hello"))  # Output: Hello   

def get_first_element(lst: List[T]) -> Optional[T]:
    if lst:
        return lst[0]
    return None
print(get_first_element([1, 2, 3]))  # Output: 1
print(get_first_element([]))  # Output: None    

# Interesting to note that the __annotations__ attribute of the function will show the types that were specified in the function definition. This can be useful for introspection or debugging purposes.
get_first_element.__annotations__  # Output: {'lst': typing.List[~T], 'return': typing.Optional[~T]}    
print(get_first_element.__annotations__)  # Output: {'lst': typing.List[~T], 'return': typing.Optional[~T]} 




