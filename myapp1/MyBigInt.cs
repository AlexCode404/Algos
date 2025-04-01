using System;
using System.Collections.Generic;
using System.Text;

namespace myapp1
{
    // Класс для целочисленной арифметики произвольной точности.
    public class MyBigInt : IComparable<MyBigInt>
    {
        // Храним абсолютное значение числа в виде списка байтов (младшие разряды впереди)
        private List<byte> digits;
        // Знак: 1 для положительных, -1 для отрицательных, 0 для нуля.
        private int sign;

        // Конструктор из int
        public MyBigInt(int value)
        {
            if (value == 0)
            {
                sign = 0;
                digits = new List<byte> { 0 };
            }
            else
            {
                sign = value < 0 ? -1 : 1;
                int absVal = Math.Abs(value);
                digits = new List<byte>();
                while (absVal > 0)
                {
                    digits.Add((byte)(absVal & 0xFF));
                    absVal >>= 8;
                }
            }
        }

        // Приватный конструктор, позволяющий задать список цифр и знак
        internal MyBigInt(List<byte> digits, int sign)
        {
            this.digits = new List<byte>(digits);
            this.sign = (IsZero(this.digits)) ? 0 : sign;
            Normalize();
        }

        // Удаление лишних старших нулей
        private void Normalize()
        {
            for (int i = digits.Count - 1; i > 0; i--)
            {
                if (digits[i] == 0)
                    digits.RemoveAt(i);
                else
                    break;
            }
            if (digits.Count == 1 && digits[0] == 0)
                sign = 0;
        }

        private bool IsZero(List<byte> d)
        {
            return d.Count == 1 && d[0] == 0;
        }

        // Преобразование числа в строку (десятичное представление)
        public override string ToString()
        {
            if (this.sign == 0) return "0";
            MyBigInt temp = new MyBigInt(new List<byte>(this.digits), 1);
            StringBuilder sb = new StringBuilder();
            while (temp > new MyBigInt(0))
            {
                MyBigInt remainder;
                temp = DivRem(temp, new MyBigInt(10), out remainder);
                // remainder – число от 0 до 9, берем первый байт
                sb.Insert(0, remainder.digits[0].ToString());
            }
            if (this.sign < 0)
                sb.Insert(0, "-");
            return sb.ToString();
        }

        // Перегрузка оператора сложения
        public static MyBigInt operator +(MyBigInt a, MyBigInt b)
        {
            if(a.sign == 0) return b;
            if(b.sign == 0) return a;
            if(a.sign == b.sign)
            {
                List<byte> result = AddAbsolute(a.digits, b.digits);
                return new MyBigInt(result, a.sign);
            }
            else
            {
                // a + (-b) = a - b, и наоборот
                int cmp = CompareAbsolute(a.digits, b.digits);
                if (cmp >= 0)
                {
                    List<byte> result = SubtractAbsolute(a.digits, b.digits);
                    return new MyBigInt(result, a.sign);
                }
                else
                {
                    List<byte> result = SubtractAbsolute(b.digits, a.digits);
                    return new MyBigInt(result, b.sign);
                }
            }
        }

        // Перегрузка оператора вычитания
        public static MyBigInt operator -(MyBigInt a, MyBigInt b)
        {
            return a + (-b);
        }

        // Унарный минус
        public static MyBigInt operator -(MyBigInt a)
        {
            return new MyBigInt(new List<byte>(a.digits), -a.sign);
        }

        // Перегрузка оператора умножения
        public static MyBigInt operator *(MyBigInt a, MyBigInt b)
        {
            if (a.sign == 0 || b.sign == 0)
                return new MyBigInt(0);
            List<byte> result = MultiplyAbsolute(a.digits, b.digits);
            return new MyBigInt(result, a.sign * b.sign);
        }

        // Перегрузка операторов деления и остатка (реализована на основе длинного деления для неотрицательных чисел)
        public static MyBigInt operator /(MyBigInt a, MyBigInt b)
        {
            MyBigInt r;
            MyBigInt q = DivRem(a, b, out r);
            return q;
        }

        public static MyBigInt operator %(MyBigInt a, MyBigInt b)
        {
            MyBigInt r;
            DivRem(a, b, out r);
            return r;
        }


        // Длинное деление: возвращает частное, остаток через out-параметр.
        // Для простоты алгоритм работает с положительными числами.
        public static MyBigInt DivRem(MyBigInt dividend, MyBigInt divisor, out MyBigInt remainder)
        {
            if(divisor == new MyBigInt(0))
                throw new DivideByZeroException();
            int resultSign = dividend.sign * divisor.sign;
            MyBigInt absDividend = new MyBigInt(dividend.digits, dividend.sign < 0 ? -1 : 1);
            MyBigInt absDivisor = new MyBigInt(divisor.digits, divisor.sign < 0 ? -1 : 1);

            if (absDividend < absDivisor)
            {
                remainder = absDividend;
                return new MyBigInt(0);
            }
            MyBigInt quotient = new MyBigInt(0);
            MyBigInt current = new MyBigInt(0);
            // Переводим цифры делимого в big-endian порядок
            List<byte> dividendBytes = new List<byte>(absDividend.digits);
            dividendBytes.Reverse();
            foreach (byte b in dividendBytes)
            {
                current = current * new MyBigInt(256) + new MyBigInt(b);
                int x = 0;
                while (current >= absDivisor)
                {
                    current = current - absDivisor;
                    x++;
                }
                quotient = quotient * new MyBigInt(256) + new MyBigInt(x);
            }
            quotient = new MyBigInt(quotient.digits, resultSign);
            remainder = current;
            return quotient;
        }

        // Перегрузка операторов сравнения
        public static bool operator ==(MyBigInt a, MyBigInt b)
        {
            return a.CompareTo(b) == 0;
        }

        public static bool operator !=(MyBigInt a, MyBigInt b)
        {
            return a.CompareTo(b) != 0;
        }

        public static bool operator <(MyBigInt a, MyBigInt b)
        {
            return a.CompareTo(b) < 0;
        }

        public static bool operator >(MyBigInt a, MyBigInt b)
        {
            return a.CompareTo(b) > 0;
        }

        public static bool operator <=(MyBigInt a, MyBigInt b)
        {
            return a.CompareTo(b) <= 0;
        }

        public static bool operator >=(MyBigInt a, MyBigInt b)
        {
            return a.CompareTo(b) >= 0;
        }

        public int CompareTo(MyBigInt other)
        {
            if (this.sign != other.sign)
                return this.sign.CompareTo(other.sign);
            if (this.sign == 0) return 0;
            int cmp = CompareAbsolute(this.digits, other.digits);
            return this.sign > 0 ? cmp : -cmp;
        }

        public override bool Equals(object obj)
        {
            if (obj is MyBigInt)
                return this == (MyBigInt)obj;
            return false;
        }

        public override int GetHashCode()
        {
            int hash = sign;
            foreach (byte b in digits)
                hash = hash * 31 + b;
            return hash;
        }

        // Метод для вычисления обратного по модулю (расширенный алгоритм Евклида)
        public MyBigInt ModInverse(MyBigInt modulus)
        {
            MyBigInt a = this % modulus;
            MyBigInt m = modulus;
            MyBigInt x0 = new MyBigInt(0), x1 = new MyBigInt(1);
            if (modulus == new MyBigInt(1))
                return new MyBigInt(0);
            while (a > new MyBigInt(1))
            {
                MyBigInt q = a / m;
                MyBigInt t = m;
                m = a % m;
                a = t;
                t = x0;
                x0 = x1 - q * x0;
                x1 = t;
            }
            if (x1 < new MyBigInt(0))
                x1 = x1 + modulus;
            return x1;
        }

        // Вспомогательные методы для работы с абсолютными значениями.

        private static List<byte> AddAbsolute(List<byte> a, List<byte> b)
        {
            List<byte> result = new List<byte>();
            int carry = 0;
            int maxLen = Math.Max(a.Count, b.Count);
            for (int i = 0; i < maxLen; i++)
            {
                int av = i < a.Count ? a[i] : 0;
                int bv = i < b.Count ? b[i] : 0;
                int sum = av + bv + carry;
                result.Add((byte)(sum & 0xFF));
                carry = sum >> 8;
            }
            if (carry > 0)
                result.Add((byte)carry);
            return result;
        }

        private static List<byte> SubtractAbsolute(List<byte> a, List<byte> b)
        {
            List<byte> result = new List<byte>();
            int borrow = 0;
            int maxLen = a.Count; // предполагаем, что a >= b
            for (int i = 0; i < maxLen; i++)
            {
                int av = a[i];
                int bv = i < b.Count ? b[i] : 0;
                int sub = av - bv - borrow;
                if (sub < 0)
                {
                    sub += 256;
                    borrow = 1;
                }
                else
                    borrow = 0;
                result.Add((byte)sub);
            }
            return result;
        }

        private static List<byte> MultiplyAbsolute(List<byte> a, List<byte> b)
        {
            int n = a.Count;
            int m = b.Count;
            int resultLen = n + m;
            int[] temp = new int[resultLen];
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    temp[i + j] += a[i] * b[j];
                }
            }
            List<byte> result = new List<byte>(new byte[resultLen]);
            int carry = 0;
            for (int i = 0; i < resultLen; i++)
            {
                int sum = temp[i] + carry;
                result[i] = (byte)(sum & 0xFF);
                carry = sum >> 8;
            }
            while (result.Count > 1 && result[result.Count - 1] == 0)
                result.RemoveAt(result.Count - 1);
            return result;
        }

        private static int CompareAbsolute(List<byte> a, List<byte> b)
        {
            if(a.Count != b.Count)
                return a.Count.CompareTo(b.Count);
            for (int i = a.Count - 1; i >= 0; i--)
            {
                if(a[i] != b[i])
                    return a[i].CompareTo(b[i]);
            }
            return 0;
        }
    }
}
