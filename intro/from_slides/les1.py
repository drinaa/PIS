#Tuple - неизменяемый список, задаётся в ()
#Set - множество - набор уникальных элементов
#Dictionary - ключ-значение. Ключ должен быть неизменяемый


def figure1(a):
    for i in range(1, a+1):
        print('*' * i)

def figure2(a):
    for i in range(a, 0, -1):
        print(' ' * (a-i) + '*' * i)

def figure3(a):
    for i in range(1, a+1):
        print('*' * (a+1 - i) + ' ' * (i - 1))

def figure4(a):
    s = ""
    for i in range(a):
        s += (' ' * i + '*' * ((a * 2 - 1) - i * 2) + ' ' * i) + '\n'


def figure5(a):
    for i in range(a+1, 0, -1):
        print(' ' * (i - 1) + '*' * (a+2 - i))

def figure6(a):
    for i in range(a-1, -1, -1):
        print(' ' * i + '*' * ((a*2-1) - i * 2) + ' ' * i)


def figure7(a):
    for i in range(round(a/2), round(-a/2)-1, -1):
         print(' ' * abs(i) + '*' * (a - abs(i * 2)))

ask_num = int(input("Введите номер фигуры, которую нужно вывести: "))
ask_kol = int(input("Введите количество строк, которое должно получиться: "))
if ask_num == 1:
    figure1(ask_kol)
elif ask_num == 2:
    figure2(ask_kol)
elif ask_num == 3:
    figure3(ask_kol)
elif ask_num == 4:
    figure4(ask_kol)
elif ask_num == 5:
    figure5(ask_kol)
elif ask_num == 6:
    figure6(ask_kol)
elif ask_num == 7:
    figure7(ask_kol)

