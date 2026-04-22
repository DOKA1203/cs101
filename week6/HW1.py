n = int(input("약수를 출력할 정수를 입력하시오: "))
cnt = 1
for i in range(1, n):
    if n % i == 0:
        cnt += 1
        print(i, end=", ")
print(n)
print("%d의 약수의 개수는 %d개입니다." % (n, cnt))
