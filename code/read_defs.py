#from os import getcwd 
#from csv import reader

def remove_empty_items(list_in):
	try:
		while True:
			list_in.remove("");
	except:
		return list_in

def read_csv(str_in):# reads data from file and returns list 
# output has format list = [ [headings],[ values_par_1, values_par_2, ...]]
	from os import getcwd
	from csv import reader
	#load data file name, if not provided load standard data file name
	if str_in=="":#if file name is empty string
		data_file_name = "test_dat2.csv"; 
	else:# if file name is provided
		data_file_name = str_in;
	# get path to data folder 
	current_dir = getcwd();
	data_dir = current_dir[:len(current_dir)-4]
	data_dir = data_dir+"data/"+data_file_name;
	try:
		# assuming the first row in the .csv file are the headings
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
	except IOError:# if reading .csv filed failed
		print "ERROR READING FROM "+data_dir
		print "PROBABLY A BAD FILE NAME, DUMMY!"
		raise

def read_csv_of_lists(str_in):# reads data from file and returns list 
# output has format list = [ [headings],[ values_par_1, values_par_2, ...]]
	from os import getcwd
	from csv import reader
	#load data file name, if not provided load standard data file name
	if str_in=="":#if file name is empty string
		data_file_name = "test_dat4.csv"; 
	else:# if file name is provided
		data_file_name = str_in;
	# get path to data folder 
	current_dir = getcwd();
	data_dir = current_dir[:len(current_dir)-4]
	data_dir = data_dir+"data/"+data_file_name;
	try:
		# assuming the first row in the .csv file are the headings
		headings = [];
		list_val = [];
		with open(data_dir,'rb') as f:
			rdr = reader(f)
			for row in rdr:
				#extract headings, SHOULD THIS BE OPTIONAL?
				headings.append(row[0]);
				list_val.append(remove_empty_items(row[1:]))
		return [headings,list_val]
	except IOError:# if reading .csv filed failed
		print "ERROR READING FROM "+data_dir
		print "PROBABLY A BAD FILE NAME, DUMMY!"
		raise



if __name__=="__main__":
	import sys
	read_csv(sys.argv[1])	
