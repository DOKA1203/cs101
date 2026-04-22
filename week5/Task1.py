a = tuple(map(int, input("input ay, ax: ").split(",")))
b = tuple(map(int, input("input by, bx: ").split(",")))

# a = (5, 5)
# b = (7, -5)

if a == b:
    print("Same Point")
elif a[0] == -b[0] and a[1] == b[1]:
    print("X-axis symmetry")
elif a[0] == b[0] and a[1] == -b[1]:
    print("Y-axis symmetry")
elif a[0] == -b[0] and a[1] == -b[1]:
    print("Origin symmetry")
else:
    print("Nothing")