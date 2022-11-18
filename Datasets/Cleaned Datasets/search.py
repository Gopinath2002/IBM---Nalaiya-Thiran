import csv

csv_file_name = 'round_4.csv'
count = 0
clg = {}

with open(csv_file_name, 'r') as file:
	csvreader = csv.reader(file)
	for row in csvreader:
		if row[6] == '5' and row[7] == 'ST':
			print(row)

