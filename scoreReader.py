import csv
file = open("saved", "r")
# data = file.readlines()

csvFile = csv.reader(file)

[
    ['bill', ' 0'], 
    ['bob', ' 220']
]



csvList = list(csvFile)


for line in csvList:
    print(line[0])
    print(line[1])


file.close()
