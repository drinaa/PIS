import json
import math

import pandas as pd

variant = 34
not_watching = -1  # обозначение непросмотренного фильма
sim_uv = []
rv = []
new_mark = {}
dict_recommend_film = {}


# высчитывает метрику для двух пользователей и сразу считает среднюю оценку (учитывая, что средняя оценка -
# это сумма всех проставленных оценок / на кол-во просмотренных фильмов(а не всех фильмов)
def sim(u, v):
    total_sum, u_sum, v_sum, col, sum_uv, vc = 0, 0, 0, 0, 0, 0
    for i in range(num_films):
        if v[i] != not_watching:
            total_sum += v[i]
            col += 1
            if u[i] != not_watching:
                sum_uv += (u[i] * v[i])
                u_sum += u[i] ** 2
                v_sum += v[i] ** 2
    return round(sum_uv / (math.sqrt(u_sum) * math.sqrt(v_sum)), 3), round(total_sum / col, 3)


# высчитывает дробь из формулы оценки
def calc_mark(data):
    data.columns = ['mov', 'sim', 'rv']
    data = data.drop(data[data.mov == not_watching].index)
    data['sum_ch'] = round(data.sim * (data.mov - data.rv), 3)
    res_calc_mark = round(sum(data.sum_ch) / sum(abs(data.sim)), 3)
    return res_calc_mark


def recommend_mark(data, my_str):
    knn = 4
    for i in range(num_users):
        v_df = list(data.iloc[i])
        ret = sim(my_str[0], v_df)
        sim_uv.append(ret[0])
        rv.append(ret[1])
    data2 = data.assign(sim = sim_uv, rv = rv)
    my_mean = data2.at['User ' + str(variant), 'rv']
    data2 = data2.sort_values(by = ['sim'], ascending = False)
    data2 = data2.iloc[1:knn + 1]
    for i in range(num_films):
        if my_str[0][i] == not_watching:
            new_mark['Movie ' + str(i + 1)] = round(my_mean + calc_mark(data2.iloc[:, [i, -2, -1]]), 3)
    return new_mark


def recommend_film(dict_films):
    not_watch_films = [i for i in dict_films]
    for film in not_watch_films:
        film_place_day = round((dp[dp[film] == 'h'].shape[0] + dd[dd[film] == 'Sat'].shape[0] +
                                dd[dd[film] == 'Sun'].shape[0]) / dp[dp[film] != not_watching].shape[0], 3)
        film_ser = df[film]
        avg_film = round(sum(film_ser[film_ser != not_watching]) / num_films)
        rate_film = avg_film + film_place_day
        dict_recommend_film[film] = rate_film
    return dict_recommend_film

#стоит ли передавать df,dp,dd в функции?
df = pd.read_csv('data.csv', index_col = 0, sep = ',\s+', engine = 'python')
dp = pd.read_csv('context_place.csv', index_col = 0, sep = ',\s+', engine = 'python')
dd = pd.read_csv('context_day.csv', index_col = 0, sep = ',\s+', engine = 'python')
num_films = df.shape[1]
num_users = df.shape[0]
my_str_df = df.loc[df.index == 'User ' + str(variant)]  # выделяю свой вариант
res_task1 = recommend_mark(df, my_str_df.values)  # task1

# task2: чтобы порекомендовать фильм для просмотра дома в выходной, будем вычислять так называемую "привлекательность"
# фильма. Участвовать в вычислениях будут только те фильмы, которые не посмотрел пользователь. Для вычислений я буду
# учитывать среднюю оценку фильма + процент посмотревших фильм дома + процент посмотревших его в выходной день
dict_task2 = recommend_film(res_task1)
res_task2 = {}
max_value = max(dict_task2.values())
res_task2[max(dict_task2, key = dict_task2.get)] = max_value

result = {"user": variant, "1": res_task1, "2": res_task2}
with open('result.json', 'w', encoding = 'utf-8') as f:
    json.dump(result, f, ensure_ascii = False, indent = 4)
