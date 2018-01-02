
def sieve_of_erastothenes(n):
    """returns list of prime numbers using sieve of erasthotenes up to n."""
    multiples = set()

    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update([z for z in range(i*i, n+1, i)])

print(list(sieve_of_erastothenes(100)))

def is_prime(n):
    x = 2
    while x*x <= n:
        if n % x == 0:
            return False
        x += 1
    return True
# runtime : O(square root of N)

def sum_digits(n):
    total_sum = 0
    while n > 0:
        print("n", n)
        print("sum", total_sum)
        total_sum += n % 10
        print("sum", total_sum)
        n //= 10
        print(n)
    return total_sum
