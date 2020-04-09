import csv

datafile = open('totalAvocado.csv', 'r')
outputfile = open('totalAvocado_v2.csv', 'w')


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
    }
    return switcher.get(arg, arg)


with open('totalAvocado.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        
        if row[13] == 'region':
            continue
        elif row[13] == 'West':
            continue
        else:
            row[13] = cityNames(row[13])

            outputfile.write(','.join(row))
            outputfile.write('\n')