#!/usr/local/bin/python
# coding: latin-1

import math
import io

#read the training set into a list which contains all characters for each language
def getCharacters(training_set):

	print "\nGetting Characters...\n"

	#strings that will hold all characters for each language
	slovak_characters = ""
	french_characters = ""
	spanish_characters = ""
	german_characters = ""
	polish_characters = ""

	#read the whole file, make sure to use right encoding to get all those juicy characters
	file = io.open('../datasets/training_data.csv', 'r', encoding='latin-1')
	training_data = file.readlines()

	for i in xrange(1, len(training_data)):

		if i % 25000 == 0:
			print "i: ", i

		#split each line and get relevant values
		line = training_data[i].split("\t")
		language_id = line[1]
		sentence_string = line[2].replace("\n", "").replace(" ", "").lower()

		if int(language_id) == 0:
			slovak_characters = ''.join([slovak_characters, sentence_string])
			
		if int(language_id) == 1:
			french_characters = ''.join([french_characters, sentence_string])
							
		if int(language_id) == 2:
			spanish_characters = ''.join([spanish_characters, sentence_string])
			
		if int(language_id) == 3:
			german_characters = ''.join([german_characters, sentence_string])
			
		if int(language_id) == 4:
			polish_characters = ''.join([polish_characters, sentence_string])

	#return a list with each entry being a string containing all characters typed in a givin langauge
	character_list = [slovak_characters, french_characters, spanish_characters, german_characters, polish_characters]
	return character_list

#turns a list of characters into a list containing character distributions
def makeDistributions(character_list):

	print "Making Distributions...\n"

	distribution_list = []

	for i in xrange(0, len(character_list)):

		#sort the characters
		sorted_string = ''.join(sorted(character_list[i]))
		
		#preliminary variable assignents
		count = 0
		distribution = []
		char = sorted_string[0]

		print char

		#make distribution by counting the number of each character and then diving that 
		#by total number of characters
		for i in xrange(0, len(sorted_string)):

			if(sorted_string[i] == char):
				count += 1
			else:
				distribution.append([char, float(count)/len(sorted_string)])
				char = sorted_string[i]
				count = 1
		#make sure to add the last character to the distribution
		distribution.append([char, float(count)/len(sorted_string)])

		#add the distribution to a list of distributions
		distribution_list.append(distribution)
	
	return distribution_list

def writeToFile(distribution_list):

	print "Writing to ../stats/characterDistributions.txt...\n"

	#open file and clear it
	file = io.open('../stats/characterDistributions.txt', 'w', encoding='latin-1')
	file.truncate()
	#write a line describing the format of the file
	file.write(u'Character distributions\ncharacter,percent occurance\n\n')

	for i in xrange(0, len(distribution_list)):

		distribution = distribution_list[i]

		#header for each new language
		if i == 0:
			file.write(u'Slovak Character Distribution:\n\n')
		if i == 1:
			file.write(u'French Character Distribution:\n\n')
		if i == 2:
			file.write(u'Spanish Character Distribution:\n\n')
		if i == 3:
			file.write(u'German Character Distribution:\n\n')
		if i == 4:
			file.write(u'Polish Character Distribution:\n\n')	

		#write each element of each distribution
		for i in xrange(0, len(distribution)):

			file.write(distribution[i][0] + "," + str(distribution[i][1]) + "\n")

		file.write(u'\n\n')

	file.close()

def sets(distribution_list):

	slovak = set()
	for i in xrange(0, len(distribution_list[0])):
		slovak.add(distribution_list[0][i][0])

	french = set()
	for j in xrange(0, len(distribution_list[1])):
		french.add(distribution_list[1][j][0])

	spanish = set()
	for k in xrange(0, len(distribution_list[2])):
		spanish.add(distribution_list[2][k][0])

	german = set()
	for l in xrange(0, len(distribution_list[3])):
		german.add(distribution_list[3][l][0])

	polish = set()
	for m in xrange(0, len(distribution_list[4])):
		polish.add(distribution_list[4][m][0])

	#_____________USELESS LETTERS____________

	print "\nLetters in Every Language:"
	print slovak & french & spanish & german & polish
	print "\n\n\n"


	#________________ONLY AND NOTS_______________

	print "ONLY slovak"
	print slovak - (slovak & french) - (slovak & spanish) - (slovak & german) - (slovak & polish)
	print "\n"

	print "NOT slovak"
	print french-(french&slovak) | spanish-(spanish&slovak) | german-(german&slovak) | polish-(polish&slovak)
	print "\n"

	print "ONLY french"
	print french - (french & slovak) - (french & spanish) - (french & german) - (french & polish)
	print "\n"

	print "NOT french"
	print slovak-(slovak&french) | spanish-(spanish&french) | german-(german&french) | polish-(polish&french)
	print "\n"

	print "ONLY spanish"
	print spanish - (spanish & slovak) - (spanish & french) - (spanish & german) - (spanish & polish)
	print "\n"

	print "NOT spanish"
	print slovak-(slovak&spanish) | french-(french&spanish) | german-(german&spanish) | polish-(polish&spanish)
	print "\n"

	print "ONLY german"
	print german - (german & slovak) - (german & french) - (german & spanish) - (german & polish)
	print "\n"

	print "NOT german"
	print slovak-(slovak&german) | spanish-(spanish&german) | french-(french&german) | polish-(polish&german)
	print "\n"

	print "ONLY polish"
	print polish - (polish & slovak) - (polish & french) - (polish & spanish) - (polish & german)
	print "\n"

	print "NOT polish"
	print slovak-(slovak&polish) | spanish-(spanish&polish) | german-(german&polish) | french-(french&polish)
	print "\n\n\n"


def main():
	character_list = getCharacters("../datasets/training_data.csv")
	distribution_list = makeDistributions(character_list)
	#writeToFile(distribution_list)
	#sets(distribution_list)

main()





















