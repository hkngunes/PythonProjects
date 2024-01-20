
def create_output_file(ref_year, pow_diffs):
	result_file_name = "out/result_for_year_"+str(ref_year)+".txt"
	with open(result_file_name, 'w') as res_file:
		res_file.write("Ref Year:"+str(ref_year)+"\n\n"+
			"Year\tDiff\tResult\n\n")

	with open(result_file_name,'a') as res_file:
		for year in pow_diffs.keys():
			res = 'Low'
			if pow_diffs[year] > 0:
				res = 'High'
			res_file.write(str(year)+"\t"+str(pow_diffs[year])+"%\t"+res+"\n")