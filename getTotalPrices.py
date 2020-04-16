import csv
import os
from pprint import pprint

allCols = ['region', 'year', 'avg']

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


