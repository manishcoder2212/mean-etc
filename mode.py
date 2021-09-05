import csv
import statistics

with open('data1.csv', newline="") as f:
  reader = csv.reader(f)
  Height_Weight_data = list(reader)
  
Height_Weight_data.pop(0)
Height=[]
for c in range(len(Height_Weight_data)):
    Height.append(float(Height_Weight_data[c][1]))  

mode=statistics.mode(Height)

print(mode)
