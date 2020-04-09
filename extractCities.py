import csv

datafile = open('totalAvocado.csv', 'r')

citySet = set([])

with open('totalAvocado_v2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        citySet.add(row[13])

citySet = list(citySet)
citySet.sort()
output = open('regionNames.txt', 'w')
for elem in citySet:
    output.write(elem)
    output.write('\n')

print(len(citySet))