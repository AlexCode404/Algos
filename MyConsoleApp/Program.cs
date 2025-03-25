using System;
using System.Numerics;
using System.IO;

class Program
{
    static void Main()
    {
        Console.WriteLine("Введите команду (add, sub, mul, div, mod, cmp, rsa-gen, rsa-enc, rsa-dec, exit):");
        while (true)
        {
            Console.Write("Команда: ");
            string command = Console.ReadLine()?.Trim().ToLower();

            switch (command)
            {
                case "add":
                case "sub":
                case "mul":
                case "div":
                case "mod":
                    BigIntCalculator.PerformOperation(command);
                    break;
                case "cmp":
                    BigIntCalculator.CompareNumbers();
                    break;
                case "rsa-gen":
                    RSAEncryption.GenerateRSAKeys();
                    break;
                case "rsa-enc":
                    RSAEncryption.EncryptFile();
                    break;
                case "rsa-dec":
                    RSAEncryption.DecryptFile();
                    break;
                case "exit":
                    return;
                default:
                    Console.WriteLine("Неизвестная команда.");
                    break;
            }
        }
    }
}
