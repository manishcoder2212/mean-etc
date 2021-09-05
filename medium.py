import csv

with open('data1.csv', newline="") as f:
  reader = csv.reader(f)
  Height_Weight_data = list(reader)
  
Height_Weight_data.pop(0)
Height=[]
for c in range(len(Height_Weight_data)):
    Height.append(float(Height_Weight_data[c][1]))  

total_number_of_contents=len(Height)

Height.sort()
if total_number_of_contents % 2 == 0:
    #getting the first number
	median1 = float(Height[total_number_of_contents//2])
    #getting the second number
	median2 = float(Height[total_number_of_contents//2 - 1])
    #getting mean of those numbers
	median = (median1 + median2)/2
else:
	median = Height[total_number_of_contents//2]

print(median)