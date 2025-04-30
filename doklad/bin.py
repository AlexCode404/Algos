def to_binary(n):
    if n == 0:
        return '0'
    b = ''
    while n:
        b = str(n % 2) + b
        n //= 2
    return b

n = int(input())
print(to_binary(n))
