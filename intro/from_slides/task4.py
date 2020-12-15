print("Введите A и B")
a, b = int(input()), int(input())

sum = 0
mult = 1
for i in range (a, b+1):
    sum += i
    mult *= i
print (f"Сумма чисел от {a} до {b} равна {sum}. Произведение этих чисел равно {mult}")