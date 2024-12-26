# 請輸入6個 1-49 的數字存入choose的串列中，必須判斷輸入數字在1-49，且數字不能重複。最後印出choose串列。

choose = []
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
        if counter == 6:
            break
    except ValueError:
        print("請輸入有效的整數")
    except AssertionError as e:
        print(e)

print(f"你輸入的數字為 {choose}")