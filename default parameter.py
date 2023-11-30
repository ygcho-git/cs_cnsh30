# 1. 매개변수의 기본값 지정

def score_table(name, age=17, school="충남과학고", kor=70, eng=80) :
    print(f"{school} {age}세 {name}, 총점 : {kor + eng}")

score_table("홍길동", 18, "율도고", 73, 78)   # 율도고 18세 홍길동, 총점 : 151
score_table("김철수")                        # 충남과학고 17세 김철수, 총점 : 150
#score_table()  # 오류

score_table("김영수", 88, 90)                # 90 88세 김영수, 총점 : 150
score_table("이영희", kor=88, eng=90)        # 충남과학고 17세 이영희, 총점 : 178

score_table(eng=80, kor=70, school="충곽", age=18, name="홍길동") # 충곽 18세 홍길동, 총점 : 150



# 2. 가변인자 예시
a = int("10")
#b, c = int("20", "30")

max_v = max(10, 35, 20, 13)
print(max_v)

min_v = min(5, 2, 3)
print(min_v)


print("뽀로로", "루피", "크롱")



# 3-1. 가변인자 적용한 함수 예시
def func1(a, *b) :
   print(a, b)

func1(1, 2, 3)


# 3-1. 가변인자 적용한 함수 예시
def func2(*a) :
   print(a)
   print(a[0] + a[1] + a[2])

func2( 1, 2, 3 )