import csv
import os
import pprint

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

# allCols = ['region', 'year', 'janP', 'febP', 'marP', 'aprP', 'mayP', 'junP', 'julP', 'augP', 'sepP', 'octP', 'novP', 'decP', 
#             'janV', 'febV', 'marV', 'aprV', 'mayV', 'junV', 'julV', 'augV', 'sepV', 'octV', 'novV', 'decV']

regionNames = ["Albany", "Atlanta", "Baltimore/Washington", "Boise", "Boston", "Buffalo/Rochester", 
        "Charlotte", "Chicago", "Cincinnati/Dayton", "Columbus", "Dallas/Ft. Worth", "Denver", "Detroit", 
        "Grand Rapids", "Harrisburg/Scranton", "Hartford/Springfield", "Houston", "Indianapolis", "Jacksonville", 
        "Las Vegas", "Los Angeles", "Louisville", "Miami/Ft. Lauderdale", "Nashville", "New Orleans/Mobile", 
        "New York", "Orlando", "Philadelphia", "Phoenix/Tucson", "Pittsburgh", "Portland", "Raleigh/Greensboro", 
        "Richmond/Norfolk", "Roanoke", "Sacramento", "San Diego", "San Francisco", "Seattle", "Spokane", "St. Louis",
         "Syracuse", "Tampa"]


pp = pprint.PrettyPrinter(indent=4)
keys = []
for (key, yearData) in raw.items():
    if (key[1] != '2015'):
        keys.append(key)    

keys.sort(key=lambda elem : elem[1])


region_prices_dict = {}

for key in keys:
    region_prices_dict[key[0]] = []

for key in keys:
    region_prices_dict[key[0]] += [elem[0] for elem in avg[key]]

pp.pprint(region_prices_dict)
# print(len(region_prices_dict['Albany']))



# keys.sort(key=lambda i)
# with open('avgAvocado.csv', 'w') as f:
#     f.write(','.join(allCols) + '\n')
#     for ((region, year), yearData) in avg.items():
        # f.write(f'{region},{year},{",".join(str(price) for (price, vol) in yearData)},{",".join(str(vol) for (price, vol) in yearData)}\n')

# pp.pprint(avg)

allCols = ['region', 'sixone', 'sixtwo', 'sixthree', 'sixfour', 'sixfive', 'sixsix', 'sixsev', 'sixeight', 'sixnine', 'sixten', 'sixelev', 'sixtwel',
             'sevone', 'sevtwo', 'sevthree', 'sevfour', 'sevfive', 'sevsix', 'sevsev', 'sixeight', 'sevnine', 'sevten', 'sevelev', 'sevtwel',
             'eightone', 'eighttwo', 'eightthree', 'eightfour', 'eightfive', 'eightsix', 'eightssevn', 'eighteight', 'eightnine', 'eightten', 'eightelev', 'eighttwel',
             'nine', 'ninetwo', 'ninethree', 'ninefour', 'ninefive', 'ninesix', 'ninessevn', 'nineeight', 'ninenine', 'nineten', 'nineelev', 'ninetwel']

print(len(allCols))
with open('pricepermonth.csv', 'w') as f:
    f.write(','.join(allCols) + '\n')
    for key, val in region_prices_dict.items():
        f.write(f'{key},{",".join([str(elem) for elem in val])}\n')

