def standard_weight(height, sex):
    if sex == "m":
        standard_weight = (height - 80) * 0.7
    else:
        standard_weight = (height - 70) * 0.6
    return standard_weight

height = None

while True:
    try:
        if height is None:
            height = float(input("請輸入身高 (cm): "))
            if height <= 80:
                height = None
                print("請輸入有效身高 (必須超過 80 cm)")
            continue

        sex = input("請輸入性別 (M)ale/(F)emale/(H)elicopter: ").strip().lower()
        if len(sex) >= 1 and sex[0] in ["m", "f", "h"]:
            if sex[0] == "h":
                print("我不接受直升機.w.")
                continue
            break
        else:
            print("請輸入有效性別")
    except ValueError:
        print("請輸入有效的參數")
    except KeyboardInterrupt:
        exit()

print(f"你的標準體重是: {round(standard_weight(height, sex[0]))} 公斤")
