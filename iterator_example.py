"""
using System;
using System.Collections;

class Program
{
    static void Main()
    {
        // Iterator in C#
        MyCollection myCollection = new MyCollection();

        foreach (int number in myCollection)
        {
            Console.WriteLine(number);
        }
    }
}

// Custom collection implementing IEnumerable
class MyCollection : IEnumerable
{
    private int[] numbers = { 1, 2, 3, 4, 5 };

    public IEnumerator GetEnumerator()
    {
        return new MyEnumerator(numbers);
    }
}

// Custom enumerator implementing IEnumerator
class MyEnumerator : IEnumerator
{
    private int[] numbers;
    private int position = -1;

    public MyEnumerator(int[] numbers)
    {
        this.numbers = numbers;
    }

    public object Current
    {
        get
        {
            return numbers[position];
        }
    }

    public bool MoveNext()
    {
        position++;
        return position < numbers.Length;
    }

    public void Reset()
    {
        position = -1;
    }
}

#JAVA
import java.util.Iterator;

public class Main {
    public static void main(String[] args) {
        // Iterator in Java
        MyCollection myCollection = new MyCollection();

        Iterator<Integer> iterator = myCollection.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }
}

// Custom collection implementing Iterable
class MyCollection implements Iterable<Integer> {
    private int[] numbers = {1, 2, 3, 4, 5};

    @Override
    public Iterator<Integer> iterator() {
        return new MyIterator(numbers);
    }
}

// Custom iterator implementing Iterator
class MyIterator implements Iterator<Integer> {
    private int[] numbers;
    private int position = -1;

    public MyIterator(int[] numbers) {
        this.numbers = numbers;
    }

    @Override
    public boolean hasNext() {
        return position < numbers.length - 1;
    }

    @Override
    public Integer next() {
        if (hasNext()) {
            position++;
            return numbers[position];
        } else {
            throw new UnsupportedOperationException("No more elements");
        }
    }
}


"""
# Iterator in Python
class MyCollection:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]

    def __iter__(self):
        return MyIterator(self.numbers)

class MyIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.position = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.position += 1
        if self.position < len(self.numbers):
            return self.numbers[self.position]
        else:
            raise StopIteration()

# Using the iterator
my_collection = MyCollection()

for number in my_collection:
    print(number)
