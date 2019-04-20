import pandas as pd
import numpy as np


df = pd.read_csv('F:\\web development\\Minor Project\\hello.csv')


def returncities(a):
    m = list()
    pt = list()
    lr = list()
    tg = list()

    for i in a:
        m.append(df.loc[df['name_of_city'] == i, 'sample_mean'].iloc[0])
        pt.append(df.loc[df['name_of_city'] == i, 'population_total'].iloc[0])
        lr.append(df.loc[df['name_of_city'] == i, 'effective_literacy_rate_total'].iloc[0])
        tg.append(df.loc[df['name_of_city'] == i, 'total_graduates'].iloc[0])

    m = np.mean(m)
    pt = np.mean(pt)
    lr = np.mean(lr)
    tg = np.mean(tg)

    filter1 = df['sample_mean'] > m - 0.08
    filter2 = df['sample_mean'] < m + 0.08
    filter3 = df['population_total'] > pt - 0.03
    filter4 = df['population_total'] < pt + 0.03
    filter5 = df['effective_literacy_rate_total'] > lr - 0.005
    filter6 = df['effective_literacy_rate_total'] < lr + 0.005
    filter7 = df['total_graduates'] > tg - 0.01
    filter8 = df['total_graduates'] < tg + 0.01



    d = df['name_of_city'].where(filter1 & filter2 | filter3 & filter4 | filter5 & filter6 | filter7 & filter8)
    d = d.dropna()
    d = list(d)
    d = [i.strip() for i in d]
    print(len(d))

    return d
