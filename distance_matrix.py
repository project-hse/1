import googlemaps
import csv
import pandas as pd

list0 = []
list1 = []
list2 = []
list3 = []
with open("Output1.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
        if lines[0] != 'City 1':
            list0.append(lines[0])
with open("Output1.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
        if lines[1] != 'City 2':
            list1.append(lines[1])
with open("Output1.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
        if lines[2] != 'Graph':
            list2.append(lines[2])


for i, j in zip(list0, list1):
    gmaps = googlemaps.Client(key='AIzaSyB1OUZUeW1mWl6kIssk2yLM8e3Rqb0ON1s')


    result = gmaps.directions(i, j, mode = "driving", avoid = None, departure_time = None)
    result1 = (result[0]['legs'][0]['distance']['text'])
    list3.append(result1)
print(list3)
data = dict(City1=list0, City2=list1, Graph=list2, Google=list3)
df = pd.DataFrame(data)
df.to_csv(r'Final.csv', sep=',', index=False)
