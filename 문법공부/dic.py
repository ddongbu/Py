#빈 딕셔너리 만들기
dict_student = {}

#딕셔너리 안에 for루프로 5명의 학생이름 점수 받아서 딕셔너리에 저장
for i in range(1,6):
    name = input("이름:")
    score = float(input("점수:"))
    dict_student[name] = score
#딕셔너리 안에 값들의 평균 출력
avg = sum(dict_student.values()) / len(dict_student)

for name, score in dict_student.items():
    print(f"학생 이름: {name} 학점: {score}")
print(f"학생들의 평균은 {avg:.1f}입니다.")

