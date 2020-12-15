old_list = [5, 3, -2, 4, 2, -6, -3, -9, 8]

negative = []
positive = []
a = [positive.append(elem) if elem >= 0 else negative.append(elem) for elem in old_list]

print(f"Positive: {positive} \nNegative: {negative}")

#Тут попыталась вместо двух проходов по списку сделать 1, но чтобы сработало, пришлось извернуться и впихать
#третий список. Не уверена, что такой вариант лучше того, что был в предыдущей задаче с двумя генераторами.
#Но на большее мой мозг не способен.