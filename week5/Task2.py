player1 = input("player1: ")
player2 = input("player2: ")

if player1 == player2:
    print("draw")
elif player1 == "가위":
    if player2 == "바위":
        print("player2")
    else:
        print("player1")
elif player1 == "바위":
    if player2 == "보":
        print("player2")
    else:
        print("player1")
else: #보
    if player2 == "가위":
        print("player2")
    else:
        print("player1")
