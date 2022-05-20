#사용자로부터 정수 3개의 숫자를 입력 받아 평균을 계산하고 출력한다.
opr1 = int(input("1st:"))
opr2 = int(input("2nd:"))
opr3 = int(input("3nd:"))

sum = opr1+opr2+opr3
avg = float(sum)/3

print(f"11,7,4의 평균은 {avg:.2f}입니다.")