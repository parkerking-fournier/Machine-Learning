# -*- coding: latin-1 -*-

import io


#read the training set into a list which contains all characters for each language
def getSets(training_set):

	print "\nMaking sets....\n"

	#strings that will hold all characters for each language
	slovak = set()
	french = set()
	spanish = set()
	german = set()
	polish = set()
	total = set()

	#read the whole file, make sure to use right encoding to get all those juicy characters
	file = io.open('../datasets/training_data.csv', 'r', encoding='latin-1')
	training_data = file.readlines()

	for i in xrange(1, len(training_data)):

		#split each line and get relevant values
		line = training_data[i].split("\t")
		language_id = line[1]
		sentence_string = line[2].replace("\n", "").replace(" ", "").lower()

		if int(language_id) == 0:
			for j in xrange(0, len(sentence_string)):

				#add to relevant alphabet
				if sentence_string[j] not in slovak:
					slovak.add(sentence_string[j])
				
		
		if int(language_id) == 1:
			for k in xrange(0, len(sentence_string)):

				if sentence_string[k] not in french:
					french.add(sentence_string[k])

				
							
		if int(language_id) == 2:
			for l in xrange(0, len(sentence_string)):

				if sentence_string[l] not in spanish:
					spanish.add(sentence_string[l])

				
			
		if int(language_id) == 3:
			for m in xrange(0, len(sentence_string)):

				if sentence_string[m] not in german:
					german.add(sentence_string[m])

				
			
		if int(language_id) == 4:
			for n in xrange(0, len(sentence_string)):

				if sentence_string[n] not in polish:
					polish.add(sentence_string[n])

				

	total = slovak | french | spanish | german | polish 

	#file = io.open('../stats/sets4.txt', 'w', encoding='latin-1')
	#file.truncate()
	#for element in total:
	#	file.write(element)
	#file.write(u'\n\n')

	#print "Writing to Documents/U4?/Fall Semester/ML/Project2//stats/sets.txt...\n"

	#open file and clear it
	#file = io.open('../stats/sets.txt', 'w', encoding='latin-1')
	#file.truncate()



	#_____________USELESS LETTERS____________

	#file.write(u'Letters in Every Language:')
	#file.write(u'\n')
	#temp = slovak & french & spanish & german & polish
	#for element in temp:
		#file.write(element)
	#file.write(u'\n\n\n')


	#________________ONLY AND NOTS_______________

	#file.write(u'ONLY slovak')
	#file.write(u'\n')
	#onlyslovak = slovak - (slovak & french) - (slovak & spanish) - (slovak & german) - (slovak & polish) 
	#for element in onlyslovak:
		#file.write(element)
	#file.write(u'\n\n')

	#file.write(u'NOT slovak')
	#file.write(u'\n')
	#notslovak = french-(french&slovak) | spanish-(spanish&slovak) | german-(german&slovak) | polish-(polish&slovak) 
	#for element in notslovak:
		#file.write(element)
	#file.write(u'\n\n')

	#file.write(u'ONLY french')
	#file.write(u'\n')
	#onlyfrench = french - (french & slovak) - (french & spanish) - (french & german) - (french & polish) 
	#for element in onlyfrench:
		#file.write(element)
	#file.write(u'\n\n')

	#file.write(u'NOT french')
	#file.write(u'\n')
	#notfrench = slovak-(slovak&french) | spanish-(spanish&french) | german-(german&french) | polish-(polish&french) 
	#for element in notfrench:
		#file.write(element)
	#file.write(u'\n\n')

	#file.write(u'ONLY spanish')
	#file.write(u'\n')
	#onlyspanish = spanish - (spanish & slovak) - (spanish & french) - (spanish & german) - (spanish & polish) 
	#for element in onlyspanish:
		#file.write(element)
	#file.write(u'\n\n')

	#file.write(u'NOT spanish')
	#file.write(u'\n')
	#notspanish = slovak-(slovak&spanish) | french-(french&spanish) | german-(german&spanish) | polish-(polish&spanish) 
	#for element in notspanish:
		#file.write(element)
	#file.write(u'\n\n')

	#file.write(u'ONLY german')
	#file.write(u'\n')
	#onlygerman = german - (german & slovak) - (german & french) - (german & spanish) - (german & polish) 
	#for element in onlygerman:
		#file.write(element)
	#file.write(u'\n\n')

	#file.write(u'NOT german')
	#file.write(u'\n')
	#notgerman = slovak-(slovak&german) | spanish-(spanish&german) | french-(french&german) | polish-(polish&german) 
	#for element in notgerman:
		#file.write(element)
	#file.write(u'\n\n')

	#file.write(u'ONLY polish')
	#file.write(u'\n')
	#onlypolish = polish - (polish & slovak) - (polish & french) - (polish & spanish) - (polish & german) 
	#for element in onlypolish:
		#file.write(element)
	#file.write(u'\n\n')

	#file.write(u'NOT polish')
	#file.write(u'\n')
	#notpolish = slovak-(slovak&polish) | spanish-(spanish&polish) | german-(german&polish) | french-(french&polish) 
	#for element in notpolish:
		#file.write(element)
	#file.write(u'\n\n\n')


	#____IMPORTANT SET COMBOS______
	#print "Writing to Documents/U4?/Fall Semester/ML/Project2//stats/sets2.txt...\n"

	#open file and clear it
	#file = io.open('../stats/sets2.txt', 'w', encoding='latin-1')
	#file.truncate()

	#file.write(u'ONLY (polish and slovak)')
	#file.write(u'\n')
	#onlypolishandslovak = (slovak&polish) - (french&slovak&polish) - (german&slovak&polish) - (spanish&slovak&polish) - onlyslovak - onlypolish 
	#for element in onlypolishandslovak:
		#file.write(element)
	#file.write(u'\n\n')


	#file.write(u'ONLY (spanish and french)')
	#file.write(u'\n')
	#onlyfrenchandspanish = (spanish&french) - (slovak&spanish&french) - (german&spanish&french) - (polish&spanish&french) - onlyspanish - onlyfrench
	#for element in onlyfrenchandspanish:
		#file.write(element)
	#file.write(u'\n\n')


	#file.write(u'ONLY (german and polish)')
	#file.write(u'\n')
	#onlygermanandpolish = (german&polish) - (french&german&polish) - (spanish&german&polish) - (slovak&german&polish)
	#for element in onlygermanandpolish:
		#file.write(element)
	#file.write(u'\n\n')

	#file.write(u'ONLY (german and slovak)')
	#file.write(u'\n')
	#onlygermanandslovak = (german&slovak) - (french&german&slovak) - (spanish&german&slovak) - (polish&german&slovak)
	#for element in onlygermanandslovak:
		#file.write(element)
	#file.write(u'\n\n')

	#file.write(u'ONLY (german and slovak)')
	#file.write(u'\n')
	#onlygermanandslovak = (german&slovak) - (french&german&slovak) - (spanish&german&slovak) - (polish&german&slovak)
	#for element in onlygermanandslovak:
		#file.write(element)
	#file.write(u'\n\n')

	#------PARTITIONING [Sl, Gr, Po]___________

	#open file and clear it
	#file = io.open('../stats/sets3.txt', 'w', encoding='latin-1')
	#file.truncate()

	#file.write(u'german NOT polish,slovak')
	#file.write(u'\n')
	#germannotpolishslovak = german - polish - slovak
	#for element in germannotpolishslovak:
		#file.write(element)
	#file.write(u'\n\n')

	#file.write(u'polish NOT german,slovak')
	#file.write(u'\n')
	#polishnotgermanslovak = polish - slovak - german
	#for element in polishnotgermanslovak:
		#file.write(element)
	#file.write(u'\n\n')

	#file.write(u'slovak NOT german,polish')
	#file.write(u'\n')
	#slovaknotgermanpolish = slovak - german - polish
	#for element in slovaknotgermanpolish:
		#file.write(element)
	#file.write(u'\n\n')

	#file.write(u'french NOT spanish')
	#file.write(u'\n')
	#frenchnotspanish = french-spanish
	#for element in frenchnotspanish:
		#file.write(element)
	#file.write(u'\n\n')

	#file.write(u'spanish NOT french')
	#file.write(u'\n')
	#spanishnotfrench = spanish-french
	#for element in spanishnotfrench:
		#file.write(element)
	#file.write(u'\n\n')


	not_slovak = total - slovak
	not_french = total - french	
	not_spanish = total - spanish 
	not_german = total - german
	not_polish = total - polish



	only_slovak = slovak - french - spanish - german - polish
	only_french = french - spanish - german - polish - slovak 
	only_spanish = spanish - german - polish - slovak - french
	only_german = german - polish- slovak - french - spanish 
	only_polish = polish - slovak - french - spanish - german

	#open file and clear it
	file = io.open('../stats/sets6.txt', 'w', encoding='latin-1')
	file.truncate
	
	file.write(u'________NOTS_________\n\n')

	file.write(u'Not Slovak\n')
	for element in not_slovak:
		file.write(element)
	file.write(u'\n\n')
	
	file.write(u'Not French\n')
	for element in not_french:
		file.write(element)
	file.write(u'\n\n')
	
	file.write(u'Not Spanish\n')
	for element in not_spanish:
		file.write(element)
	file.write(u'\n\n')
	
	file.write(u'Not German\n')
	for element in not_german:
		file.write(element)
	file.write(u'\n\n')	
	
	file.write(u'Not Polish\n')
	for element in not_polish:
		file.write(element)
	file.write(u'\n\n\n\n')

	file.write(u'______________ONLYS____________\n\n')


	file.write(u'Only Slovak\n')
	for element in only_slovak:
		file.write(element)
	file.write(u'\n\n')
	
	file.write(u'Only French\n')
	for element in only_french:
		file.write(element)
	file.write(u'\n\n')
	
	file.write(u'Only Spanish\n')
	for element in only_spanish:
		file.write(element)
	file.write(u'\n\n')
	
	file.write(u'Only German\n')
	for element in only_german:
		file.write(element)
	file.write(u'\n\n')	
	
	file.write(u'Only Polish\n')
	for element in only_polish:
		file.write(element)
	
	file.close()



def main():
	getSets("../datasets/training_data.csv")

main()












