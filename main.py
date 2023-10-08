import math
import random
 
# step 1
def is_prime() -> int:
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    return random.choice(prime_numbers)


def min() -> int:
    
    msg = int(input())
    
    p = is_prime()
    q = is_prime()
    n = p*q
    print("n =", n)
    
    phi = (p-1)*(q-1)
    
    e = 4
    
    while(1<e<phi):
        if (math.gcd(e, phi) == 1): #Возвращает наибольший общий делитель указанных целочисленных аргументов. Если какой-либо из аргументов отличен от нуля, то возвращаемое значение является наибольшим положительным целым числом, которое является делителем всех аргументов.
            break
        else:
            e += 1
 
    print("e =", e)

    k = e
    d = ((k*phi)+1) / e
    print("d =", d)
    print(f'Public key: {e, n}')
    print(f'Private key: {d, n}')
    print(f'Original message:{msg}')
 
    C = pow(msg, e)
    C = math.fmod(C, n)
    print(f'Encrypted message: {C}')
 
    M = pow(C, d)
    M = math.fmod(M, n)
 
    print(f'Decrypted message: {M}')
    
min()