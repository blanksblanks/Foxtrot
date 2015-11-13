import csv

def parse_categories(filepath):
    with open(filepath, 'rb') as csvfile:
        categories = {}
        reader = csv.reader(csvfile)
        for row in reader:
            for item in row[2].split(', '):
                categories[item.lower()] = (row[0].lower(), row[1].lower())
        print categories
        return categories

parse_categories('data/category.csv')
