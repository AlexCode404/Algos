using System;
using System.IO;
using System.Text;

namespace myapp1
{
    class Program
    {
        static void Main(string[] args)
        {
            // Для демонстрации используются небольшие простые числа (неподходящие для реальной безопасности)
            MyBigInt p = new MyBigInt(499);
            MyBigInt q = new MyBigInt(547);
            MyBigInt e = new MyBigInt(65537);
            RSA rsa = new RSA(p, q, e);

            // Вывод публичного ключа в консоль в формате (n,e)
            Console.WriteLine("Публичный ключ: (e, n) = (" + rsa.e + ", " + rsa.n + ")\n");
            Console.WriteLine("Приватный ключ: (d, n) = (" + rsa.d + ", " + rsa.n + ")\n");

            // Бесконечное интерактивное меню
            while (true)
            {
                Console.WriteLine("1. Шифрование файла");
                Console.WriteLine("2. Расшифрование файла");
                Console.Write("Введите номер режима: ");
                string choice = Console.ReadLine();

                if (choice == "1")
                {
                    // Режим шифрования файла
                    Console.Write("Введите путь к входному файлу: ");
                    string inputFileEnc = Console.ReadLine();
                    Console.Write("Введите путь для сохранения зашифрованного файла: ");
                    string outputFileEnc = Console.ReadLine();

                    try
                    {
                        rsa.EncryptFile(inputFileEnc, outputFileEnc);
                        Console.WriteLine("Файл успешно зашифрован.\n");
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("Ошибка при шифровании файла: " + ex.Message + "\n");
                    }
                }
                else if (choice == "2")
                {
                    // Режим расшифрования файла
                    Console.Write("Введите путь к зашифрованному файлу: ");
                    string inputFileDec = Console.ReadLine();
                    Console.Write("Введите путь для сохранения расшифрованного файла: ");
                    string outputFileDec = Console.ReadLine();

                    try
                    {
                        rsa.DecryptFile(inputFileDec, outputFileDec);
                        Console.WriteLine("Файл успешно расшифрован.\n");
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("Ошибка при расшифровании файла: " + ex.Message + "\n");
                    }
                }
                else if (choice == "3" || choice.ToLower() == "exit")
                {
                    // Завершение работы программы
                    Console.WriteLine("Завершение работы программы.");
                    break;
                }
                else
                {
                    Console.WriteLine("Неверный выбор. Пожалуйста, попробуйте еще раз.\n");
                }
            }
        }
    }
}
