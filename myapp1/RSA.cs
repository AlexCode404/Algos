using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace myapp1
{
    // Класс RSA, использующий MyBigInt для арифметических операций.
    public class RSA
    {
        public MyBigInt n; // модуль
        public MyBigInt e; // публичная экспонента
        public MyBigInt d; // приватная экспонента

        // Конструктор генерации ключей по заданным простым числам p и q и экспоненте e.
        public RSA(MyBigInt p, MyBigInt q, MyBigInt e)
        {
            n = p * q;
            MyBigInt phi = (p - new MyBigInt(1)) * (q - new MyBigInt(1));
            this.e = e;
            d = e.ModInverse(phi);
        }

        // Шифрование сообщения: c = m^e mod n.
        public MyBigInt Encrypt(MyBigInt message)
        {
            return ModExp(message, e, n);
        }

        // Расшифрование: m = c^d mod n.
        public MyBigInt Decrypt(MyBigInt cipher)
        {
            return ModExp(cipher, d, n);
        }

        // Быстрое возведение в степень по модулю.
        public static MyBigInt ModExp(MyBigInt baseValue, MyBigInt exponent, MyBigInt modulus)
        {
            MyBigInt result = new MyBigInt(1);
            baseValue = baseValue % modulus;
            while (exponent > new MyBigInt(0))
            {
                if ((exponent % new MyBigInt(2)) == new MyBigInt(1))
                    result = (result * baseValue) % modulus;
                exponent = exponent / new MyBigInt(2);
                baseValue = (baseValue * baseValue) % modulus;
            }
            return result;
        }

        // Функция шифрования строки. Каждый байт исходной строки шифруется отдельно.
        public string EncryptString(string input)
        {
            byte[] bytes = Encoding.UTF8.GetBytes(input);
            List<string> encryptedParts = new List<string>();
            foreach (byte b in bytes)
            {
                MyBigInt m = new MyBigInt((int)b);
                MyBigInt cipher = Encrypt(m);
                encryptedParts.Add(cipher.ToString());
            }
            return string.Join(" ", encryptedParts);
        }

        // Функция расшифрования строки.
        public string DecryptString(string input)
        {
            string[] parts = input.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
            List<byte> decryptedBytes = new List<byte>();
            foreach (string part in parts)
            {
                MyBigInt cipher = new MyBigInt(int.Parse(part));
                MyBigInt m = Decrypt(cipher);
                int val = int.Parse(m.ToString());
                decryptedBytes.Add((byte)val);
            }
            return Encoding.UTF8.GetString(decryptedBytes.ToArray());
        }

        // Шифрование текстового файла с помощью открытого ключа.
        public void EncryptFile(string inputFile, string outputFile)
        {
            string text = File.ReadAllText(inputFile, Encoding.UTF8);
            string encryptedText = EncryptString(text);
            File.WriteAllText(outputFile, encryptedText, Encoding.UTF8);
        }

        // Расшифрование текстового файла с помощью закрытого ключа.
        public void DecryptFile(string inputFile, string outputFile)
        {
            string encryptedText = File.ReadAllText(inputFile, Encoding.UTF8);
            string decryptedText = DecryptString(encryptedText);
            File.WriteAllText(outputFile, decryptedText, Encoding.UTF8);
        }
    }
}
