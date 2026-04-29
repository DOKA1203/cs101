def is_triangle(a,b,c):
    return a+b>c and a+c>b and b+c>a

a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))
res = is_triangle(a,b,c)

if res:
    print("YES")
else:
    print("NO")