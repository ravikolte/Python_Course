"""
C#
using System;

class Program
{
    // Global variable (accessible throughout the program)
    static int globalVariable = 10;

    static void Main()
    {
        // Local variable (accessible only within Main method)
        int localVariable = 5;

        Console.WriteLine($"Global Variable: {globalVariable}");
        Console.WriteLine($"Local Variable: {localVariable}");

        // Accessing a method with its own local variable
        AccessMethod();
    }

    static void AccessMethod()
    {
        // Another local variable (accessible only within AccessMethod)
        int anotherLocalVariable = 20;

        // Accessing global and local variables
        Console.WriteLine($"Global Variable from AccessMethod: {globalVariable}");
        // Console.WriteLine($"Local Variable from AccessMethod: {localVariable}"); // Error, localVariable is not accessible here
        Console.WriteLine($"Another Local Variable: {anotherLocalVariable}");
    }
}

#JAVA
public class Main {
    // Global variable (accessible throughout the program)
    static int globalVariable = 10;

    public static void main(String[] args) {
        // Local variable (accessible only within the main method)
        int localVariable = 5;

        System.out.println("Global Variable: " + globalVariable);
        System.out.println("Local Variable: " + localVariable);

        // Accessing a method with its own local variable
        accessMethod();
    }

    static void accessMethod() {
        // Another local variable (accessible only within accessMethod)
        int anotherLocalVariable = 20;

        // Accessing global and local variables
        System.out.println("Global Variable from accessMethod: " + globalVariable);
        // System.out.println("Local Variable from accessMethod: " + localVariable); // Error, localVariable is not accessible here
        System.out.println("Another Local Variable: " + anotherLocalVariable);
    }
}

"""
# Global variable (accessible throughout the program)
global_variable = 10

def main():
    # Local variable (accessible only within the main function)
    local_variable = 5

    print("Global Variable:", global_variable)
    print("Local Variable:", local_variable)

    # Accessing a function with its own local variable
    access_function()

def access_function():
    # Another local variable (accessible only within access_function)
    another_local_variable = 20

    # Accessing global and local variables
    print("Global Variable from access_function:", global_variable)
    # print("Local Variable from access_function:", local_variable)  # Error, local_variable is not accessible here
    print("Another Local Variable:", another_local_variable)

# Call the main function
main()
