import math
import math


#________________________ENTROPY________________________
def findEntropy(language, language_classes):
	pos_percent = 0
	total_data = len(language_classes)-2

	for i in xrange(1,len(language_classes)):

	
		lang_id = float(language_classes[i].strip().split(",")[1])

		if(lang_id == language):
			pos_percent +=1

	pos_percent /= float(total_data)
	neg_percent = 1 - pos_percent

	entropy = (-1)*pos_percent*(math.log(pos_percent)/math.log(2)) + (-1)*neg_percent*(math.log(neg_percent)/math.log(2))

	return entropy

#________________________LANGUAGE DISTRIBUTION________________________
def findDistribution(language_classes):
	slovak_percent = 0.0
	french_percent = 0.0
	spanish_percent = 0.0
	german_percent = 0.0
	polish_percent = 0.0

	total_data = len(language_classes)-2

	#Calculate the percentages of each language in the data set.
	#first take the totals then divide each by the total number of data points
	for i in xrange(1,len(language_classes)):

		#for each line strip the line, split it at the comma
		#and find the language_id # for each instance
		lang_id = float(language_classes[i].strip().split(",")[1])
	
		#increment language counts accordingly
		if lang_id == 0:
			slovak_percent += 1
		elif lang_id == 1:
			french_percent += 1
		elif lang_id == 2:
			spanish_percent += 1
		elif lang_id == 3:
			german_percent += 1
		elif lang_id == 4:
			polish_percent += 1

	slovak_percent /= total_data
	french_percent /= total_data
	spanish_percent /= total_data
	german_percent /= total_data
	polish_percent /= total_data

	print slovak_percent 
	print french_percent 
	print spanish_percent 
	print german_percent 
	print polish_percent 



#________________________Finding the best 1-gram________________________
def bestOneGram(comments, language_classes):

	best_gram = ""
	best_entropy = 0.0

	#get total entropy
	total_entropy = findEntropy(1, language_classes)

	#iterate through all letters
	from string import ascii_lowercase
	for character in ascii_lowercase:

		#Counters
		positive_french = 0
		positive_other = 0
		negative_french = 0
		negative_other = 0

		gram = character
		print gram
		#look at every comment to see if it has that character
		for i in xrange(1,len(comments)):

			#strip the comment into no spaces all lowecase
			comment = comments[i].strip().split(",")[1].replace(" ", "").lower()

			#increment the right counters
			if gram in comment:
				if(int(language_classes[i].strip().split(",")[1]) == 1):
					positive_french += 1
				else:
					positive_other += 1
			else:
				if(int(language_classes[i].strip().split(",")[1]) == 1):
					negative_french += 1
				else:
					negative_other += 1

		#more calculations for entropy equations
		positive_total = positive_french + positive_other
		negative_total = negative_french + negative_other

		total_percent = float(positive_total)/(positive_total + negative_total)

		positive_french_percent = float(positive_french)/positive_total
		positive_other_percent = 1 - positive_french_percent
		negative_french_percent = float(negative_french)/negative_total
		negative_other_percent = 1 - negative_french_percent

		conditional_entropy = total_percent*((-1)*positive_french_percent*math.log(positive_french_percent)/math.log(2) + (-1)*positive_other_percent*math.log(positive_other_percent)/math.log(2) + (-1)*negative_french_percent*math.log(negative_french_percent)/math.log(2) + (-1)*negative_other_percent*math.log(negative_other_percent)/math.log(2))

		#Final information gain equation
		information_gain = total_entropy - conditional_entropy

		#record the gram and score for the Highest Information Gain
		if information_gain > best_entropy:
			best_entropy = information_gain
			best_gram = gram

	print "\nbest 1gram: ", best_gram
	print "entropy: ", best_entropy, "\n"


#________________________Finding the best 1-gram________________________
def bestTwoGram(comments, language_classes):

	best_gram = ""
	best_entropy = 0.0

	#get total entropy
	total_entropy = findEntropy(1, language_classes)

	#iterate through all letters
	from string import ascii_lowercase
	for character1 in ascii_lowercase:

		for character2 in ascii_lowercase:

			#Counters
			positive_french = 0
			positive_other = 0
			negative_french = 0
			negative_other = 0

			gram = character1 + character2
			print gram

			#look at every comment to see if it has that gram
			for i in xrange(1,len(comments)):

				#strip the comment into no spaces all lowecase
				comment = comments[i].strip().split(",")[1].replace(" ", "").lower()

				#increment the right counters
				if gram in comment:
					if(int(language_classes[i].strip().split(",")[1]) == 1):
						positive_french += 1
					else:
						positive_other += 1
				else:
					if(int(language_classes[i].strip().split(",")[1]) == 1):
						negative_french += 1
					else:
						negative_other += 1

			#more calculations for entropy equations
			positive_total = positive_french + positive_other
			negative_total = negative_french + negative_other

			total_percent = float(positive_total)/(positive_total + negative_total)

			positive_french_percent = float(positive_french)/positive_total
			positive_other_percent = 1 - positive_french_percent
			negative_french_percent = float(negative_french)/negative_total
			negative_other_percent = 1 - negative_french_percent

			conditional_entropy = total_percent*((-1)*positive_french_percent*math.log(positive_french_percent)/math.log(2) + (-1)*positive_other_percent*math.log(positive_other_percent)/math.log(2) + (-1)*negative_french_percent*math.log(negative_french_percent)/math.log(2) + (-1)*negative_other_percent*math.log(negative_other_percent)/math.log(2))

			#Final information gain equation
			information_gain = total_entropy - conditional_entropy

			#record the gram and score for the Highest Information Gain
			if information_gain > best_entropy:
				best_entropy = information_gain
				best_gram = gram

	print "\nbest 2gram: ", best_gram
	print "entropy: ", best_entropy, "\n"



#________________________MAIN________________________
#Open the files training_set_x and training_set_y
#Store them in Lists
set_x = "../datasets/train_set_x.csv"
set_y = "../datasets/train_set_y.csv"
file1 = open(set_x, "r")
file2 = open(set_y, "r")
data = file1.readlines()
data_labels = file2.readlines()





