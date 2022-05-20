#학점이 평균 3.5 이상이고 8시간 이상의 학내 봉사시간이 있어야 장학금을 받을수있다.
#두학기의 학점과 봉사시간을 입력받고 장학금을 받을수있을지 없을지 확인하는 프록그램

#2개의 학기 학점 변수 봉시사간 변수 입력받는다.
grade1 = float(input("학점이 어떻게되세요?:"))
grade2 = float(input("학점이 어떻게되세요?:"))
time = int(input("봉사시간이 어떻게되세요?:"))

avg = (grade1 + grade2) / 2

#if문 선언으로 and사용
if avg >= 3.5 and time >= 8 :
    print("장학금 대상 여부 : True")
else:
    print("장학금 대상 여부 : Flase")

