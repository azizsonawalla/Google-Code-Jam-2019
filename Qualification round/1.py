for i in range(0, 10**10+1):
    n = str(i)
    if not ("4" in n):
        a = int(n)
        b = 0
    else:
        m = ""
        for digit in map(int, n):
            if digit == 4:
                m += "1"
            else:
                m += "0"
        a = int(m)
        b = int(n) - a
    if (("4" in str(a)) or ("4" in str(b)) or (a + b != i)):
        print("FAIL")
print("PASS!")