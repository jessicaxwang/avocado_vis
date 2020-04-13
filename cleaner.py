import os
import csv

class Cleaner():
    
    def aggregate(self, input1, input2, output):
        output = open(output, 'w')

        file1 = open(input1, 'r')

        for row in file1:
            output.write(row)

        file1.close()

        file2 = open(input2, 'r')

        firstline = True
        for row in file2:
            if firstline:
                firstline = False
                continue
            output.write(row)

        output.close()
        file2.close()

    def cleanData(self, input1, output):

        outputfile = open(output, 'w')

        def cityNames(arg):
            switcher = {
                "BaltimoreWashington": "Baltimore/Washington",
                "BuffaloRochester": "Buffalo/Rochester",
                "CincinnatiDayton": "Cincinnati/Dayton",
                "DallasFtWorth": "Dallas/Ft. Worth",
                "GrandRapids": "Grand Rapids",
                "GreatLakes": "Great Lakes",
                "HarrisburgScranton": "Harrisburg/Scranton",
                "HartfordSpringfield": "Hartford/Springfield",
                "LasVegas": "Las Vegas",
                "LosAngeles": "Los Angeles",
                "MiamiFtLauderdale": "Miami/Ft. Lauderdale",
                "NewOrleansMobile": "New Orleans/Mobile",
                "NewYork": "New York",
                "NorthernNewEngland": "Northern New England",
                "PhoenixTucson": "Phoenix/Tucson",
                "RaleighGreensboro": "Raleigh/Greensboro",
                "RichmondNorfolk": "Richmond/Norfolk",
                "SanDiego": "San Diego",
                "SanFrancisco": "San Francisco",
                "SouthCarolina": "South Carolina",
                "SouthCentral": "South Central",
                "StLouis": "St. Louis",
                "TotalUS": "Total U.S.",
                "WestTexNewMexico": "West Tex/New Mexico",
                "West Tex/New Mexico1": "West Tex/New Mexico" 
            }
            return switcher.get(arg, arg)

        def keep(test, bad_array):
            return test in bad_array


        with open(input1, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:

                if not (keep(row[13], ['region', 'West', 'California', 'Great Lakes', 'Midsouth', 'Northeast', \
                                    'Northern New England', 'Plains', 'South Carolina', 'South Central', 'Southeast', 'West Tex/New Mexico'])):
                    row[13] = cityNames(row[13])

                    outputfile.write(','.join(row))
                    outputfile.write('\n')
    
    def extractCities(self, input1):
        citySet = set([])

        with open(input1, 'r') as csvfile:
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


cleaner = Cleaner()
# cleaner.extractCities('totalAvocado.csv')
# cleaner.cleanData('totalAvocado.csv', 'totalAvocado_v2.csv')
# cleaner.extractCities('totalAvocado_v2.csv')
# cleaner.aggregate('edited 2018 data.csv', 'totalAvocado_v2.csv', 'totalAvocado_v3.csv')
# cleaner.extractCities('totalAvocado_v3.csv')
# cleaner.cleanData('totalAvocado_v3.csv', 'totalAvocado_v4.csv')
cleaner.extractCities('totalAvocado_v4.csv')
cleaner.cleanData('totalAvocado_v4.csv', 'totalAvocado_v5.csv')
cleaner.extractCities('totalAvocado_v5.csv')