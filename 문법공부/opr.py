#자판기 문제

#거스름돈 500원짜리 100원 짜리 동전 몇개를 거슬러줘야하나

money = int(input("투입한돈:"))
obj = int(input("물건의 가격:"))
str = money - obj
print(f"거스름돈:",str)
#500원 동전 갯수
#100원 동전 갯수
mo = str // 500
mo1 = str % 500
mo2 = mo1 // 100
#찍어내!
print(f"500원 동전 갯수:{mo}")
print(f"100원 동전 갯수:{mo2}")