// Write a C# program that creates a list of objects, adds some objects to the list, and then iterates through the list to display the properties of each object.
using System;
using System.Collections.Generic;

namespace My2ndPro
{
    class Person
    {
        public string Name { get; set; }
        public int Age { get; set; }

        public Person(string name, int age)
        {
            Name = name;
            Age = age;
        }
    }

    class ListOfObjects
    {
        static void Main()
        {
            // Create a list of Person objects
            List<Person> people = new List<Person>();

            // Add some Person objects to the list
            people.Add(new Person("Alice", 30));
            people.Add(new Person("Bob", 25));
            people.Add(new Person("Charlie", 35));

            // Iterate through the list and display the properties of each object
            foreach (Person person in people)
            {
                Console.WriteLine($"Name: {person.Name}, Age: {person.Age}");
            }
        }
    }
}
