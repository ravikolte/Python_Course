""" C# code with a simple function
using System;

class Program
{
    static void Main()
    {
        int result = AddNumbers(5, 10);
        Console.WriteLine("Sum: " + result);
    }

    static int AddNumbers(int a, int b)
    {
        return a + b;
    }
}

// Java code with a simple function
public class Main {
    public static void main(String[] args) {
        int result = addNumbers(5, 10);
        System.out.println("Sum: " + result);
    }

    static int addNumbers(int a, int b) {
        return a + b;
    }
}

"""


# Python code with a simple function
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 10)
print("Sum:", result)
