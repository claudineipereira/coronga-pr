#!/usr/bin/env python
# coding: UTF-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

today = date.today().strftime('%d/%m')

ir2019 = 2328
ir_today = 2182

p2019 = 3287
p_today = 3350

font = {
    'family': 'Liberation Sans',
    'serif': 'FreeSerif',
    # 'weight': 'bold',
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


def annotation(x, y, *m):
    for a, b in zip(x, y):
        if m:
            label = '' if b < m else b
        else:
            label = '' if b == 0 else b
        plt.annotate(label,
                     (a, b),
                     textcoords="offset points",
                     xytext=(0, 10),
                     ha='center')


df = pd.read_csv('data/coronga-pr.csv')
max_number = df['Confirmados'].max()
# df['Diff'] = df['Confirmados'].diff().fillna(0).astype(int)

x = df['Data'].values
y1 = df['Confirmados'].values
y2 = df['Óbitos'].values
# y3 = df['Diff'].values

fig, ax = plt.subplots()

ax.plot(x, y1, marker='o', label='Confirmados')
annotation(x, y1, max_number)

ax.bar(x, y2, color='red', label='Óbitos')
annotation(x, y2)

# ax.plot(x, y3, marker='o', label='Diferença')
# annotation(x, y3)

plt.text(3, 1150, 'Mortes por Insufiência Respiratória', fontsize=12, weight='bold')
plt.text(4, 1100, 'No ano de 2019: ', fontsize=12)
plt.text(11, 1100, '%d' % (ir2019), fontsize=11, weight='bold')
plt.text(4, 1050, '01 Jan. a %s:' % (today), fontsize=12)
plt.text(11, 1050, '%d' % (ir_today), fontsize=11, weight='bold')

plt.text(3, 950, 'Mortes por Pneumonia', fontsize=12, weight='bold')
plt.text(4, 900, 'No ano de 2019: ', fontsize=12)
plt.text(11, 900, '%d' % (p2019), fontsize=11, weight='bold')
plt.text(4, 850, '01 Jan. a %s:' % (today), fontsize=12)
plt.text(11, 850, '%d' % (p_today), fontsize=11, weight='bold')

plt.title('Evolução do Coronavírus no Paraná', **title_font)
plt.legend(loc='upper left')
plt.xlabel('Data')
plt.ylabel('Número de casos')
plt.xticks(rotation=90)
plt.yticks(np.arange(0, max_number, 200))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().yaxis.grid(True)
plt.tight_layout()
plt.savefig('figs/coronga-pr.png', dpi=300)
plt.clf()
