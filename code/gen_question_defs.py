#This modules containes all functions related to generating questions

def gen_match_word(list_in):#list_in is list of [word,definition]
	from random import sample,randint;
	#pick 4 combinations at random
	pick_list = sample(list_in,4)#pick four combinations
	answer_idx = randint(0,3)# pick a word to question
	question_word = pick_list[answer_idx][0]
	def_list = []# retrieve definitions
	for ii in range(0,4):
		def_list.append(pick_list[ii][1])
	return [question_word,def_list,answer_idx]

def gen_match_def(list_in):#list_in is list of [word,definition]
	from random import sample,randint;
	#pick 4 combinations at random
	pick_list = sample(list_in,4)#pick four combinations
	answer_idx = randint(0,3)# pick a word to question
	question_def = pick_list[answer_idx][1]
	word_list = []# retrieve definitions
	for ii in range(0,4):
		word_list.append(pick_list[ii][0])
	return [question_def,word_list,answer_idx]
