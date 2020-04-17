import csv
import os
from pprint import pprint

raw = {} # (Albany, 2019): [[],[]]
avg = {} # (Albany, 2019): (avgPrice, avgVol)

with open('totalAvocado_v5.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[2] != 'AveragePrice':
            region = row[14]
            year = row[12]
            price = float(row[2])
            volume = float(row[3])
            k = (region, year)
            if k not in raw:
                raw[k] = [[] for _ in range(2)]
            raw[k][0].append(price)
            raw[k][1].append(volume)

avg = { k : (round(sum(prices) / len(prices), 2), round(sum(vol), 2))for (k, (prices, vol)) in raw.items()}

allCols = ['region', 'year', 'avg', 'totalVol']
with open('avgTotals.csv', 'w') as f:
    f.write(','.join(allCols) + '\n')
    for ((region, year), (prices, vol)) in avg.items():
        f.write(f'{region},{year},{prices},{vol}\n')
