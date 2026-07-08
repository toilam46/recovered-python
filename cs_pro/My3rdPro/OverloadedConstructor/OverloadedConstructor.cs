// Write a C# program that with overloaded constructors to create a pizza object with different crust sauce toppings and cheese
// Demonstrade of using getters and setters to access the properties of the pizza object

using System;

namespace My3rdPro
{
    class Pizza
    {
        // Auto-implemented properties (each has an implicit getter and setter)
        public string Crust { get; set; }     // getter and setter
        public string Sauce { get; set; }     // getter and setter
        public string Toppings { get; set; }  // getter and setter
        public string Cheese { get; set; }    // getter and setter

        // Overloaded constructor 1
        public Pizza(string crust, string sauce)
        {
            // setters: assign values to the properties
            Crust = crust;     // sets `Crust`
            Sauce = sauce;     // sets `Sauce`
            Toppings = "None"; // sets `Toppings`
            Cheese = "None";   // sets `Cheese`
        }

        // Overloaded constructor 2
        public Pizza(string crust, string sauce, string toppings)
        {
            // setters used here
            Crust = crust;
            Sauce = sauce;
            Toppings = toppings;
            Cheese = "None";
        }

        // Overloaded constructor 3
        public Pizza(string crust, string sauce, string toppings, string cheese)
        {
            // setters used here
            Crust = crust;
            Sauce = sauce;
            Toppings = toppings;
            Cheese = cheese;
        }

        public void DisplayPizza()
        {
            // getters: read property values for output
            Console.WriteLine($"Crust: {Crust}, Sauce: {Sauce}, Toppings: {Toppings}, Cheese: {Cheese}");
        }
    }

    class OverloadedConstructor
    {
        static void Main()
        {
            // creating pizzas (constructors invoke setters to initialize properties)
            Pizza pizza1 = new Pizza("Thin", "Tomato");
            Pizza pizza2 = new Pizza("Thick", "Barbecue", "Pepperoni");
            Pizza pizza3 = new Pizza("Stuffed", "Alfredo", "Mushrooms", "Mozzarella");

            pizza1.DisplayPizza();
            pizza2.DisplayPizza();
            pizza3.DisplayPizza();
        }
    }
}
