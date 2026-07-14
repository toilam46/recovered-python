// Program to demonstrate the use of std::unique_ptr in C++17.  The unique_ptr class encapsulates the calls to new and delete. When a widget object goes out of scope, the unique_ptr destructor will be invoked and it releases the memory that was allocated for the array.
// To run: g++ UsingUniquePtrClass.cpp -o UsingUniquePtrClass && ./UsingUniquePtrClass
#include <iostream>
#include <memory> 
class Widget {
public:
    Widget(int value) : value_(value) {
        std::cout << "Widget constructed with value: " << value_ << std::endl;
    }
    ~Widget() {
        std::cout << "Widget destructed with value: " << value_ << std::endl;
    }
    void display() const {
        std::cout << "Widget value: " << value_ << std::endl;
    }
private:
    int value_;
};
int main() {
    // Create a unique_ptr to a Widget object
    std::unique_ptr<Widget> widgetPtr(new Widget(42));    
    widgetPtr->display();
    return 0;
} 