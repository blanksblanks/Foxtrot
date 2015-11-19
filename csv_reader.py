import csv
from brand_size import BrandSize

# Read CSV file and make a dictionary.
def convertDict(fileName, key, value):
    with open(fileName, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        categoryDict = dict()
        for row in reader:
            categoryDict[row[key]]=row[value]
        print categoryDict
        return categoryDict

category = convertDict("data/category.csv", 'Category ID', 'Category Description')
brand = convertDict("data/brand.csv", "BrandID", "Brand Name")

with open('data/brandsizes.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    categoryDict = dict()
    count = 0
    for row in reader:
        if count is 20:
            break
        item = row
        count += 1
        item['BrandName'] = brand[(item['BrandID'])]
        item['CategoryName'] = category[(row['CategoryID'])]
        print item
        print BrandSize(item)
