import csv
import os
from pprint import pprint

raw = {}
avg = {}

with open('totalAvocado_v5.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[13] != 'month':
            region = row[14]
            year = row[12]
            price = float(row[2])
            vol = float(row[3])
            month = int(row[13])
            k = (region, year)
            if k not in raw:
                raw[k] = [[[] for _ in range(2)] for _ in range(12)]
            raw[k][month - 1][0].append(price)
            raw[k][month - 1][1].append(vol)

avg = { key : [(round(sum(month[0]) / len(month[0]), 2), round(sum(month[1]) / len(month[1]), 2)) for month in yearData] for (key, yearData) in raw.items() }

allCols = ['region', 'year', 'janP', 'febP', 'marP', 'aprP', 'mayP', 'junP', 'julP', 'augP', 'sepP', 'octP', 'novP', 'decP', 
            'janV', 'febV', 'marV', 'aprV', 'mayV', 'junV', 'julV', 'augV', 'sepV', 'octV', 'novV', 'decV']

with open('avgAvocado.csv', 'w') as f:
    f.write(','.join(allCols) + '\n')
    for ((region, year), yearData) in avg.items():
        f.write(f'{region},{year},{",".join(str(price) for (price, vol) in yearData)},{",".join(str(vol) for (price, vol) in yearData)}\n')
