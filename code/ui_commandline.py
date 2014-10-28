# kernel version of prcogramme
#import modules
import os
import ask_questions_defs as ask
clear_screen = lambda: os.system("clear");
#define constants
menu_items = ["onderdeel 1.1","kwaliteitsattributen begrip  naar definitie","kwaliteitsattritbuten definitie naar begrip"]
filename = "test_dat2.csv"
letter_list = ["a","b","c","d","e","f","g","h"]
		

# define exit condition
answer = ""
while answer!="exit":
	clear_screen();
	print "Type \"exit\" to quit programme"
	print "Select an option from the menu"
	for ii in range(0,len(menu_items)):
		print letter_list[ii]+") "+menu_items[ii]
	answer = raw_input("your input...")
	if answer=="a":
		#start match to word function
		ask.match_word_to_def("exam_spec_begrippen_11.csv")
	elif answer=="b":
		ask.match_word_to_def("kwaliteitsattributen_csv.csv")
	elif answer=="c":
		ask.match_def_to_word("kwaliteitsattributen_csv.csv")
print "Have a good day:)"
			 
			
