import random
num = input("게임 수:")

print("로또 번호 생성기")
for i in range(0,int(num)):
    lotto = random.sample(range(1,46),6)
    lotto.sort()
    print(lotto)


