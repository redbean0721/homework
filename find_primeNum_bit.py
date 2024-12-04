# 試撰寫一程式，使用者輸入一起始與終止區間的兩個正整數a與b，且a < b， 顯示這一區間的所有質數，並計算其總和，最後判斷總和是不是質數。

import math
import time

a = None
b = None

def is_prime(n):
    if n == 1: 
        return False
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
    # 從 2 開始
    if start < 2: 
        start = 2

    sieve_size = end - start + 1
    sieve = [True] * sieve_size  # 假設所有數都是質數

    for p in range(2, int(math.sqrt(end)) + 1):
        # 計算 p 在範圍內的第一個倍數
        start_index = max(p * p, start + (p - start % p) % p)  # 計算第一個有效的倍數
        if start_index == p:  # 如果第一個倍數是 p 本身，則從 p 的平方開始篩選
            start_index = p * p
        for multiple in range(start_index, end + 1, p):
            sieve[multiple - start] = False  # 標記非質數

    primes = [num for num, is_prime in enumerate(sieve, start=start) if is_prime]
    primes_sum = sum(primes)
    return primes, primes_sum

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

# start_time = time.time()
# primes, sum = aa(a, b)
primes, sum = sieve_of_eratosthenes_bit_array(a, b)
# end_time = time.time()
print(f"質數有: {primes}",
      f"\n質數的總和為: {sum}")
if is_prime(sum):
    print("總和 \033[1m是\033[0m 質數")
else:
    print("總和 \033[1m不是\033[0m 質數")
# print(f"執行時間: {end_time - start_time}")
