name = input("이름: ")
sc_id = input("학번: ")
birth = input("생년월일: ")
email = input("이메일: ")
goal = input("올해 대학생활 목표: ")

print("이름: %s" % name)
print("학번: %s" % sc_id)
print("생년월일: %s" % birth)
print("이메일: %s" % email)
print("올해 대학생활 목표: %s" % goal)


f = open("profile.txt", "w")

f.write("이름: %s\n" % name)
f.write("학번: %s\n" % sc_id)
f.write("생년월일: %s\n" % birth)
f.write("이메일: %s\n" % email)
f.write("올해 대학생활 목표: %s\n" % goal)

f.close()