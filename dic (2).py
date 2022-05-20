#좋아하는 장소 딕셔너리만들기

#딕셔너리선언

favorite_place = {
    '이상민':'내 집',
    '이진호':'울산 천곡동 돼지국밥집',
    '이아름별':'별침대',
    '홍성아':'피시방'
}

for name, place in favorite_place.items():
    print(f"{name}이 가장 좋아하는 장소는 {place}입니다.")