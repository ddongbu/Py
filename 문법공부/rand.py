import random
rand = random.randrange(1,45)
rand_list=[]
print("무작위 로또 번호 생성기")
for i in range(1,7):
    rand_list.append(rand)
    if rand == rand:
        rand_list.remove(rand)
    rand= random.randrange(1,45)
    rand_list.append(rand)

print(rand_list)