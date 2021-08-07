import csv

all_articles = []

with open("data/articles_data.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []
