import matplotlib.pyplot as mp
import csv
fileName = input("Enter a file name (must be within this folder and of valid syntax, or the program will hang)\n")
rowNum = int(input("Enter the number your data is stored on\n"))
data = [0]
with open (fileName, "r") as file:
    dataA = csv.reader(file)
    next(dataA)
    for i in dataA:
        data.append(int(i[rowNum]))
mp.plot(data)
mp.show()
