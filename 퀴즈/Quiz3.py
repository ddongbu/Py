#url = "http://naver.com"
#url2 = "http://daum.net"
print("naver : 1")
print("daum : 2")
print("nate : 3")
menu = input("홈페이지 번호 입력: ")
url = ""
if(menu == "1"):
    url = "http://naver.com"
elif(menu=="2"):
    url = "http://daum.net"
elif(menu=="3"):
    url = "http://nate.com"

my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]

if(menu == "1"):
 password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
 print(f"{url}의 비밀번호는 {password}입니다.")
elif(menu == "2"):
 password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
 print(f"{url}의 비밀번호는 {password}입니다.")
elif(menu == "3"):
 password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
 print(f"{url}의 비밀번호는 {password}입니다.")