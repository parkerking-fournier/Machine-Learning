# -*- coding: utf-8 -*-

import io
import math

def notSlovak(letter_set):
	not_slovak = set(['É','Ñ','á','à','ã','ä','å','ê','ï','ù','†','£','¢','§','¶','®','¨','Ø','Æ','µ','ª','æ','„','Á','Ê','È','Î','Ì','Ò','','Û','ı','Ù','˜','˘','¸'])
	if len(not_slovak&letter_set) > 0:
		return True
	else:
		return False

#______________________MAIN______________________
def main():
	file1 = io.open('../stats/notsandonlys.txt', 'r', encoding='latin-1')


	file2 = io.open('../datasets/train_set_x.csv', 'r', encoding='latin-1')
	temp1 = file1.readlines()

	print temp1

	
	

main()