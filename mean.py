import csv

with open('data1.csv', newline="") as f:
  reader = csv.reader(f)
  Height_Weight_data = list(reader)
  
Height_Weight_data.pop(0)
Height=[]
for c in range(len(Height_Weight_data)):
    Height.append(float(Height_Weight_data[c][1]))  

total_number_of_contents=len(Height)

sum_of_heights=0
for x in Height:
    sum_of_heights+=x

mean=sum_of_heights/total_number_of_contents
print(mean)