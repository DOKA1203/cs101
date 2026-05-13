nums = [1, 2, 3, 4, 5, 6, 7, 8]

print(nums[1::2])

front = nums[:4]
back = nums[4:]

print(front, back)

result = front + back[::-1]
print(result)