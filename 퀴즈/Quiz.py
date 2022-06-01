#변수를 이용하여 다음 문장을 출력하시오

#변수명
#:station
#변수값 사당,신도림,인천공항 순서대로 입력
#
#출력 문장
#xx행 열차가 들어오고 있습니다.

station = ["사당","신도림","인천공항"]

print("무슨 열차가 들어오고 있죠?")
menu = input("")
if(menu == "1"):
    print(f"{station[0]}행 열차가 들어오고 있습니다.")
elif(menu == "2"):
    print(f"{station[1]}행 열차가 들어오고 있습니다.")
elif(menu == "3"):
    print(f"{station[2]}행 열차가 들어오고 있습니다.")
