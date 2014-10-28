import os
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
			print "Welk begrip hoort bij de volgede definitie: "
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

