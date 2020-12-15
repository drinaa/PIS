field = list(range(1, 10))  # массив для хранения значений игрового поля

wins_cort = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (4, 6, 9)]


# функция, отрисовывающая поле
def draw_field():
    print(' -----------')
    for i in range(3):
        print('|', field[i * 3 + 0], '|', field[i * 3 + 1], '|', field[i * 3 + 2], '|')
    print(' -----------')


# функция запроса ввода от пользователя с проверкой
def player_input(player_symb):
    while True:
        val = int(input(f'В какое поле поставить {player_symb}: '))
        if (val < 1) or (val > 9):
            print('Ошибочное значение, повторите ввод.')
            continue
        if str(field[val - 1]) in 'XO':
            print('Эта клетка занята. Выберите другое поле.')
            continue
        field[val - 1] = player_symb
        break


def check_win():
    for elem in wins_cort:
        if field[elem[0] - 1] == field[elem[1] - 1] == field[elem[2] - 1]:
            return field[elem[0] - 1]
    else:
        return False


def play():
    counter = 0  # счётчик ходов для определения очереди игроков
    while True:
        draw_field()
        if counter % 2 == 0:
            player_input('X')
        else:
            player_input('O')
        if counter > 3:
            win_player = check_win()
            if win_player:
                draw_field()
                print(f'Поздравляю! Игрок {win_player} выиграл!')
                break
        counter += 1
        if counter > 8:
            print('Ничья')
            break


while True:
    print('Выберите действие: ')
    print('1 - Сыграть в крестики-нолики')
    print('2 - Выйти')
    if input() == '1':
        play()
    else:
        break
