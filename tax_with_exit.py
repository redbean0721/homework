# 級距1：0-520000 x 5% -0
# 級距2：520001-1170000 x 12% -36400
# 級距3：1170001-2350000 x 20% -130000
# 級距4：2350001-4400000 x 30% -365000
# 級距5：4400001-10000000 x 40% -805000
# 級距6：10000001以上 x 45% -1305000

def calculate_tax(income):
    if income <= 520000:
        tax = income * 0.05
    elif income <= 1170000:
        tax = income * 0.12 - 36400
    elif income <= 2350000:
        tax = income * 0.20 - 130000
    elif income <= 4400000:
        tax = income * 0.30 - 365000
    elif income <= 10000000:
        tax = income * 0.40 - 805000
    else:
        tax = income * 0.45 - 1305000
    return tax

while True:
    try:
        income = int(input("請輸入您的年收入: "))
        if income == -999:
            print("程式結束")
            break
        elif income < 0:
            print("輸入不能為負數，請重新輸入。")
        else:
            tax = round(calculate_tax(income))
            print(f"應繳所得稅為: {tax} 元")
            break
    except ValueError:
        print("請輸入有效的整數。")
