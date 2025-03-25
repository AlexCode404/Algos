using System;
using System.Numerics;

class RSAKeyFormatter
{
    public static string ToBase64(BigInteger number)
    {
        byte[] bytes = number.ToByteArray();
        return Convert.ToBase64String(bytes);
    }

    public static BigInteger FromBase64(string base64)
    {
        byte[] bytes = Convert.FromBase64String(base64);
        return new BigInteger(bytes);
    }
}
