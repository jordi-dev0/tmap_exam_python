import os
from sys import platform
if platform.startswith('win32'):
	clear_screen = lambda: os.system("cls");
elif platform.startswith('linux'):
	clear_screen = lambda: os.system("clear");
letter_list = ["a","b","c","d","e","f","g","h"]
#functions
def match_word_to_def(f_name):
	import read_defs as r
	import gen_question_defs as q
	answer = ""
	while answer!="exit":
		res = q.gen_match_word(r.read_csv(f_name)[1])
		answer_validity = False
		while not answer_validity:
			clear_screen()
			print "Enter exit to quit"
			print ""
			print "Wat betekent: "+res[0]+" ?"
			print ""
			for d in range(0,4):
				print letter_list[d]+") "+res[1][d]
				print ""
			answer = raw_input("your answer: ")
			if answer in ["a","b","c","d","exit"]:
				answer_validity = True
				if answer=="a":
					answer = 0
				elif answer=="b":
					answer = 1
				elif answer=="c":
					answer = 2
				elif answer=="d":
					answer = 3
				elif answer=="exit":
					break
				if answer==res[2]:
					print "Correct!"
					print "Press enter to continue..."
					answer = raw_input()
				else:
					print "Incorrect!"
					print "Press enter to continue..."
					answer = raw_input()

			else:
				print "please insert valid input"
				print "press enter"
				raw_input()
def match_def_to_word(f_name):
	import read_defs as r
	import gen_question_defs as q
	answer = ""
	while answer!="exit":
		res = q.gen_match_def(r.read_csv(f_name)[1])
		answer_validity = False
		while not answer_validity:
			clear_screen()
			print "Enter exit to quit"
			print ""
			print "Welk begrip hoort bij de volgende definitie: "
			print res[0]
			print ""
			for d in range(0,4):
				print letter_list[d]+") "+res[1][d]
			answer = raw_input("your answer: ")
			if answer in ["a","b","c","d","exit"]:
				answer_validity = True
				if answer=="a":
					answer = 0
				elif answer=="b":
					answer = 1
				elif answer=="c":
					answer = 2
				elif answer=="d":
					answer = 3
				elif answer=="exit":
					break
				if answer==res[2]:
					print "Correct!"
					print "Press enter to continue..."
					answer = raw_input()
				else:
					print "Incorrect!"
					print "Press enter to continue..."
					answer = raw_input()

			else:
				print "please insert valid input"
				print "press enter"
				raw_input()

#match item to heading
def match_lists(f_name,str_choice):
	import read_defs as r
	import gen_question_defs as q
	from random import randint
	answer = ""
	while answer!="exit":
		if str_choice=="heading":
			res = q.gen_match_heading_to_item(r.read_csv_of_lists(f_name))
		elif str_choice=="item":
			res = q.gen_match_item_to_heading(r.read_csv_of_lists(f_name))
		else:
			if randint(0,1)==0:
				res = q.gen_match_heading_to_item(r.read_csv_of_lists(f_name))
			else:
				res = q.gen_match_item_to_heading(r.read_csv_of_lists(f_name))

		answer_validity = False
		while not answer_validity:
			clear_screen()
			print "Enter exit to quit"
			print ""
			print "Wat hoort bij: "
			print res[0]
			print ""
			for d in range(0,4):
				print letter_list[d]+") "+res[1][d]
			answer = raw_input("your answer: ")
			if answer in ["a","b","c","d","exit"]:
				answer_validity = True
				if answer=="a":
					answer = 0
				elif answer=="b":
					answer = 1
				elif answer=="c":
					answer = 2
				elif answer=="d":
					answer = 3
				elif answer=="exit":
					break
				if answer==res[2]:
					print "Correct!"
					print "Press enter to continue..."
					answer = raw_input()
				else:
					print "Incorrect!"
					print "Press enter to continue..."
					answer = raw_input()

			else:
				print "please insert valid input"
				print "press enter"
				raw_input()

def match_word(f_name,str_choice):
	import read_defs as r
	import gen_question_defs as q
	from random import randint
	answer = ""
	while answer!="exit":
		if str_choice=="word":
			res = q.gen_match_word(r.read_csv(f_name)[1])
		elif str_choice=="def":
			res = q.gen_match_def(r.read_csv(f_name)[1])
		else:
			if randint(0,1)==0:
				res  =q.gen_match_word(r.read_csv(f_name)[1])
			else:
				res = q.gen_match_def(r.read_csv(f_name)[1])
		answer_validity = False
		while not answer_validity:
			clear_screen()
			print "Enter exit to quit"
			print ""
			print "Wat hoort bij:"
			print res[0]+" ?"
			print ""
			for d in range(0,4):
				print letter_list[d]+") "+res[1][d]
			answer = raw_input("your answer: ")
			if answer in ["a","b","c","d","exit"]:
				answer_validity = True
				if answer=="a":
					answer = 0
				elif answer=="b":
					answer = 1
				elif answer=="c":
					answer = 2
				elif answer=="d":
					answer = 3
				elif answer=="exit":
					break
				if answer==res[2]:
					print "Correct!"
					print "Press enter to continue..."
					answer = raw_input()
				else:
					print "Incorrect!"
					print "Press enter to continue..."
					answer = raw_input()

			else:
				print "please insert valid input"
				print "press enter"
				raw_input()
