import read_input
import write_output

US_infls = read_input.US_inf_rates()
min_wages = read_input.min_wages()
ref_year = read_input.ref_year()
years = list(min_wages.keys())



def purch_pow_for_ref_year():
	result = {}
	result[ref_year] = min_wages[ref_year]
	for year in range(ref_year, years[-1]):
		result[year+1] = result[year]*(1+US_infls[year]/100)
	for year in range(ref_year, years[0],-1):
		result[year-1] = result[year]/(1+US_infls[year-1]/100)
	return result

def purch_pow_diffs():
	diffs = {}
	purch_pows = purch_pow_for_ref_year()
	for year in min_wages.keys():
		if year == ref_year:
			continue
		diffs[year] = round(100*(min_wages[year]/purch_pows[year]-1),1)
	return diffs

pow_diffs = purch_pow_diffs()
write_output.create_output_file(ref_year, pow_diffs)