using System;
using System.Numerics;

class BigIntCalculator
{
    public static void PerformOperation(string operation)
    {
        Console.Write("Введите первое число: ");
        BigInteger a = BigInteger.Parse(Console.ReadLine());
        Console.Write("Введите второе число: ");
        BigInteger b = BigInteger.Parse(Console.ReadLine());

        BigInteger result = operation switch
        {
            "add" => a + b,
            "sub" => a - b,
            "mul" => a * b,
            "div" => a / b,
            "mod" => a % b,
            _ => throw new InvalidOperationException()
        };

        Console.WriteLine($"Результат: {result}");
    }

    public static void CompareNumbers()
    {
        Console.Write("Введите первое число: ");
        BigInteger a = BigInteger.Parse(Console.ReadLine());
        Console.Write("Введите второе число: ");
        BigInteger b = BigInteger.Parse(Console.ReadLine());

        string result = a == b ? "==" : a < b ? "<" : ">";
        Console.WriteLine($"Сравнение: {a} {result} {b}");
    }
}
