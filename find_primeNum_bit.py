# 試撰寫一程式，使用者輸入一起始與終止區間的兩個正整數a與b，且a < b， 顯示這一區間的所有質數，並計算其總和，最後判斷總和是不是質數。

import math
import time

a = None
b = None

def is_prime(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# def aa(a, b):
#     primes = []
#     sum = 0
#     for num in range(a, b + 1):
#         if is_prime(n=num):
#             primes.append(num)
#             sum += num
#     return primes, sum

def sieve_of_eratosthenes_bit_array(start, end):
    if start < 2: 
        start = 2
    # 只處理奇數
    sieve_size = (end - start) // 2 + 1
    sieve = bytearray(sieve_size)

    # 將起點取到奇數
    start = max(3, start | 1)
    for p in range(3, int(math.sqrt(end)) + 1, 2):
        if p >= start and (p - start) % 2 == 0 and sieve[(p - start) // 2]:
            continue
        for multiple in range(max(p * p, (start + p - 1) // p * p), end + 1, 2 * p):
            sieve[(multiple - start) // 2] = 1

    primes = [2] if start <= 2 and end >= 2 else []
    primes += [start + 2 * i for i in range(sieve_size) if sieve[i] == 0]
    sum = sum(primes)
    return primes, sum

while True:
    try:
        if a == None:
            a = int(input("請輸入 a 的值: "))
            assert a > 0, "a 必須大於 0"
        if b == None:
            b = int(input("請輸入 b 的值: "))
            assert b > 0, "b 必須大於 0"
            assert a < b, "a 必須小於 b"
        break
    except ValueError:
        print("請輸入有效的整數")
    except AssertionError as e:
        print(e)
        if "a 必須大於 0" == str(e): a = None
        elif "b 必須大於 0" == str(e): b = None
        else: a = b = None
    except KeyboardInterrupt:
        exit()

# primes, sum = aa(a, b)
primes, sum = sieve_of_eratosthenes_bit_array(a, b)
print(f"質數有: {primes}",
      f"\n質數的總和為: {sum}")
if is_prime(sum):
    print("總和 \033[1m是\033[0m 質數")
else:
    print("總和 \033[1m不是\033[0m 質數")