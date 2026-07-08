// Using switches to write a program to check the days in the week
using System;

namespace My3rdPro
{
    class Switches
    {
        static void Main()
        {
            Console.Write("Enter a day of the week: ");
            string? day = Console.ReadLine();
            if (string.IsNullOrWhiteSpace(day))
            {
                Console.WriteLine("Invalid day entered.");
                return;
            }

            switch (day.ToLower())
            {
                case "monday":
                    Console.WriteLine("It's Monday!");
                    break;
                case "tuesday":
                    Console.WriteLine("It's Tuesday!");
                    break;
                case "wednesday":
                    Console.WriteLine("It's Wednesday!");
                    break;
                case "thursday":
                    Console.WriteLine("It's Thursday!");
                    break;
                case "friday":
                    Console.WriteLine("It's Friday!");
                    break;
                case "saturday":
                    Console.WriteLine("It's Saturday!");
                    break;
                case "sunday":
                    Console.WriteLine("It's Sunday!");
                    break;
                default:
                    Console.WriteLine("Invalid day entered.");
                    break;
            }
        }
    }
}
