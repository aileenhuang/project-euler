"""
Brute-force solution:
Loop from 1 to n, inspecting if each number is (1) a factor of n, and if so, (2) a prime

Slightly more optimized solution:
Loop from 1 to n.
If each number is a prime factor, divide by that number.
"""
def get_largest_prime_factor(n):
	factors = []
	i = 2

	while i <= n:
		if n % i == 0:
			factors.append(i)
		while n % i == 0:
			n = n / i
		i += 1

	return factors[-1]

if __name__ == "__main__":
    print(get_largest_prime_factor(600851475143))
