import csv

with open("CSVProjects/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)

import pandas

data = pandas.read_csv("CSVProjects/data/weather_data.csv")
print(data)

data = pandas.read_csv("CSVProjects/data/squirrel_data.csv")
color_data = data["Primary Fur Color"].value_counts()
color_data.to_csv("CSVProjects/data/color_data.csv")