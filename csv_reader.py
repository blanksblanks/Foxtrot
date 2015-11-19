import csv


# Read CSV file and make a dictionary.  
def convertDict(fileName, key, value): 
    with open(fileName, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        categoryDict = dict()
        for row in reader:
            categoryDict[row[key]]=row[value]
        print categoryDict
        return;

category = convertDict("data/category.csv", 'Category ID', 'Category Description')
brand = convertDict("data/brand.csv", "BrandID", "Brand Name") 


