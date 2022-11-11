import csv

clg_names = {}
branch = {}
#count = 0

with open('College_names.csv', 'r') as f:
	csvreader = csv.reader(f)
	for row in csvreader:
		code = int(row[0])
		clg_names[code] = row[1]

with open('course_dept_names.csv', 'r') as f2:
	csvreader = csv.reader(f2)
	for row in csvreader:
		d = row[0]
		#print(type(d))
		branch[d] = row[1]
		#print(type(row[1]))
		
while (True):
	print('\nEnter College Code:')
	test = int(input())
	print('Collge Name: ', clg_names.get(test))
	print('\nEnter Branch Code:')
	test2 = input()
	print('Branch Name: ', branch.get(test2))


