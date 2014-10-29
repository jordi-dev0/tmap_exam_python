import read_defs as r
import gen_question_defs as q
import ask_questions_defs as a
import sys
# define test parameters
test_filename = "test_dat2.csv"
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


