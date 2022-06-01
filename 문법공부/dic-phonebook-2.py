#딕셔너리 생성
dict_PhoneBook = {}

#반복 연락처 입력
while True:
    print("==============")
    print(" [1] 추가")
    print(" [2] 검색")
    print(" [0] 종료")
    print("==============")
    a = input("선택:")
    if a == "1":
        print("추가 기능 수행")
        for i in range(1,3):
            name = input("이름:")
            if name == '':
                break
            phone = input("연락처:")
            dict_PhoneBook[name] = phone
        print("====연락처목록====")
        for name, phone in dict_PhoneBook.items():
            print(f"{name}: {phone}")
    elif a == "2":
        print("검색 기능 수행")
        name = input('검색할 이름 입력:')
        phone = dict_PhoneBook.get(name, '해당 이름의 연락처를 찾을 수 없습니다.')
        print(f'{name}:', phone)

    elif a == "0":
        print("프로그램을 종료합니다.")
        break

