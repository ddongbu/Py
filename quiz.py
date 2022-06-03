#수의 지수 표현
a = 1e9 // 1,000,000,000
a = 75.25e1 // 752.5
a = 3954e-3 // 3.954

#반올림 round 함수
round(123.456, 2) // 123.46
#리스트 컴프리헨션
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [ i for i in range(20) if i % 2 == 1 ]

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [ i**2 for i in range(10) ]

# 2차원 리스트 초기화
n = 3
m = 3
array = [[0] * m for _ in range(n)]
print(array)
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#리스트 관련 기타 메서드
#변수.reverse() # 리스트의 순서 모두 뒤집음
#변수.count(특정 값) # 리스트에서 특정 값을 가지는 데이터의 개수
#변수.remove(특정 값) # 특정 값 가지는 원소 제거, 값이 여러 개면 하나만 제거

#append() 함수는 O(1)에 실행되지만
#insert() 함수는 O(N)에 실행된다 # 원소를 삽입한 뒤에, 리스트의 원소 위치를 조정해줘야 하기 때문

#특정한 값의 원소를 모두 제거하려면?
a = [1, 2, 3, 4, 5]
remove_set = [1, 4]
result = [i for i in a if i not in remove_set] // [2, 3, 5]
#문자열 연산
a = "Hello"
b = "World"
print(a+b)
print(a + " " + b)
#HelloWorld
#Hello World

#튜플
#튜플 자료형은 리스트와 거의 비슷하지만 다음과 같은 차이가 있다.
#-튜플은 한 번 선언된 값을 변경할 수 없다.
#-리스트는 대괄호를([])를 이용하지만, 튜플은 소괄호(())를 이용한다

#튜플 자료형은 그래프 알고리즘을 구현할 때 자주 사용된다.
#Dictionary 관련 함수
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()

# 각 기에 따른 값을 하나씩 출력
for key in key_list:
	print(data[key])
Set
# Set은 다음과 같은 특징이 있다.
#-중복을 허용하지 않는다.
#-순서가 없다.

# Set 초기화 방법 1
data = set([1, 1, 2, 3, 4, 4, 5])

# Set 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
# Set의 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합