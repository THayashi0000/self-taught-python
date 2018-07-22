X = [3, 4, 8]

while True:
    try:
        x = input("数字を入力してください:")
        if x == "q":
            break
        elif int(x) in X:
            print("正解")
        else:
            print("不正解")
    except ValueError:
        print("数字を入力するか、ｑで終了します。")
