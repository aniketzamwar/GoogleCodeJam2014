#!/usr/bin/python

'''
Google Code Jam 2014
https://code.google.com/codejam/contest/2974486/dashboard#s=p3
'''

import sys

def getWarScore(naomi_blocks, kens_blocks):
	naomiWins = 0
	kenBlockIndex = 0
	for i in range(0, len(naomi_blocks)):
		while(kens_blocks[kenBlockIndex] < naomi_blocks[i]):
			naomiWins = naomiWins + 1
			kenBlockIndex = kenBlockIndex + 1
			if(kenBlockIndex >= len(kens_blocks)):
				break
		kenBlockIndex = kenBlockIndex + 1
		if(kenBlockIndex >= len(kens_blocks)):
			break
	return str(naomiWins)

def getDeceitfulWarScore(naomi_blocks, kens_blocks):
	kenEnd = len(naomi_blocks) - 1
	kenBlockIndex = 0
	naomiWins = 0
	 
	for i in range(0, len(naomi_blocks)):
		if(kens_blocks[kenBlockIndex] < naomi_blocks[i]):
			naomiWins = naomiWins + 1
			kenBlockIndex = kenBlockIndex + 1
			continue;
		kenEnd = kenEnd - 1
		
	return str(naomiWins)


if len(sys.argv) != 2:
    print "Please run program: python file.py inputFilename"
    sys.exit()

f = open(sys.argv[1],'r')
count = int(f.readline())

case = 1

while count > 0:
	count = count - 1
	
	line = f.readline()
	numOfBlocks = int(line)
	s = f.readline()
	vals = s.strip().split(' ')
	naomi_blocks = [float(x) for x in vals]
	naomi_blocks.sort()
	s = f.readline()
	vals = s.strip().split(' ')
	kens_blocks = [float(x) for x in vals]
	kens_blocks.sort()

	#print naomi_blocks
	#print kens_blocks
	#print getWarScore(naomi_blocks, kens_blocks)
	#print getDeceitfulWarScore(naomi_blocks, kens_blocks)

	print "Case #" + str(case) + ": "  + getDeceitfulWarScore(naomi_blocks, kens_blocks) + " " + getWarScore(naomi_blocks, kens_blocks)
	case = case + 1


