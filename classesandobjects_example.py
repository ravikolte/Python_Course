"""
using System;

// Class definition in C#
class Car
{
    // Fields
    public string Model;
    public int Year;

    // Constructor
    public Car(string model, int year)
    {
        Model = model;
        Year = year;
    }

    // Method
    public void DisplayInfo()
    {
        Console.WriteLine($"Car Model: {Model}, Year: {Year}");
    }
}

class Program
{
    static void Main()
    {
        // Creating objects in C#
        Car car1 = new Car("Toyota", 2022);
        Car car2 = new Car("Honda", 2021);

        // Accessing object properties and methods
        car1.DisplayInfo();
        car2.DisplayInfo();
    }
}

# JAVA
// Class definition in Java
class Car {
    // Fields
    public String model;
    public int year;

    // Constructor
    public Car(String model, int year) {
        this.model = model;
        this.year = year;
    }

    // Method
    public void displayInfo() {
        System.out.println("Car Model: " + model + ", Year: " + year);
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating objects in Java
        Car car1 = new Car("Toyota", 2022);
        Car car2 = new Car("Honda", 2021);

        // Accessing object properties and methods
        car1.displayInfo();
        car2.displayInfo();
    }
}


"""
# Class definition in Python
class Car:
    # Constructor
    def __init__(self, model, year):
        self.model = model
        self.year = year

    # Method
    def display_info(self):
        print(f"Car Model: {self.model}, Year: {self.year}")

# Creating objects in Python
car1 = Car("Toyota", 2022)
car2 = Car("Honda", 2021)

# Accessing object properties and methods
car1.display_info()
car2.display_info()
