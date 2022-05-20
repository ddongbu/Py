#빈딕셔너리 선언후 저장한 학생들의 평균 점수 구하기

#딕셔너리 선언
students_dict = {}
#for문 범위 지정한뒤 키값 = 벨류값 선언
for stu in range(1,3):
    name = input("학생입력:")
    score = int(input("성적입력:"))
    students_dict[name] = score

#성적 평균내기
avg = sum(students_dict.values()) / len(students_dict)

#for문으로 학생들과 성적 찍어내기
for name, score in students_dict.items():
    print(f"{name}의 학생의 점수는 {score}입니다.")

print(f"학생들의 평균은:{avg}입니다.")

