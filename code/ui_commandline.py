# kernel version of prcogramme
#import modules
from sys import platform
import os
import ask_questions_defs as ask
if platform.startswith("win32"):
	clear_screen = lambda: os.system("cls");
elif platform.startswith("linux"):
	clear_screen = lambda: os.system("clear");

#define constants
menu_items = ["onderdeel 1.1","kwaliteitsattributen begrip  naar definitie","begrippen testtools","deelfasen faseringsmodel"]
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
		ask.match_word("exam_spec_begrippen_11.csv","random")
	elif answer=="b":
		ask.match_word("kwaliteitsattributen_csv.csv","random")
	elif answer=="c":
		ask.match_word("test_tools.csv","random")
	elif answer=="d":
		ask.match_lists("deelfasen_lijst.csv","random")
print "Have a good day:)"
			 
			
