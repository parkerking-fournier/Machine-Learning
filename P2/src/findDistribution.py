import math


#Read in the files into a list of a list of each languages comments
def readFiles(train_set_x, train_set_y):
	
	#Read in the files
	file1 = open(train_set_x, "r")
	file2 = open(train_set_y, "r")
	data = file1.readlines()
	data_labels = file2.readlines()

	slovak_list = []
	french_list = []
	spanish_list = []
	german_list = []
	polish_list = []

	for i in xrange(1,len(data)):

		#remove surrounding white spaces, split at comma, take the second entry, take out all spaces, turn to lowercase
		training_sentence = data[i].strip().split(",")[1].replace(" ", "").lower()
		#take the row, split at the comma, take the first element and cast to int
		training_label = int(data_labels[i].split(",")[0])

		#add a conversation to the relevant language list
		if training_label == 0:
			slovak_list.append(training_sentence)
		elif training_label == 1:
			french_list.append(training_sentence)
		elif training_label == 2:
			spanish_list.append(training_sentence)			
		elif training_label == 3:
			german_list.append(training_sentence)		
		elif training_label == 4:
			polish_list.append(training_sentence)		

	language_list = [slovak_list, french_list, spanish_list, german_list, polish_list]
	return language_list


#find the distribution of each character for each language
def characterCount(language_list):

	slovak_char_count = [[]]
	french_char_count = [[]]
	spanish_char_count = [[]]
	german_char_count = [[]]
	polish_char_count = [[]]

	#go through slovak, french, etc
	for i in xrange(0, len(language_list)):

		#for each language go through each of their new stripped comment
		language = language_list[i]	
		for j in xrange(0, len(langauge)):

			#for each comment look through all characters
			comment = language[j]
			for k in xrange(0, len(comment)):
				
				character = comment[k];

				if i == 0:
					slovak_char_count = updateCount(character, slovak_char_count)
				elif i == 1:
					french_char_count = updateCount(character, french_char_count)	
				elif i == 2:
					spanish_char_count = updateCount(character, spanish_char_count)
				elif i == 3:
					german_char_count = updateCount(character, german_char_count)					
				elif i == 4:
					polish_char_count = updateCount(character, polish_char_count)

	#make a cohesive list of all distributions and return it
	char_count_list = [slovak_char_count, french_char_count, spanish_char_count, german_char_count, polish_char_count]
	return char_count_list


#when a new character is found for a language, update the distribution
def updateCount(character, char_count):

	#set a dummy value for index
	index = -1

	#look to see if the character is already in the distribution, if you find it, keep the index
	for i in xrange(0,len(distribution)):
		if char_count[i][0] == character:
			index = i

	#if it wasnt in the distribution, add it to the end with an occurrence of 1
	if index == -1:
		char_count.append([character,1])
	#if it was in the distribution, increase the occurrence number of that variable by 1
	else:
		char_count[index][1] += 1

	#return the new modified distribution
	return char_count

#takes a single character count for ONE language and turns it into a probability distribution
def makeDistribution(char_count):

	#set dummy total
	total = -1

	#Get the total number of characters
	for i in xrange(0,len(char_count)):
		total += char_count[i][1]
	#divide each of the character occurences by this total
	for i in xrange(0,len(char_count)):
		char_count[i][0] = float(char_count[i][0])/float(total)

	return char_count


#______________________________MAIN_________________________________
#file names for training data
train_set_x = "../datasets/train_set_x.csv"
train_set_y = "../datasets/train_set_y.csv"

#read files, then count all the characters present in each langauge
language_list = readFiles(train_set_x, train_set_y)
char_count_list = characterCount(language_list)

#make distributions from the character counts for each language
distribution_list = []
for i in xrange(0,len(char_count_list)):

	char_count = char_count_list[i]
	distribution_list.append(makeDistribution(char_count)
	















