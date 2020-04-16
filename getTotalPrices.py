import csv
import os
from pprint import pprint


raw = {}
avg = {}

with open('totalAvocado_v5.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[2] != 'AveragePrice':
            region = row[14]
            year = row[12]
            price = float(row[2])
            k = (region, year)
            if k not in raw:
                raw[k] = []
            raw[k].append(price)

avg = { k : round(sum(v) / len(v), 2) for (k, v) in raw.items()}

allCols = ['region', 'year', 'avg']
with open('avgTotals.csv', 'w') as f:
    f.write(','.join(allCols) + '\n')
    for ((region, year), yearData) in avg.items():
        f.write(f'{region},{year},{yearData}\n')
