import sys

bord = [["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]]

def inputBord():
    print("  0 1 2")
    for i in range(len(bord)):
        print(i, *bord[i])
    print("")

def inputData(bord, player):
    try:
        N = int(input("Введите номер строки: "))
        M = int(input("Введите номер столбца: "))
        if not (M >= 0 and M < 3 and N >= 0 and N < 3):
            print("Вводите числа в диапазоне от 0 до 2.")
            inputData(bord, player)
        elif bord[N][M] != "-":
            print("Ячейка занята!")
            inputData(bord, player)
        else:
            bord[N][M] = player
    except ValueError:
        print('Вводите только числа!')
        inputData(bord, player)

def checkWiner(bord,player):
    def checkCells(a, b, c, player):
        if a == b == c == player:
            return True
    for i in range(3):
        if checkCells(bord[i][0],bord[i][1],bord[i][2], player) or \
        checkCells(bord[0][i], bord[1][i], bord[2][i], player) or \
        checkCells(bord[0][0], bord[1][1], bord[2][2], player) or \
        checkCells(bord[0][2], bord[1][1], bord[2][0], player):
            return True
    return False

def hod():
    counter = 0
    inputBord()
    while True:
        if counter % 2 == 0:
            print("Ходят х")
            player = "x"
        else:
            print("Ходят o")
            player = "o"
        counter += 1
        inputData(bord, player)
        inputBord()
        if counter == 9:
            print("Победила дружба)")
            break
        else:
            if checkWiner(bord, player):
                print(f"Победили {player}")
                break
            print("")

hod()
sys.exit()