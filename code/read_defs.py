#from os import getcwd 
#from csv import reader
def read_csv(str_in):# reads data from file and returns list 
# output has format list = [ [headings],[ values_par_1, values_par_2, ...]]
	list_out = [];
	from os import getcwd
	from csv import reader
#load data file name, if not provided load standard data file name
	if str_in=="":
		data_file_name = "test_dat2.csv"; 
	else:
		data_file_name = str_in;
# get path to data folder 
	current_dir = getcwd();
	data_dir = current_dir[:len(current_dir)-4]
	data_dir = data_dir+"data/"+data_file_name;
	try:
		row_counter = 0;
		headings = [];
		list_val = [];
		with open(data_dir,'rb') as f:
			rdr = reader(f)
			for row in rdr:
				#extract headings, SHOULD THIS BE OPTIONAL?
				if row_counter==0:
					headings = row;
				else:
					list_val.append(row)
				row_counter +=1;
		return [headings,list_val]
	except IOError:
		print "ERROR READING FROM "+data_dir
		print "PROBABLY A BAD FILE NAME, DUMMY!"
		raise

if __name__=="__main__":
	import sys
	read_csv(sys.argv[1])	
