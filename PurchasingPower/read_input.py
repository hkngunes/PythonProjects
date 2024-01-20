import csv

def US_inf_rates():
	US_inflation_rates = {}
	with open('in/US_inflation_rates.csv','r') as f:
		csv_reader = csv.reader(f)
		for row in csv_reader:
			US_inflation_rates[int(row[0])] = float(row[1])

	return US_inflation_rates

def min_wages():
	minimum_wages = {}
	with open('in/minimum_wages.csv', 'r') as f:
		csv_reader = csv.reader(f)
		for row in csv_reader:
			minimum_wages[int(row[0])] = float(row[1])
	return minimum_wages

def ref_year():
	print("Give referance year: ")
	years = min_wages()
	year = 0
	while(year not in years.keys()):
		try:
			year = int(input())
		except:
			print("input can't cast to integer!")
	return year