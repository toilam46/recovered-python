// Program to generate a random number between 1 and 100
// Note: 101 is exclusive in the Random.Next method, so it generates numbers from 1 to 100.
using System;

namespace My3rdPro
{
    class RandomNum
    {
        static void Main()
        {
            Random random = new Random();
            int randomNumber = random.Next(1, 101);
            Console.WriteLine("Random number between 1 and 100: " + randomNumber);
        }
    }
}
