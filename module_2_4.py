numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    a = numbers[i]
    is_prime = True

    for j in range(2, a):
        if a % j == 0:
            is_prime = False
            break
    if a == 1:
        continue
    elif is_prime:
        primes.append(a)
    else:
        not_primes.append(a)
print(primes)
print(not_primes)
