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

def gen_match_item_to_heading(list_in):
#list in is [[headings],[[heading1_item1,heading1_item1,...],[heading2_item2,....]]]
	from random import sample, randint
	pick_list = sample(range(0,len(list_in[0])),4)# pick 4 headings
	items_list = [];
	headings_list = [];
	tmp_list = []
	for ii in pick_list:#pick a item for each heading
		headings_list.append(list_in[0][ii])# extract heading
		tmp_list = list_in[1][ii]# extract items for this heading
		items_list.append(tmp_list[randint(0,len(tmp_list)-1)])
	answer_idx = randint(0,3)
	return [items_list[answer_idx],headings_list,answer_idx]

def gen_match_heading_to_item(list_in):
#list in is [[headings],[[heading1_item1,heading1_item1,...],[heading2_item2,....]]]
	from random import sample, randint
	pick_list = sample(range(0,len(list_in[0])),4)# pick 4 headings
	items_list = [];
	headings_list = [];
	tmp_list = []
	for ii in pick_list:#pick a item for each heading
		headings_list.append(list_in[0][ii])# extract heading
		tmp_list = list_in[1][ii]# extract items for this heading
		items_list.append(tmp_list[randint(0,len(tmp_list)-1)])
	answer_idx = randint(0,3)
	return [headings_list[answer_idx],items_list,answer_idx]

