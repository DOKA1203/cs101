time = input("")
hour, minute = map(int, time.split(":"))

minute -= 30
if minute < 0:
    hour -= 1
    minute += 60
    if hour < 0:
        hour += 24

print("%02d:%02d" % (hour, minute))