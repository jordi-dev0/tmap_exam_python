import read_defs as r
import gen_question_defs as q
import sys
# define test parameters
test_filename = "test_dat2.csv"
test_filename_list = "test_dat4.csv"
test_list = [["w1","d1"],["w2","d2"],["w3","d3"],["w4","d4"],["w5","d5"],["w6","d6"]]

# test read_defs.read_csv with test data
print "test read_csv with test data ...",
try:
	r.read_csv("")
	print "success"
except:
	print "failed"

# test read_defs.read_csv with provided test data
print "test read_csv with provided data ...",
try:
	r.read_csv(test_filename)
	print "success"
except:
	print "failed"

# test read_defs.read_csv_list_of_items with provided test data
print "test read_csv_list_of_items with provided data ...",
try:
	r.read_csv_of_lists(test_filename_list)
	print "success"
except:
	print "failed"


# test gen_match_word with test data
print "test gen_match_word with test data ...",
try:
	q.gen_match_word(test_list)
	print "success"
except:
	print "failed"

# test gen_match_word with provided data
print "test gen_match_word with provided data ...",
try:
	q.gen_match_word(r.read_csv(test_filename)[1])
	print "success"
except:
	print "failed"

# test gen_match_def with test data
print "test gen_match_def with test data ...",
try:
	q.gen_match_def(test_list)
	print "success"
except:
	print "failed"

# test gen_match_def with provided data
print "test gen_match_def with provided data ...",
try:
	q.gen_match_def(r.read_csv(test_filename)[1])
	print "success"
except:
	print "failed"

# test gen_match_item to heading with provided data
print "test gen_match_item_to_heading with provided data ...",
try:
	q.gen_match_item_to_heading(r.read_csv_of_lists(test_filename_list))
	print "success"
except:
	print "failed"

# test gen_match_heading to item with provided data
print "test gen_match_heading_to_item with provided data ...",
try:
	q.gen_match_heading_to_item(r.read_csv_of_lists(test_filename_list))
	print "success"
except:
	print "failed"

