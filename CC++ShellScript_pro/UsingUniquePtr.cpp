// Program to use the smart unique_ptr in modern C++11
// To run: g++ UsingUniquePtr.cpp -o UsingUniquePtr && ./UsingUniquePtr
#include <iostream>
#include <memory> 
int main() {
    // Create a unique_ptr to an integer
    std::unique_ptr<int> ptr1(new int(10));

    // Access the value using the unique_ptr
    std::cout << "Value: " << *ptr1 << std::endl;

    // Transfer ownership to another unique_ptr
    std::unique_ptr<int> ptr2 = std::move(ptr1);

    // Check if ptr1 is now null
    if (!ptr1) {
        std::cout << "ptr1 is now null after moving ownership to ptr2." << std::endl;
    }
    // Access the value using the new unique_ptr
    std::cout << "Value from ptr2: " << *ptr2 << std::endl;

    return 0;
}