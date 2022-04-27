using System;

namespace _3
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter Your Name:");
            string Name=Console.ReadLine();
            Console.WriteLine("Now Enter Your Age:");
            int age=Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Your name is "+Name +" and your age is "+age);
        }
    }
}
