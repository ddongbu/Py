#게산기 프로젝트


while True:
    print("==============")
    print("[1] 덧셈")
    print("[2] 뺄셈")
    print("[3] 나눗셈")
    print("[4] 곱셈")
    print("[5] 프로그램 종료")

    i = input("선택:")
    if i == "1":
        input1 = int(input("첫 번째 숫자를 입력하세요"))
        input2 = int(input("첫 번째 숫자를 입력하세요"))

        total = input1 + input2
        print(f"두 수의 합 : {total} ")

    elif i == "2":
        input1 = int(input("첫 번째 숫자를 입력하세요"))
        input2 = int(input("첫 번째 숫자를 입력하세요"))

        total = input1 - input2
        print(f"두 수의 차 : {total} ")

    elif i == "3":
        input1 = int(input("첫 번째 숫자를 입력하세요"))
        input2 = int(input("첫 번째 숫자를 입력하세요"))

        total = input1 / input2
        print(f"두 수의 몫 : {total} ")

    elif i == "4":
        input1 = int(input("첫 번째 숫자를 입력하세요"))
        input2 = int(input("첫 번째 숫자를 입력하세요"))

        total = input1 * input2
        print(f"두 수의 곱 : {total} ")

    elif i == "5":
        break