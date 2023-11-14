"""
C#
using System;

class Program
{
    static void Main()
    {
        try
        {
            // Code that may throw an exception
            int result = Divide(10, 0);
            Console.WriteLine("Result: " + result);
        }
        catch (DivideByZeroException ex)
        {
            Console.WriteLine("Error: " + ex.Message);
        }
        catch (Exception ex)
        {
            Console.WriteLine("An unexpected error occurred: " + ex.Message);
        }
    }

    static int Divide(int a, int b)
    {
        // Method that may throw an exception
        return a / b;
    }
}

#JAVA

public class Main {
    public static void main(String[] args) {
        try {
            // Code that may throw an exception
            int result = divide(10, 0);
            System.out.println("Result: " + result);
        } catch (ArithmeticException ex) {
            System.out.println("Error: " + ex.getMessage());
        } catch (Exception ex) {
            System.out.println("An unexpected error occurred: " + ex.getMessage());
        }
    }

    static int divide(int a, int b) {
        // Method that may throw an exception
        return a / b;
    }
}

"""

def main():
    try:
        # Code that may throw an exception
        result = divide(10, 0)
        print("Result:", result)
    except ZeroDivisionError as ex:
        print("Error:", str(ex))
    except Exception as ex:
        print("An unexpected error occurred:", str(ex))

def divide(a, b):
    # Function that may throw an exception
    return a / b

# Call the main function
main()
