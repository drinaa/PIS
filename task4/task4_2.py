#вариант 28
# Начальная популяция: случайная генерация
# Отбор: выбор каждой особи пропорционально приспособленности (рулетка)
# Скрещивание: однородный (каждый бит от случайно выбранного родителя)
# Мутация: инвертирование всех битов у 1 особи
# Новая популяция: замена своих родителей

import random

#фитнесс-функция
def fitness_func(individual, list_weight, list_size, list_value):
    sum1,sum2,sum3 = 0,0,0
    for i in range(len(list_weight)):
        sum1 += individual[i] * list_weight[i]
        sum2 += individual[i] * list_size[i]
        sum3 += individual[i] * list_value[i]
    if sum1 > max_weight or sum2 > max_size: fitness = 0
    else: fitness=sum3
    return fitness

#создание популяции
def create_population(list_weight, list_size, individuals_number):
    population = []
    for j in range (individuals_number):
        individual = [0 for i in range(len(list_size))]
        sum_weight, sum_size = 0,0


        for elem in range(len(list_size)):
            rnd_ind = random.randint(0,1)
            individual[elem] = rnd_ind
            if (sum_weight + list_weight[elem] > max_weight) or (sum_size + list_size[elem] > max_size):
                individual[elem] = 0
                continue
            else:
                if individual[elem] == 1:
                    sum_weight += list_weight[elem]
                    sum_size += list_size[elem]
        population.append(individual)
    return population

#получение лучшей особи
def get_best_individual(population, list_weight, list_size, list_value):
    individuals = []

    for ind in population:
        individuals.append((fitness_func(ind, list_weight, list_size, list_value), ind))

    best_ind = individuals[0]
    for elem in individuals:
        best_ind = elem if elem[0] > best_ind[0] else best_ind

    return best_ind


#отбор для скрещивания
def selecting_for_crossing(populaton, list_weight, list_size, list_value):
    res_individuals = []
    individuals = [] #массив для фитнес-функций
    for i in range(len(population)):
        individuals.append(fitness_func(population[i], list_weight, list_size, list_value))

    max_fitness = max(individuals)
    min_fitness = individuals[0]
    for m in range(len(individuals)):
        if (individuals[m] < min_fitness) and individuals[m] != 0:
            min_fitness = individuals[m]

    #отбор родителей
    d = max_fitness - min_fitness
    for m in range(len(individuals)):
        if random.random() < individuals[m]:
            res_individuals.append(populaton[m])
    return res_individuals

#создание новой особи - результат скрещивания
def new_child(f_parent, s_parent):
    individual = [0 for i in range(30)]
    for elem in range(30):
        rnd_ind = random.randint(0, 1)
        individual[elem] = rnd_ind
    return individual

#скрещивание
def crossing (parents, list_weight, list_size, list_value):
    children = []
    length = len(parents) - 1
    while length > 0:
        first_ind = random.randint(0, length)
        first_parent = parents[first_ind]
        parents.pop(first_ind)
        length -= 1
        second_ind = random.randint(0, length)
        second_parent = parents[second_ind]
        parents.pop(second_ind)
        first_child = new_child(first_parent, second_parent)
        second_child = new_child(first_parent, second_parent)
        # вместо нежизнеспособного ребенка возвращаем родителя
        if fitness_func(first_child,  list_weight, list_size, list_value) == 0:
            first_child = first_parent
        if fitness_func(second_child,  list_weight, list_size, list_value) == 0:
            second_child = second_parent

        children.append(first_child)
        children.append(second_child)
        length -= 1

    return children

#обновление популяции (замена родителей детьми)
def update_pop(population, parents, res_crossing):
    new_pop = []
    for indiv in population:
        if indiv not in parents:
            new_pop.append(indiv)
    new_pop.extend(res_crossing)
    return new_pop

#мутация
def mutation(population, list_weight, list_size, list_value):
    new_indiv = []
    mut_index = random.randint(0, len(population))
    mut_indiv = population[mut_index]
    for i in range(30):
        if mut_indiv[i] == 0:
            new_indiv.append(1)
        else:
            new_indiv.append(0)

    if fitness_func(new_indiv, list_weight, list_size, list_value) == 0:
        new_indiv = [0]*30

    population.pop(mut_index)
    population.insert(mut_index, new_indiv)

    return population


def ga(population, list_weight, list_size, list_value, max_weight, max_size):
    min_value = min(list_value)
    list_last_value = [0]*10
    last_count = 0
    best_individual = get_best_individual(population, list_weight, list_size, list_value)[1]

    for l in range(max_generation):
        parents = selecting_for_crossing(population, list_weight, list_size, list_value)

        res_crossing = crossing(parents, list_weight, list_size, list_value)

        population = update_pop(population, parents, res_crossing)

        population = mutation(population, list_weight, list_size, list_value)

        #поиск лучшей особи нового поколения
        new_best = get_best_individual(population, list_weight, list_size, list_value)

        #проверка лучшей особи среди всех поколений
        if new_best[0] > fitness_func(best_individual, list_weight, list_size, list_value):
            best_individual = new_best[1]

        list_last_value[last_count] = new_best[0]
        last_count += 1

        if last_count >= len(list_last_value):
            last_count = 0
            # если за последние несколько поколений ценность менялась меньше чем на стоимость самой дешевой вещи - заканчиваем
        if abs(min(list_last_value) - max(list_last_value)) <= min_value:
            break

    return (best_individual)

#основная программа
#загрузка и обработка начальных данных
file_name = '28.txt'
matrix_data = []
with open(file_name) as f:
    for line in f:
        matrix_data.append([float(x) for x in line.split()])

max_weight = matrix_data[0][0]
max_size = matrix_data[0][1]

del matrix_data[0]

list_weight, list_size, list_value = [], [], []

for i in range(len(matrix_data)):
    list_weight.append(matrix_data[i][0])
    list_size.append(matrix_data[i][1])
    list_value.append(matrix_data[i][2])

individuals_number = 200 #количество особей в популяции
max_generation = 500

population = create_population(list_weight, list_size, individuals_number)
result = ga(population, list_weight, list_size, list_value, max_weight, max_size)

sum_size, sum_weight = 0, 0

res = []
for i in range(len(result)):
    sum_size += result[i] * list_size[i]
    sum_weight += result[i] * list_weight[i]

    if result[i] == 1:
        res.append([i, list_weight[i], list_size[i], list_value[i]])

print("При максимальной грузоподъёмности", round(max_weight, 2), "было сложено груза весом", round(sum_weight,2),
". При максимальной вместимости", round(max_size,2), "было сложено груза объёмом", round(sum_size,2),
". Ценность груза при этом", round(fitness_func(result, list_weight, list_size, list_value),2))
