"""
====================================================================================================================
In Python, collections are built-in data structures used to store and organize data. Some of the commonly used
collection types in Python are:

Lists:

Lists are ordered, mutable sequences.

Elements can be of different types.

Example in Python:

python

my_list = [1, 2, 3, 'a', 'b', 'c']
Similar in C# (using List<T>):

csharp

List<object> myList = new List<object> { 1, 2, 3, "a", "b", "c" };
Similar in Java (using ArrayList):

java

List<Object> myList = new ArrayList<>(Arrays.asList(1, 2, 3, "a", "b", "c"));
Tuples:

Tuples are ordered, immutable sequences.

Elements can be of different types.

Example in Python:

python

my_tuple = (1, 2, 'a', 'b')
Similar in C# (using Tuple):

csharp

var myTuple = Tuple.Create(1, 2, "a", "b");
Similar in Java (using a custom class or Pair from Apache Commons Lang):

java

Pair<Integer, Pair<Integer, Pair<String, String>>> myTuple = Pair.of(1, Pair.of(2, Pair.of("a", "b")));
Sets:

Sets are unordered collections of unique elements.

Example in Python:

python

my_set = {1, 2, 3, 3, 3}  # Only contains unique elements
Similar in C# (using HashSet<T>):

csharp

HashSet<int> mySet = new HashSet<int> { 1, 2, 3 };
Similar in Java (using HashSet):

java

Set<Integer> mySet = new HashSet<>(Arrays.asList(1, 2, 3));
Dictionaries (or Maps):

Dictionaries are collections of key-value pairs.

Example in Python:

python

my_dict = {'one': 1, 'two': 2, 'three': 3}
Similar in C# (using Dictionary<TKey, TValue>):

csharp

Dictionary<string, int> myDict = new Dictionary<string, int> { { "one", 1 }, { "two", 2 }, { "three", 3 } };
Similar in Java (using HashMap):

java

Map<String, Integer> myMap = new HashMap<>();
myMap.put("one", 1);
myMap.put("two", 2);
myMap.put("three", 3);
These are just a few examples of common collection types in Python, C#, and Java. Each language may have additional
 collection types and variations, but these cover the basics. Understanding the similarities and differences in
 how these collections are used can help when working across different languages.
================================================================================================================================
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Collections in C#
        // List
        List<int> myList = new List<int> { 1, 2, 3, 4, 5 };

        // Dictionary
        Dictionary<string, int> myDictionary = new Dictionary<string, int>
        {
            { "One", 1 },
            { "Two", 2 },
            { "Three", 3 }
        };

        // Array
        int[] myArray = { 10, 20, 30, 40, 50 };

        Console.WriteLine("List:");
        foreach (int item in myList)
        {
            Console.Write(item + " ");
        }

        Console.WriteLine("\nDictionary:");
        foreach (var kvp in myDictionary)
        {
            Console.WriteLine($"{kvp.Key}: {kvp.Value}");
        }

        Console.WriteLine("Array:");
        foreach (int item in myArray)
        {
            Console.Write(item + " ");
        }
    }
}
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        // Collections in Java
        // ArrayList
        ArrayList<Integer> myList = new ArrayList<>();
        myList.add(1);
        myList.add(2);
        myList.add(3);
        myList.add(4);
        myList.add(5);

        // HashMap
        Map<String, Integer> myMap = new HashMap<>();
        myMap.put("One", 1);
        myMap.put("Two", 2);
        myMap.put("Three", 3);

        // Array
        int[] myArray = { 10, 20, 30, 40, 50 };

        System.out.println("ArrayList:");
        for (int item : myList) {
            System.out.print(item + " ");
        }

        System.out.println("\nHashMap:");
        for (Map.Entry<String, Integer> entry : myMap.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }

        System.out.println("Array:");
        for (int item : myArray) {
            System.out.print(item + " ");
        }
    }
}

"""
# Collections in Python
# List
my_list = [1, 2, 3, 4, 5]

# Dictionary
my_dict = {
    "One": 1,
    "Two": 2,
    "Three": 3
}

my_set = {1,2,3}
# Tuple
my_tuple = (10, 20, 30, 40, 50)

print("List:")
for item in my_list:
    print(item, end=" ")

print("\nDictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print("Set:")
for item in my_set:
    print(item, end=" ")

print("\nTuple:")
for item in my_tuple:
    print(item, end=" ")
