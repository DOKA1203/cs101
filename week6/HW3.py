while True:
    n = int(input("정수를 입력하시오: "))

    rev = 0
    temp = n
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10

    if rev == n:
        print("회문수입니다.")
        break
    else:
        print("회문수가 아닙니다.")