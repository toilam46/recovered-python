# Function: create a new user that takes a 1st name, last name and age, then return a dictionary with the user information
# Create type aliases User for a dictionary with string keys and values that can be either string, int, or None
User = dict[str, str | int | None]

def create_user(
    first_name: str, 
    last_name: str, 
    age: int | None = None) -> User:

    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email": email      
    }
    return user
# Example usage
new_user1 = create_user("John", "Doe", 30)
print(new_user1)
new_user2 = create_user("Thi", "Lam")
print(new_user2)
