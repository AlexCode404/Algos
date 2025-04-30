def gray_codes(n):
    codes = []
    total = 2 ** n
    for i in range(total):
        gray = i ^ (i >> 1)
        code_str = format(gray, f'0{n}b')
        codes.append(code_str)
    return codes

if __name__ == "__main__":
    n = 3
    result = gray_codes(n)
    print(result)  # ['000', '001', '011', '010', '110', '111', '101', '100']


