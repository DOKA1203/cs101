def gcd_lcm(mode, a, b):
    if mode == "gcd":
        if b == 0:
            return a
        return gcd_lcm(mode, b, a % b)
    elif mode == "lcm":
        return a * b // gcd_lcm("gcd", a, b)
    else:
        return "Error"

a = 12
b = 18
print("%d와 %d의 최대 공약수:" % (a,b), gcd_lcm("gcd", a, b))
print("%d와 %d의 최소 공배수:" % (a,b), gcd_lcm("lcm", a, b))

# Error
print(gcd_lcm("er", a, b))