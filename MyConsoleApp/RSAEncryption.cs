using System;
using System.Numerics;
using System.IO;
using System.Text;

class RSAEncryption
{
    private static Random random = new Random();

    public static void GenerateRSAKeys()
    {
        BigInteger p = GenerateLargePrime();
        BigInteger q = GenerateLargePrime();
        BigInteger n = p * q;
        BigInteger phi = (p - 1) * (q - 1);
        BigInteger e = 65537;
        BigInteger d = ModInverse(e, phi);

        File.WriteAllText("publicKey.txt", $"{RSAKeyFormatter.ToBase64(e)}\n{RSAKeyFormatter.ToBase64(n)}");
        File.WriteAllText("privateKey.txt", $"{RSAKeyFormatter.ToBase64(d)}\n{RSAKeyFormatter.ToBase64(n)}");

        Console.WriteLine("🔑 RSA ключи сохранены в файлах publicKey.txt и privateKey.txt");
    }

    public static void EncryptFile()
    {
        Console.Write("Введите путь к файлу: ");
        string inputFile = Console.ReadLine();
        Console.Write("Введите путь для сохранения: ");
        string outputFile = Console.ReadLine();

        string text = File.ReadAllText(inputFile);
        string[] key = File.ReadAllLines("publicKey.txt");
        BigInteger e = RSAKeyFormatter.FromBase64(key[0]);
        BigInteger n = RSAKeyFormatter.FromBase64(key[1]);

        byte[] bytes = Encoding.UTF8.GetBytes(text);
        BigInteger message = new BigInteger(bytes);
        BigInteger encrypted = BigInteger.ModPow(message, e, n);

        File.WriteAllText(outputFile, RSAKeyFormatter.ToBase64(encrypted));
        Console.WriteLine("✅ Файл зашифрован.");
    }

    public static void DecryptFile()
    {
        Console.Write("Введите путь к зашифрованному файлу: ");
        string inputFile = Console.ReadLine();
        Console.Write("Введите путь для сохранения: ");
        string outputFile = Console.ReadLine();

        string[] key = File.ReadAllLines("privateKey.txt");
        BigInteger d = RSAKeyFormatter.FromBase64(key[0]);
        BigInteger n = RSAKeyFormatter.FromBase64(key[1]);

        BigInteger encrypted = RSAKeyFormatter.FromBase64(File.ReadAllText(inputFile));
        BigInteger decrypted = BigInteger.ModPow(encrypted, d, n);

        byte[] bytes = decrypted.ToByteArray();
        string text = Encoding.UTF8.GetString(bytes);

        File.WriteAllText(outputFile, text);
        Console.WriteLine("✅ Файл расшифрован.");
    }

    private static BigInteger GenerateLargePrime()
    {
        while (true)
        {
            BigInteger num = GenerateRandomBigInt(512);
            if (IsPrime(num))
                return num;
        }
    }

    private static BigInteger GenerateRandomBigInt(int bits)
    {
        byte[] data = new byte[bits / 8];
        random.NextBytes(data);
        return new BigInteger(data) | 1; // Делаем нечетным
    }

    private static bool IsPrime(BigInteger n, int k = 10)
    {
        if (n < 2) return false;
        if (n % 2 == 0) return n == 2;
        for (int i = 0; i < k; i++)
        {
            BigInteger a = GenerateRandomBigInt(512) % (n - 1) + 1;
            if (BigInteger.ModPow(a, n - 1, n) != 1)
                return false;
        }
        return true;
    }

    private static BigInteger ModInverse(BigInteger a, BigInteger m)
    {
        BigInteger m0 = m, t, q;
        BigInteger x0 = 0, x1 = 1;

        if (m == 1) return 0;

        while (a > 1)
        {
            q = a / m;
            t = m;
            m = a % m;
            a = t;
            t = x0;
            x0 = x1 - q * x0;
            x1 = t;
        }
        return x1 < 0 ? x1 + m0 : x1;
    }
}
