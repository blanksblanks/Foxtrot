import csv

with open('data/category.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    categoryDict = dict()
    for row in reader:
        categoryDict[row['Category Name']]=row['Category Description']
    print categoryDict
        #print(row['Category Name'])
