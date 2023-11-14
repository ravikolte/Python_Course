"""
C#

using System;

class Program
{
    delegate int MyDelegate(int x, int y);

    static void Main()
    {
        // Lambda function in C#
        MyDelegate add = (x, y) => x + y;
        MyDelegate multiply = (x, y) => x * y;

        // Using lambda functions
        Console.WriteLine("Addition: " + add(5, 3));
        Console.WriteLine("Multiplication: " + multiply(5, 3));
    }
}

# JAVA

public class Main {
    interface MyInterface {
        int myMethod(int x, int y);
    }

    public static void main(String[] args) {
        // Lambda function in Java
        MyInterface add = (x, y) -> x + y;
        MyInterface multiply = (x, y) -> x * y;

        // Using lambda functions
        System.out.println("Addition: " + add.myMethod(5, 3));
        System.out.println("Multiplication: " + multiply.myMethod(5, 3));
    }
}



"""

# Lambda function in Python
add = lambda x, y: x + y
multiply = lambda x, y: x * y

# Using lambda functions
print("Addition:", add(5, 3))
print("Multiplication:", multiply(5, 3))
