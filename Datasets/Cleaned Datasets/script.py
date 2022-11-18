import csv

csv_file_name = 'round_4.csv'
count = 0
clg = {}

with open(csv_file_name, 'r') as file:
	csvreader = csv.reader(file)
	header = next(csvreader)
	for row in csvreader:
		try:
			temp = int(row[4])
		except:
			count += 1
			clg[row[6]] += 1 
			print (row)



for i, j in clg.items():
	print (i, j)
