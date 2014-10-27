import read_defs
# define test parameters
test_filename = "test_dat2.csv"
# test read_defs.read_csv with test data
print "test read_defs.read_csv with test data ...",
try:
	a= read_defs.read_csv("")
	print "success"
except:
	print "failed"
# test read_defs.read_csv with provided test data
print "test read_defs.read_csv with provided data ...",
try:
	read_defs.read_csv(test_filename)
	print "success"
except:
	print "failed"
