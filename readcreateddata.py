import csv
with open('stddata.csv','r',newline='') as file:
    read=csv.DictReader(file)
    for row in read:
        print(row['stdid'],row['name'])