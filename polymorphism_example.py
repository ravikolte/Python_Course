"""
c#
using System;

// Polymorphism in C#
class Shape
{
    public virtual void Draw()
    {
        Console.WriteLine("Drawing a shape");
    }
}

class Circle : Shape
{
    public override void Draw()
    {
        Console.WriteLine("Drawing a circle");
    }
}

class Square : Shape
{
    public override void Draw()
    {
        Console.WriteLine("Drawing a square");
    }
}

class Program
{
    static void Main()
    {
        // Polymorphism in C#
        Shape shape1 = new Circle();
        Shape shape2 = new Square();

        shape1.Draw();  // Calls the Draw method of Circle
        shape2.Draw();  // Calls the Draw method of Square
    }
}

#JAVA
// Polymorphism in Java
class Shape {
    void draw() {
        System.out.println("Drawing a shape");
    }
}

class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a circle");
    }
}

class Square extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a square");
    }
}

public class Main {
    public static void main(String[] args) {
        // Polymorphism in Java
        Shape shape1 = new Circle();
        Shape shape2 = new Square();

        shape1.draw();  // Calls the draw method of Circle
        shape2.draw();  // Calls the draw method of Square
    }
}

"""
# Polymorphism in Python
class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

# Polymorphism in Python
shape1 = Circle()
shape2 = Square()

shape1.draw()  # Calls the draw method of Circle
shape2.draw()  # Calls the draw method of Square
