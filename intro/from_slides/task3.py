def square(n):
    for i in range(1, n+1, 2):
        print(i**2, end=' ')

n = int(input("Введите N: "))
square(n)