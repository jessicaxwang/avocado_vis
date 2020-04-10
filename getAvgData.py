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
            month = int(row[13])
            k = (region, year)
            if k not in raw:
                raw[k] = [[] for _ in range(12)]
            raw[k][month - 1].append(price)

avg = { region : [ round(sum(month) / len(month), 2) for month in year] for (region, year) in raw.items()}
allCols = ['region', 'year', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

with open('avgAvocado.csv', 'w') as f:
    f.write(','.join(allCols) + '\n')
    for ((region, year), yearData) in avg.items():
        f.write(f'{region},{year},{",".join(str(month) for month in yearData)}\n')
