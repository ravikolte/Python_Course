"""
using System;

class Program
{
    static void Main()
    {
        // Loops in C#

        // For loop
        Console.WriteLine("For Loop:");
        for (int i = 1; i <= 5; i++)
        {
            Console.Write(i + " ");
        }

        // While loop
        Console.WriteLine("\n\nWhile Loop:");
        int j = 1;
        while (j <= 5)
        {
            Console.Write(j + " ");
            j++;
        }

        // Do-While loop
        Console.WriteLine("\n\nDo-While Loop:");
        int k = 1;
        do
        {
            Console.Write(k + " ");
            k++;
        } while (k <= 5);
    }
}


public class Main {
    public static void main(String[] args) {
        // Loops in Java

        // For loop
        System.out.println("For Loop:");
        for (int i = 1; i <= 5; i++) {
            System.out.print(i + " ");
        }

        // While loop
        System.out.println("\n\nWhile Loop:");
        int j = 1;
        while (j <= 5) {
            System.out.print(j + " ");
            j++;
        }

        // Do-While loop
        System.out.println("\n\nDo-While Loop:");
        int k = 1;
        do {
            System.out.print(k + " ");
            k++;
        } while (k <= 5);
    }
}


"""
# Loops in Python

# For loop
print("For Loop:")
for i in range(1, 6):
    print(i, end=" ")

# While loop
print("\n\nWhile Loop:")
j = 1
while j <= 5:
    print(j, end=" ")
    j += 1

# Do-While loop (Equivalent using while loop in Python)
print("\n\nDo-While Loop (Equivalent using while loop in Python):")
k = 1
while k <= 5:
    print(k, end=" ")
    k += 1

