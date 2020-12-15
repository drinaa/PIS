#Это числа Фибоначчи, их можно рекурсией, можно ещё какими-то способами, но через for лучше не придумалось
def find_n(n):
    first = second = t = 1
    for i in range (2, n):
        t = first + second
        first = second
        second = t
    return (t)

n = int(input("Введите N: "))
print(find_n(n))