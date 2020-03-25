#!/usr/bin/env python
# coding: UTF-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

font = {
    'family': 'Liberation Sans',
    'serif': 'FreeSerif',
    'weight': 'bold',
    'size': 10
}

title_font = {
    'fontname': 'Roboto',
    'size': '18',
    'color': 'black',
    'fontweight': '3',
    'fontstyle': 'italic',
    'weight': 'bold',
    'verticalalignment': 'bottom'
}

plt.style.use('seaborn-deep')
plt.rc('font', **font)
plt.rc('figure', figsize=(11.69, 8.27))
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10


def annotation(x, y):
    for a, b in zip(x, y):
        label = '' if b == 0 else b
        plt.annotate(label,
                     (a, b),
                     textcoords="offset points",
                     xytext=(0, 1),
                     ha='center')


df = pd.read_csv('data/coronga-pr.csv')
max_number = df['Suspeitos'].max()

x = df['Data'].values
y1 = df['Suspeitos'].values
y2 = df['Confirmados'].values

fig, ax = plt.subplots()

ax.plot(x, y1, label='Suspeitos')
annotation(x, y1)

ax.plot(x, y2, label='Confirmados')
annotation(x, y2)

plt.title('Evolução do Coronavírus no Paraná', **title_font)
plt.legend()
plt.xlabel('Data')
plt.ylabel('Número de casos')
plt.yticks(np.arange(0, max_number, 500))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().xaxis.grid(True)
plt.tight_layout()
plt.savefig('figs/coronga-pr.png', dpi=300)
plt.clf()
