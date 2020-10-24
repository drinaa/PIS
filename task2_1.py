import numpy as np
import pandas as pd
import math
import json

sim_uv = []
rv = []
new_mark = {}
#высчитывает метрику для двух пользователей и сразу считает среднюю оценку (учитывая, что средняя оценка -
#это сумма всех проставленных оценок / на кол-во просмотренных фильмов(а не всех фильмов)
def sim(u, v):
    v_film = [] #список просмотренных фильмов
    sum, u_sum, v_sum, col, sum_uv = 0,0,0,0,0
    for i in range (30):
          if v[i] != -1:
            sum += v[i]
            col += 1
            if (u[i] != -1):
                sum_uv += (u[i] * v[i])
                u_sum += u[i] ** 2
                v_sum += v[i] ** 2
    return round(sum_uv/(math.sqrt(u_sum)*math.sqrt(v_sum)),3), round(sum/col, 3)

#высчитывает дробь из формулы оценки
def calc_mark (data, i):
    data.columns = ['mov', 'sim', 'rv']
    data['sum_ch'] = data.sim*(data.mov-data.rv)
    itog = sum(data.sum_ch)/sum(abs(data.sim))
    return itog


def recomend (data, my_str):
    data_num_colom = data.shape[1]
    data_num_str = data.shape[0]
    for i in range (data_num_str):
        v_df = list(data.iloc[i])
        ret = sim(my_str[0], v_df)
        sim_uv.append(ret[0])
        rv.append(ret[1])
    data2 = data.assign(sim=sim_uv, rv=rv)
    my_mean = data2.at['User 34','rv']
    data2 = data2.sort_values(by = ['sim'], ascending=False)
    data2 = data2.iloc[1:5]
    for i in range(data_num_colom):
        if my_str[0][i] == -1:
            new_mark['Movie ' + str(i+1)] = round(my_mean+calc_mark(data2.iloc[:,[i,-2,-1]],i),3)
    return new_mark




df = pd.read_csv('data.csv', index_col=0)
my_str_df = df.loc[df.index == 'User 34'] #выделяю свой вариант
ans = recomend(df,my_str_df.values) #task1
result = {"user": 34, "1": ans}
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

#task2 пока в разработке





