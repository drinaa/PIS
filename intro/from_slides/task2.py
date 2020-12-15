def find_n(n):
    first = second = third = t = 1
    for i in range (3, n):
        t = first + second + third
        first = second
        second = third
        third = t
    return (t)

n = int(input("Введите N: "))
print(find_n(n))