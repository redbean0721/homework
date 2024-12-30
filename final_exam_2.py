# 輸入7個 1-49 的數字存入choose的串列中，必須判斷輸入數字在1-49，且數字不能重複。最後印出choose串列，作為購買樂透的選擇號碼。以亂數產生器產生7個1-49的不重複亂數，當作開獎號碼，並存入lotto的串列中。並比對choose, lotto如果完全相同，則印出恭喜中頭獎，否則印出未中頭獎。

import random

choose = []
lotto = []
counter = 0

while True:
    try:
        num = int(input(f"請輸入第 {counter+1} 個字: "))
        assert 1 <= num <= 49, "請輸入 1 ~ 49 內的數"
        if num in choose:
            print("此數字已經輸入過了")
            continue
        choose.append(num)
        counter += 1
        if counter == 7:
            break
    except ValueError:
        print("請輸入有效的整數")
    except AssertionError as e:
        print(e)

print(f"你投注的號碼為 {sorted(choose)}")

lotto = random.sample(range(1, 50), 7)
# print(sorted(lotto))

if sorted(choose) == sorted(lotto):
    print("恭喜中頭獎")
else: print("未中頭獎")
