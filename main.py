def printBoard():
    for i in range(0, 9, 3):
        print(board[i] + '|' + board[i + 1] + '|' + board[i + 2])


def checkWin(player):
    condition = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for con in condition:
        if all(board[i] == player for i in con):
            return True
    return False


playingNow = 'X'
board = ['#' for _ in range(9)]

while True:
    printBoard()
    choiceInput = int(input(f"Игрок {playingNow}, Введите куда поставить (0-9): ")) - 1
    if board[choiceInput] == '#' and 0 <= choiceInput < 9:
        board[choiceInput] = playingNow
        if checkWin(playingNow):
            printBoard()
            print(f'{playingNow} выиграл!')
            break
        elif '#' not in board:
            printBoard()
            print('Ничья!')
            break
        else:
            playingNow = 'O' if playingNow == 'X' else 'X'
    else:
        print('Данная клетка уже занята или не существует')
