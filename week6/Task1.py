result = [55, 90, 89, 76, 37, 100, 67]
i=1
for score in result:
    if 100 >= score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print("%d번 학생은 %d점으로 %s입니다." % (i, score, grade))
    i += 1
