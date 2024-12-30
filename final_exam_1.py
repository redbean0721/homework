while True:
    try:
        score = int(input("請輸入你的成績: "))
        if score == -999:
            break
        assert score <= 100, "成績不可以大於 100"
        assert score > 0, "成績不可以小於 0"
        if score >= 90:
            print("GRADE A")
        elif score >= 80:
            print("GRADE B")
        elif score >= 70:
            print("GRADE C")
        elif score >= 60:
            print("GRADE D")
        else:
            print("GRADE E")
    except ValueError:
        print("請輸入有效的整數")
    except AssertionError as e:
        print(e)