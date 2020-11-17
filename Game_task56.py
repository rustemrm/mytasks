def draw_game():
    print("\nИгра в крестики-нолики\n")
    print("\n      0      1      2")
    j = 0
    for i in range(0, 3):
        row_line1 = "\n" + str(i) + "   "
        for j in range(j, j + 3):
            row_line1 = row_line1 + row_line[j]
        j += 1
        print(row_line1)
    return


def make_move():
    i = 0
    while i == 0:
        print("\nИгрок номер " + str(player) + " сделайте ход:\n")
        num_row = int(input("Введите номер столбца: "))
        num_col = int(input("\nВведите номер строки : "))
        num_position = num_row + num_col * 3
        if (num_row in range(0, 3)) and (num_col in range(0, 3)) and row_line[num_position] == no_move:
            row_line.pop(num_position)
            row_line.insert(num_position, new_move1 if player == 1 else new_move2)
            i = 1
        else:
            print("\nОшибка ввода строки или столбца!")
    return


def check_win(game):
    line_win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in range(len(line_win)):
        check_line = ""
        for j in range(len(line_win[1])):
            check_line = check_line + row_line[(line_win[i][j] - 1)]
        if check_line == 3 * new_move1 or check_line == 3 * new_move2:
            draw_game()
            print(" \nИгра закончена! Выиграл игрок " + str(player))
            game = False
        elif no_move not in row_line:
            print(" \Ходов больше нет, ничья ")
            game = False
    return game

def change_player(player):
    player = 2 if player == 1 else 1
    return player

no_move = "| - |  "
new_move1 = "| X |  "
new_move2 = "| o |  "
player = 1
game = True
row_line = [no_move for i in range(0, 9)]
while game:
    draw_game()
    make_move()
    game = check_win(game)
    player = change_player(player)
