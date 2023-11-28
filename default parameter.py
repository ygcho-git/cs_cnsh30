# default parameter
def introduce(name, age, school="충남과학고") :
    print("이름 :", name, "나이 :", age, "학교 :", school)

introduce("홍길동", 18, "율도고")
introduce("곽운규", 17)          
#introduce("곽운규")

introduce(17, "곽운규")          
introduce(age=17, name="곽운규")


# 가변인자
