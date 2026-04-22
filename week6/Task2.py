a = [4,3,2,9,7,18,22,13,6,24,37,12]

prime_count = 0
composite_count = 0

for i in a:
    flag = True # True means prime number
    for j in range(2,i):
        if i % j == 0:
            flag = False
            break
    if flag:
        prime_count += 1
    else:
        composite_count += 1

print("Prime Numbers: %d\nComposite Numbers: %d" % (prime_count, composite_count))
