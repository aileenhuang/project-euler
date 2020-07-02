def get_even_fib_sum(n):
    a, b = 1, 2
    total = 0
    while a < n:
        if a % 2 == 0:
            total += a
        tmp = b
        b = a + b
        a = tmp
    return total

if __name__ == "__main__":
    print(get_even_fib_sum(4000000))

