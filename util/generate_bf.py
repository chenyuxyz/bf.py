"""
Brainfuck code generator
"""

def prime_factorize(n):
    assert n > 0
    def _fac(n, primes):
        for i in range(2, n+1):
            if i * i > n:
                if n > 1:
                    primes.append(n)
                return primes
            if n % i == 0:
                primes.append(i)
                return _fac(n // i, primes)
    return [1] if n == 1 else _fac(n, [])

def generate_int(n):
    def _generate(n):
        if n == 0:
            return ""
        primes = prime_factorize(n)
        bfcode = ">" * (len(primes) - 1)
        bfcode += "[<".join("+" * p for p in primes)
        bfcode += ">-]" * (len(primes) - 1)
        bfcode += "<" * (len(primes) - 1)
        return bfcode
    if n == 0:
        return ""
    bfcodes = [_generate(n)]
    for i in range(1, 10):
        if n-i >= 0:
            bfcodes.append(_generate(n-i) + "+" * i)
        if n+i < 256:
            bfcodes.append(_generate(n+i) + "-" * i)
    return min(bfcodes, key=len)

def generate_print_str(string):
    bfcode = ""
    for char in string:
        bfcode += "[-]" + generate_int(ord(char)) + "."
    return bfcode
