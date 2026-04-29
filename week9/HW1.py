def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n

def combination(n, r):
    if r > n or r < 0:
        return 0

    return factorial(n) // (factorial(r) * factorial(n-r))

def pretty_combination(n, r):
    print("%dC%d = %d" % (n, r, combination(n, r)))


pretty_combination(5,2)
pretty_combination(6,3)
pretty_combination(4,5)