a, b = int(input()), int(input())

odd_list = [i for i in range(a+1,b) if i%2 != 0] #можно ли сделать это не двумя генераторами? Я не придумала как,
even_list = [i for i in range(a+1,b) if i%2 == 0] #если использовать именно генераторы
print(odd_list, even_list, sep='\n')