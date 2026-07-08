public class MethodOverloading
{
    // Method overloading allows you to have multiple methods with the same name but different parameters.
    // This is useful for creating methods that perform similar tasks but with different types or numbers of parameters.

    // Example of method overloading:
    public void Print(string message)
    {
        Console.WriteLine("String: " + message);
    }

    public void Print(int number)
    {
        Console.WriteLine("Integer: " + number);
    }

    public void Print(double number)
    {
        Console.WriteLine("Double: " + number);
    }
}