"""
C#

// File: MyMath.cs
using System;

namespace MyMath
{
    public class Calculator
    {
        public static int Add(int a, int b)
        {
            return a + b;
        }

        public static int Subtract(int a, int b)
        {
            return a - b;
        }
    }
}

// File: Program.cs
using System;

class Program
{
    static void Main()
    {
        int resultAdd = MyMath.Calculator.Add(5, 3);
        int resultSubtract = MyMath.Calculator.Subtract(8, 2);

        Console.WriteLine("Addition Result: " + resultAdd);
        Console.WriteLine("Subtraction Result: " + resultSubtract);
    }
}

# JAVA

// File: MyMath.java
package mymath;

public class Calculator {
    public static int add(int a, int b) {
        return a + b;
    }

    public static int subtract(int a, int b) {
        return a - b;
    }
}

// File: Program.java
public class Program {
    public static void main(String[] args) {
        int resultAdd = mymath.Calculator.add(5, 3);
        int resultSubtract = mymath.Calculator.subtract(8, 2);

        System.out.println("Addition Result: " + resultAdd);
        System.out.println("Subtraction Result: " + resultSubtract);
    }
}

"""
# File: mymath.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# File: program.py
import mymath

result_add = mymath.add(5, 3)
result_subtract = mymath.subtract(8, 2)

print("Addition Result:", result_add)
print("Subtraction Result:", result_subtract)

""" In this example, mymath is a Python module, and add and subtract are functions defined within that module."""