seats = ['O', 'X', 'O', 'O', 'X', 'O'] # O 빈 자리, X 예약된 자리.

print(seats.count('X'))

seats[2] = 'X'
print(seats)

seats[-2] = 'O'
print(seats)

has_two_empty = False
for i in range(len(seats) - 1):
    if seats[i] == 'O' and seats[i + 1] == 'O':
        has_two_empty = True

print(has_two_empty)
