def get_largest_palindrome(digits):
	lower = 10 ** (digits - 1)
	upper = 10 ** digits

	products = []
	for i in range(upper, lower - 1, -1):
		for j in range(i, lower - 1, -1):
			prod_str = str(i * j)
			if prod_str[:len(prod_str)//2] == prod_str[len(prod_str)//2:][::-1]:
				products.append(int(prod_str))
	return max(products)

if __name__ == '__main__':
	print(get_largest_palindrome(3))