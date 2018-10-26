# -*- coding: latin-1 -*-

#	Parker King-Fournier
#	260556983

import io
import math
#_______________________MISC_______________________
def makeSet(data_string):
	letter_set = set([])
	for i in xrange(0, len(data_string)):
		if data_string[i] not in letter_set:
			letter_set.add(data_string[i])
	return letter_set

def getLanguageNumber(test_number):
	language_number = test_number
	if test_number == 5:
		language_number = 1
	if test_number == 6:
		language_number = 2
	return language_number

#___________________TESTS______________________
#0
def notSlovak(letter_set):
	not_slovak = set(['É','Ñ','á','à','ã','ä','å','ê','ï','ù','†','£','¢','§','¶','®','¨','Ø','Æ','µ','ª','æ','„','Á','Ê','È','Î','Ì','Ò','','Û','ı','Ù','˜','˘','¸'])
	if len(not_slovak&letter_set) > 0:
		return True
	else:
		return False
#
def notFrench(letter_set):
	not_french = set(['Æ'])
	if len(not_french&letter_set) > 0:
		return True
	else:
		return False
#2
def notSpanish(letter_set):
	not_spanish = set(['ä','å','Ø','æ'])
	if len(not_spanish&letter_set) > 0:
		return True
	else:
		return False
#3
def notGerman(letter_set):
	not_german = set(['É','Ñ','á','à','ã','ä','ç','å','è','ê','ù','†','•','¨','Ø','Æ','µ','¥','ª','º','æ','·','‰','Ê','È','Î','Ì','Ò','Û','ı','Ù','ˆ','¯','˝','¸'])
	if len(not_german&letter_set) > 0:
		return True
	else:
		return False
#4
def notPolish(letter_set):
	not_polish = set(['É','Ñ','á','à','ã','ä','ç','å','è','ê','ï','°','£','¢','•','®','Ø','Æ','µ','¥','ª','æ','Ê','Î','Ì','Ó','Ò','','ı','Ù','ˆ','¯','¸'])
	if len(not_polish&letter_set) > 0:
		return True
	else:
		return False
#5
def onlyFrench(letter_set):
	only_french = set(['ä','å','Ø','æ'])
	if len(only_french&letter_set) > 0:
		return True
	else:
		return False
#6
def onlySpanish(letter_set):
	only_spanish = set(['Æ'])
	if len(only_spanish&letter_set) > 0:
		return True
	else:
		return False


#___________________ENTROPY AND INFORMATION GAIN___________________

#calculate information gain for a test
def getInformationGain(data_list, true_list, false_list, language_number):
	if len(data_list) == 0:
		print 0
		return 0
	entropy = getEntropy(data_list)
	c1 = float(len(true_list))/len(data_list)
	c2 = float(len(false_list))/len(data_list)
	entropy_true = getEntropy(true_list)
	entropy_false = getEntropy(false_list)
	conditional_entropy = c1*entropy_true + c2*entropy_false
	information_gain = entropy - conditional_entropy
	print information_gain
	return information_gain

#calculate entropy for a binary test
def getEntropy(data_list):
	if len(data_list) == 0:
		return 0
	slovak = 0
	french = 0
	spanish = 0
	german = 0
	polish = 0
	for i in xrange(0, len(data_list)):
		if data_list[i][0] == 0:
			slovak = slovak + 1
		if data_list[i][0] == 1:
			french = french + 1
		if data_list[i][0] == 2:
			spanish = spanish + 1
		if data_list[i][0] == 3:
			german = german + 1
		if data_list[i][0] == 4:
			polish = polish + 1
	slovak = float(slovak)/len(data_list)
	french = float(french)/len(data_list)
	spanish = float(spanish)/len(data_list)
	german = float(german)/len(data_list)
	polish = float(polish)/len(data_list)
	if slovak == 0:
		slovak = 1
	if french == 0:
		french = 1
	if spanish == 0:
		spanish = 1
	if german == 0:
		german = 1 
	if polish == 0:
		polish = 1
	entropy = (-1)*slovak*math.log(slovak)/math.log(2) + (-1)*french*math.log(french)/math.log(2) + (-1)*spanish*math.log(spanish)/math.log(2) + (-1)*german*math.log(german)/math.log(2) + (-1)*polish*math.log(polish)/math.log(2)
	return entropy


#________________DECISION TREE________________
#build recursively with a limit called max_depth based on which test has the most information gain
#it should be noted that this will visit the nodes of the decisipon tree in POST ORDER traversal,
#assuming True lists are on the left
def makeTree(data_list, depth, max_depth):
	if(depth >= max_depth):
		return -2
		
	#make a list for the results of test 0
	true_list_0 = []
	false_list_0 = []
	language_number_0 = getLanguageNumber(0)
	#put the test examples into the right lists
	for i in xrange(0, len(data_list)):
		set_0 = makeSet(data_list[i][1])
		if notSlovak(set_0) == True:
			true_list_0.append(data_list[i])
		else:
			false_list_0.append(data_list[i])

	true_list_1 = []
	false_list_1 = []
	language_number_1 = getLanguageNumber(1)
	for i in xrange(0, len(data_list)):
		set_1 = makeSet(data_list[i][1])
		if notFrench(set_1) == True:
			true_list_1.append(data_list[i])
		else:
			false_list_1.append(data_list[i])

	true_list_2 = []
	false_list_2 = []
	language_number_2 = getLanguageNumber(2)
	for i in xrange(0, len(data_list)):
		set_2 = makeSet(data_list[i][1])
		if notSpanish(set_2) == True:
			true_list_2.append(data_list[i])
		else:
			false_list_2.append(data_list[i])

	true_list_3 = []
	false_list_3 = []
	language_number_3 = getLanguageNumber(3)
	for i in xrange(0, len(data_list)):
		set_3 = makeSet(data_list[i][1])
		if notGerman(set_3) == True:
			true_list_3.append(data_list[i])
		else:
			false_list_3.append(data_list[i])

	true_list_4 = []
	false_list_4 = []
	language_number_4 = getLanguageNumber(4)
	for i in xrange(0, len(data_list)):
		set_4 = makeSet(data_list[i][1])
		if notPolish(set_4) == True:
			true_list_4.append(data_list[i])
		else:
			false_list_4.append(data_list[i])

	true_list_5 = []
	false_list_5 = []
	language_number_5 = getLanguageNumber(5)
	for i in xrange(0, len(data_list)):
		set_5 = makeSet(data_list[i][1])
		if onlyFrench(set_5) == True:
			true_list_5.append(data_list[i])
		else:
			false_list_5.append(data_list[i])

	true_list_6 = []
	false_list_6 = []
	language_number_6 = getLanguageNumber(6)
	for i in xrange(0, len(data_list)):
		set_6 = makeSet(data_list[i][1])
		if onlySpanish(set_6) == True:
			true_list_6.append(data_list[i])
		else:
			false_list_6.append(data_list[i])

	#calculate the information gain for each test
	information_gain_0 = getInformationGain(data_list, true_list_0, false_list_0, language_number_0)
	information_gain_1 = getInformationGain(data_list, true_list_1, false_list_1, language_number_1)
	information_gain_2 = getInformationGain(data_list, true_list_2, false_list_2, language_number_2)	
	information_gain_3 = getInformationGain(data_list, true_list_3, false_list_3, language_number_3)
	information_gain_4 = getInformationGain(data_list, true_list_4, false_list_4, language_number_4)
	information_gain_5 = getInformationGain(data_list, true_list_5, false_list_5, language_number_5)
	information_gain_6 = getInformationGain(data_list, true_list_6, false_list_6, language_number_6)


	#put em all in a list to find the test with the highest information gain
	information_gain_list = [information_gain_0,information_gain_1,information_gain_2,information_gain_3,information_gain_4,information_gain_5,information_gain_6]
	max_information_gain = max(information_gain_list)

	# make a tree node that will have the form node = [parent_test, true_child_test, false_child_test]
	# initialized here with -1s to avoid confusion
	node = [-1,-1,-1]

	if max_information_gain == -1:
		return -1

	#recurse splitting based on the best test in terms of most information gain
	elif max_information_gain == information_gain_0:
		node[0] = 0

		node[1] = makeTree(true_list_0, depth+1, max_depth)
		node[2] = makeTree(false_list_0, depth+1, max_depth)

	elif max_information_gain == information_gain_1:
		node[0] = 1

		node[1] = makeTree(true_list_1, depth+1, max_depth)
		node[2] = makeTree(false_list_1, depth+1, max_depth)

	elif max_information_gain == information_gain_2:
		node[0] = 2

		node[1] = makeTree(true_list_2, depth+1, max_depth)
		node[2] = makeTree(false_list_2, depth+1, max_depth)

	elif max_information_gain == information_gain_3:
		node[0] = 3

		node[1] = makeTree(true_list_3, depth+1, max_depth)
		node[2] = makeTree(false_list_3, depth+1, max_depth)

	elif max_information_gain == information_gain_4:
		node[0] = 4

		node[1] = makeTree(true_list_4, depth+1, max_depth)
		node[2] = makeTree(false_list_4, depth+1, max_depth)

	elif max_information_gain == information_gain_5:
		node[0] = 5

		node[1] = makeTree(true_list_5, depth+1, max_depth)
		node[2] = makeTree(false_list_5, depth+1, max_depth)

	elif max_information_gain == information_gain_6:
		node[0] = 6

		node[1] = makeTree(true_list_6, depth+1, max_depth)
		node[2] = makeTree(false_list_6, depth+1, max_depth)

	return node

#____________________READFILES____________________
def readFile(file):
	data_list = []
	file = io.open('../datasets/training_data.csv', 'r', encoding='latin-1')
	training_data = file.readlines()
	for i in xrange(1, len(training_data)):
		line = training_data[i].split("\t")
		language_id = line[1]
		sentence_string = line[2].replace("\n", "").replace(" ", "").lower()
		data_list_entry = [language_id, sentence_string]
		data_list.append(data_list_entry)
	return data_list

#______________________MAIN______________________
def main():
	print "\nReading File...\n"
	data_list = readFile("../datasets/training_data.csv")
	print data_list

	print "Making Tree...\n"
	tree = makeTree(data_list, 0, 3)


main()