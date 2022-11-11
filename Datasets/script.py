import csv

#print('Enter file name:')
csv_file_name = 'ACADEMIC_ROUND4.csv'
res_file_name = 'round_4.csv'
count = 0

def write_to_csv(data):
	with open (res_file_name, 'a+') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(data)

with open(csv_file_name, 'r') as file:
	csvreader = csv.reader(file)
	
	header = next(csvreader)
	#print (header)
	write_to_csv(header)
	
	for row in csvreader:
		val = row[0]
		if val != header[0]:
			write_to_csv(row)
			count += 1
	
file.close()
#print ('\n Count: ',count)

