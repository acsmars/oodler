# -*- coding: utf-8 -*-
import argparse

def oodley( oodle, doodle ):
	oodle = oodle.lower()
	def listGet(list,index):
		if index < 0: return ' '
		try: return list[index]
		except: return ' '
	if listGet(oodle,doodle+1) in 'aeiou':
		return False
	if listGet(oodle,doodle-1) in 'aeiou' and listGet(oodle,doodle+1) != ' ':
		return False
	return True

def soodle( oodle ):
	with open(args.output, 'w') as foodle:
			foodle.write(oodle)
			foodle.close()

def oodlr( oodle, roodle=0 ):
	noodle = []
	if roodle>0: oodle = oodlr(oodle,roodle-1)
	if args.accent:
		for doodle in range(len(oodle)):
			if oodle[doodle] == 'a': noodle.append(u"oôdle")
			elif oodle[doodle] == 'e': noodle.append(u"oödle")
			elif oodle[doodle] == 'i': noodle.append(u"oòdle")
			elif oodle[doodle] == 'o': noodle.append(u"oódle")
			elif oodle[doodle] == 'u': noodle.append(u"oōdle")
			elif oodle[doodle] == 'y' and oodley(oodle,doodle): noodle.append(u"oodle")
			elif oodle[doodle] == 'A': noodle.append(u"Oôdle")
			elif oodle[doodle] == 'E': noodle.append(u"Oödle")
			elif oodle[doodle] == 'I': noodle.append(u"Oòdle")
			elif oodle[doodle] == 'O': noodle.append(u"Oódle")
			elif oodle[doodle] == 'U': noodle.append(u"Oōdle")
			elif oodle[doodle] == 'Y' and oodley(oodle,doodle): noodle.append(u"Oodle")
			else: noodle.append(oodle[doodle])
		noodle = ''.join(noodle)
		if roodle>0: print len(noodle)
		return noodle
	elif args.binary:
		for doodle in range(len(oodle)):
			if oodle[doodle] == 'a': noodle.append(u"oodlE")
			elif oodle[doodle] == 'e': noodle.append(u"oodLe")
			elif oodle[doodle] == 'i': noodle.append(u"oodLE")
			elif oodle[doodle] == 'o': noodle.append(u"ooDle")
			elif oodle[doodle] == 'u': noodle.append(u"ooDlE")
			elif oodle[doodle] == 'y' and oodley(oodle,doodle): noodle.append(u"ooDLe")
			elif oodle[doodle] == 'A': noodle.append(u"OodlE")
			elif oodle[doodle] == 'E': noodle.append(u"OodLe")
			elif oodle[doodle] == 'I': noodle.append(u"OodLE")
			elif oodle[doodle] == 'O': noodle.append(u"OoDle")
			elif oodle[doodle] == 'U': noodle.append(u"OoDlE")
			elif oodle[doodle] == 'Y' and oodley(oodle,doodle): noodle.append(u"OoDLe")
			else: noodle.append(oodle[doodle])
		noodle = ''.join(noodle)
		if roodle>0: print len(noodle)
		return noodle
	else:
		for doodle in range(len(oodle)):
			if oodle[doodle] in 'aeiou' or (oodle[doodle] == 'y' and oodley(oodle,doodle)):
				noodle.append("oodle")
			elif oodle[doodle] in 'AEIOU' or (oodle[doodle] == 'Y' and oodley(oodle,doodle)):
				noodle.append("Oodle")
			else:
				noodle.append(oodle[doodle])
		noodle = ''.join(noodle)
		if roodle>0: print len(noodle)
		return noodle

parser = argparse.ArgumentParser(description='Oodler for Oodling Oodlable Text')
parser.add_argument('input', metavar='input text or file', nargs='?', type=str, help='input', default='Hello World!')
parser.add_argument('output', metavar='output file', nargs='?', type=str, help='output', default='oodle.txt')
parser.add_argument('recursive', metavar='recursively oodle', nargs='?', type=int, help='recursively oodle', default=0)
parser.add_argument('-f','--file', action='store_true', help='flag for file input')
parser.add_argument('-a','--accent', action='store_true', help='flag for accented oodles')
parser.add_argument('-b','--binary', action='store_true', help='flag for binary oodles')
parser.add_argument('-s','--save', action='store_true', help='flag for file output')
parser.add_argument('-c','--console', action='store_true', help='flag to display output to console')
args = parser.parse_args()

if args.file:
	try:
		with open(args.input, 'r') as foodle:
			oodle = foodle.read()
			print "Reading data from {}...".format( args.input )
			toodle = oodlr( oodle, args.recursive )
			if args.console: print toodle
			if args.save: soodle(toodle.encode('utf-8'))
	except Exception as e:
		print "Error reading {}: {}".format( args.input,e )
else:
	print "Oodling text..."
	toodle = oodlr( args.input, args.recursive )
	if args.console: print toodle
	if args.save: soodle(toodle.encode('utf-8'))
