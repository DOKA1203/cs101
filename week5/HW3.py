student_number = 12263723
overdue = False

input_number = int(input("학번을 입력하세요: "))
if input_number != student_number:
    print("등록되지 않은 이용자입니다.")
elif overdue:
    print("연체로 인해 출입이 제한됩니다.")
else:
    print("출입 가능합니다.")