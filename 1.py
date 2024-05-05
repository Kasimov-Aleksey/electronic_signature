import gmpy2

start = 0
end = gmpy2.mpz(2) ** 2048

numbers_list = [gmpy2.mpz(i) for i in range(start, end)]

print(numbers_list)