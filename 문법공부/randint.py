import random

#1~100사이의 임의의 숫자를 생성한다.
rnd_number = random.randint(1,100)

#count해줄 값 초기화
count = 0
#for문으로 적을값 생성
for pas in range(1,11):
    user_number = int(input("숫자 입력 해주세요:"))
    count += 1
    if(rnd_number > user_number):
        print("숫자값이 작아요")
    elif(rnd_number < user_number):
        print("숫자값이 커요")
    else :
        break

if user_number == rnd_number :
    print(f"정답입니다! 총 도전횟수는 : {count}회 입니다.")
else:
    print("10번의 기회에도 틀렸습니다...정답은"+str(rnd_number)+"입니다.")