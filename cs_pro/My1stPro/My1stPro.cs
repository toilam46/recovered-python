// Given string cars, use foreach loop to print all the elements of the array.
// cd Py_CC++_C#/cs_pro/MyFirstProgram, then in (venv) terminal, run "dotnet run" to execute the program.
// Note the standard for loop in C# is "foreach" instead of "for" as in Python. Although C# also has a "for" loop, it is more commonly used for iterating over a range of numbers, while "foreach" is preferred for iterating over collections like arrays.
using System;   

class MyFirstProgram
{
    static void Main()
    {
        string[] cars = {"Ford", "BMW", "Fiat"};
        foreach (string i in cars)
        {
            Console.WriteLine(i);
        }
        Console.WriteLine("\nAlternatively, you can also use a standard for loop to achieve the same result:");
        for (int j = 0; j < cars.Length; j++)
        {
            Console.WriteLine(cars[j]);
        }

        // Run MethodOverloading example.
        Console.WriteLine("\nRun MethodOverloading example:");
        var mo = new MethodOverloading();
        mo.Print("Hello, Method Overloading!");
        mo.Print(123);
        mo.Print(3.14);  

        // Write a test of Equals method to compare two strings.
        string str1 = "Hello, World!";
        string str2 = "Hello, World!";
        Console.WriteLine($"Comparing str1 and str2 using Equals method: {str1.Equals(str2)}");  // This should return true since str1 and str2 have the same content.
    }
}

