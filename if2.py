#도형을 선택하고 그 도형들의 넓이를 구하라
#단 도형숫자 외 다른숫자를 입력하였을때 잘못된 입력입니다. 라고 띄우시오

#if문으로 도형선택 만들기
shape = int(input("도형을 선택해주세요 :(1:사각, 2:삼각, 3:원) "))

if shape == 1:
    opr1 = int(input("가로입력:"))
    opr2 = int(input("세로입력:"))
    sum = opr1 * opr2
    print(f"사각형의 넓이는 : {sum}cm입니다.")

elif shape == 2:
    opr1 = int(input("밑변입력:"))
    opr2 = int(input("높이입력:"))
    sum = (opr1 * opr2) / 2
    print(f"삼가형의 넓이는 : {sum}cm입니다.")

elif shape == 3:
    opr1 = int(input("반지름입력:"))
    sum = (opr1*opr1) * 3.14
    print(f"원의 넓이는 : {sum:0.2f}cm입니다.")
else :
    print("잘못된 입력입니다.")