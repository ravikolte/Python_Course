"""
using System;

// Base class
class Vehicle
{
    public string Model { get; set; }
    public int Year { get; set; }

    public void DisplayInfo()
    {
        Console.WriteLine($"Model: {Model}, Year: {Year}");
    }
}

// Derived class (inherits from Vehicle)
class Car : Vehicle
{
    public void Start()
    {
        Console.WriteLine("Car started");
    }
}

class Program
{
    static void Main()
    {
        // Creating and using objects with inheritance in C#
        Car car = new Car
        {
            Model = "Toyota",
            Year = 2022
        };

        car.DisplayInfo();  // Accessing base class method
        car.Start();        // Accessing derived class method
    }
}

#JAVA
// Base class
class Vehicle {
    String model;
    int year;

    void displayInfo() {
        System.out.println("Model: " + model + ", Year: " + year);
    }
}

// Derived class (inherits from Vehicle)
class Car extends Vehicle {
    void start() {
        System.out.println("Car started");
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating and using objects with inheritance in Java
        Car car = new Car();
        car.model = "Toyota";
        car.year = 2022;

        car.displayInfo();  // Accessing base class method
        car.start();        // Accessing derived class method
    }
}

"""
# Base class
class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Model: {self.model}, Year: {self.year}")

# Derived class (inherits from Vehicle)
class Car(Vehicle):
    def start(self):
        print("Car started")

# Creating and using objects with inheritance in Python
car = Car("Toyota", 2022)
car.display_info()  # Accessing base class method
car.start()         # Accessing derived class method
