import os

output = open('totalAvocado.csv', 'w')

file1 = open('avocado.csv', 'r')

for row in file1:
    output.write(row)

file1.close()

file2 = open('edited 2019 data.csv', 'r')

firstline = True
for row in file2:
    if firstline:
        firstline = False
        continue
    output.write(row)

output.close()
file2.close()