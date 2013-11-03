# -*- coding: utf-8-*-


import sys
import os

def convert(line):
	tmp = line.split('->')
	
	print "tmp="tmp

	Orinage = tmp[0]
	print "orinage = " + Orinage
	NewTrans = tmp[1]
	print "newtrans = " + NewTrans

	tmp2 = Orinage.split(':')
	UnTrans = tmp2[0]
	OldTrans = tmp2[1]

#	NewTrans.replace('\n', ',')

	NewLine = UnTrans + ':' + NewTrans + ',' + '\n'

	return NewLine

UnTransFile = open(r'/home/zhu_yunchuan/work/translationchangelog')

NewTransFile = open(r'/home/zhu_yunchuan/work/Portuguese', 'w')

for line in UnTransFile:
	if line != '\r\n':
		NewTransline = convert(line)
		NewTransFile.write(NewTransline)
NewTransFile.close()
