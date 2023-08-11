import bisect
import plotly.express as px
import numpy as np
import pandas as pd
from time import perf_counter_ns


def linear_search(list, item):
    found = False
    for i in range(len(list)):
        if list[i] == item:
            found = True
            return i
    if found == False:
        return i + 1


def search(list, step, algorithm):
    obs = []
    time = []
    result = []
    for observation in range(0, len(list), step):
        obs.append(observation)
        start = perf_counter_ns()
        if algorithm == "binary":
            bisect.bisect_left(list, observation)
        elif algorithm == "linear":
            linear_search(list, observation)
        else:
            break
        end = perf_counter_ns()
        time.append(end - start)
    mean = 0
    for t in time:
        mean += t
    result.append(obs)
    result.append(time)
    result.append(round(mean / len(time), 2))
    return result


ordered_list = [i for i in range(0, 10000000 + 1)]

binary = search(ordered_list, 1000000, "binary")
obs = binary[0]
binary_time = binary[1]
binary_mean = binary[2]

linear = search(ordered_list, 1000000, "linear")
linear_time = linear[1]
linear_mean = linear[2]

obs_strings = list(map(str, obs))

df = pd.DataFrame(
    {
        "Algoritmo": ["Busca Binaria"] * 11 + ["Busca Linear"] * 11,
        "Tempo": np.concatenate([binary_time, linear_time]),
        "Observação": np.concatenate([obs_strings, obs_strings]),
    }
)

fig = px.histogram(
    df,
    x="Observação",
    color="Algoritmo",
    y="Tempo",
    barmode="group",
    height=400,
    title="Tempo de execução: Busca Binária vs Busca Linear",
)
fig.show()

# scatterplot com step = 10000
binary = search(ordered_list, 10000, "binary")
obs = binary[0]
binary_time = binary[1]
binary_mean = binary[2]

print(binary_mean)
fig = px.scatter(
    x=binary_time,
    y=obs,
    color=obs,
    color_continuous_scale="bluered",
    title="Busca Binária (1000 amostras)",
)
fig.show()

linear = search(ordered_list, 10000, "linear")
linear_time = linear[1]
linear_mean = linear[2]

print(linear_mean)
fig = px.scatter(
    x=linear_time,
    y=obs,
    color=obs,
    color_continuous_scale="bluered",
    title="Busca Linear (1000 amostras)",
)
fig.show()

# scatterplot com step = 100
binary = search(ordered_list, 100, "binary")
obs = binary[0]
binary_time = binary[1]
binary_mean = binary[2]

print(binary_mean)
fig = px.scatter(
    x=binary_time,
    y=obs,
    color=obs,
    color_continuous_scale="bluered",
    title="Busca Binária (100.000 amostras)",
)
fig.show()

linear = search(ordered_list, 100, "linear")
linear_time = linear[1]
linear_mean = linear[2]

print(linear_mean)
fig = px.scatter(
    x=linear_time,
    y=obs,
    color=obs,
    color_continuous_scale="bluered",
    title="Busca Linear (100.000 amostras)",
)
fig.show()
