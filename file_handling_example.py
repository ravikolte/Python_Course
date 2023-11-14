"""
C#

using System;
using System.IO;

class Program
{
    static void Main()
    {
        // Writing to a file
        string filePath = "example.txt";
        WriteToFile(filePath, "Hello, C#!");

        // Reading from a file
        string content = ReadFromFile(filePath);
        Console.WriteLine("File Content: " + content);
    }

    static void WriteToFile(string filePath, string content)
    {
        using (StreamWriter writer = new StreamWriter(filePath))
        {
            writer.WriteLine(content);
        }
    }

    static string ReadFromFile(string filePath)
    {
        using (StreamReader reader = new StreamReader(filePath))
        {
            return reader.ReadToEnd();
        }
    }
}

#JAVA

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        // Writing to a file
        String filePath = "example.txt";
        writeToFile(filePath, "Hello, Java!");

        // Reading from a file
        String content = readFromFile(filePath);
        System.out.println("File Content: " + content);
    }

    static void writeToFile(String filePath, String content) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write(content);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static String readFromFile(String filePath) {
        StringBuilder content = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                content.append(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return content.toString();
    }
}

"""

# Writing to a file
file_path = "example.txt"
with open(file_path, "w") as writer:
    writer.write("Hello, Python!")

# Reading from a file
with open(file_path, "r") as reader:
    content = reader.read()
    print("File Content:", content)
