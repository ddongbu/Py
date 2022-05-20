

#빈 딕셔너리 생성
name_addressbook = {}

#while문으로 무한루프생성 (종료하지않고 1번 2번 추가하기위해)
while True:
    print("=================")
    print("[1]추가")
    print("[2]검색")
    print("[0]종료")
    select = input("선택:")
#if문으로 1번 2번 0번 종료 만들기
    if select == '1':
        name = input("이름입력:")
        phone = input("연락처입력:")
        name_addressbook[name] = phone
        for name,phone in name_addressbook.items():
            print(f"{name}:{phone}")
    elif select == '2':
        name = input("검색할 이름 입력:")
        phone = name_addressbook.get(name,'찾을 수 없음')
        print(f"{name}:",phone)
        continue

    elif select == '0':
        print("프로그램을 종료합니다.")
        break
