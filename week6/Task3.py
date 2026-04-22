scores = [100, 90, 80, 55, 95, 80, 65, 75, 70, 90]
sum = 0
for i in scores:
    sum = sum + i

mean = sum / len(scores)

vsum = 0
for i in scores:
    vsum = vsum + (i - mean) ** 2

variance = vsum / len(scores)

print("Means :", mean)
print("Variance :", variance)