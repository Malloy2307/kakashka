import random
import math

def main() -> int:
    p = is_prime()
    q = is_prime()
    n = p * q
    fi = (p - 1) * (q - 1)
    e = math.e
    if 1 < e < fi:
        print('я гей')

def is_prime() -> int:
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    return random.choice(prime_numbers)

if __name__ == '__main__':
    main()