#!/usr/bin/env python

import sys
import re

# def reduce_form(tab, d):
# 	i = 0
# 	c = 0
# 	a = 0
# 	print "Reduced form:",
# 	while i <= d:
# 		j = 0
# 		while j < len(tab):
# 			if (float(tab[j][1]) == i):
# 				if c == 1 and tab[j][0] != 0:
# 					if tab[j][0] < 0:
# 						print "-",
# 						a = -tab[j][0]
# 					else:
# 						print "+",
# 						a = tab[j][0]
# 				else:
# 					a = tab[j][0]
# 				if (i == 0):
# 					c = 1
# 					print "%s" % (a),
# 				elif i == 1:
# 					c = 1
# 					if a == 1:
# 						print "X",
# 					else:
# 						print "%sX" % (a),
# 				elif a != 0:
# 					c = 1
# 					if a == 1:
# 						print "X^%s" % (tab[j][1]),
# 					else:
# 						print "%s * X^%s" % (a, tab[j][1]),
# 				break;
# 			j += 1
# 		i += 1

def reduced_form(tab, d):
	print tab

def degree(tab):
	d = 0
	i = 0
	while i < len(tab):
		if d < int(tab[i][1]):
			d = int(tab[i][1])
		i += 1
	return d

def parser(arg):
	tab = re.findall("(.*) = (.*)", arg)
	# print tab

	left = re.findall("[ ]*([+\- \d.]*) \* ([X^\d]*)", tab[0][0])
	right = re.findall("[ ]*([+\- \d.]*) \* ([X^\d]*)", tab[0][1])
	# print left

	ltab = [[0] * 2 for _ in range(len(left))]
	i = 0
	while i < len(left):
		ltab[i][0] = left[i][0].replace(' ', '')
		tmp = re.findall("[\-]*\d.*", ltab[i][0])
		ltab[i][0] = tmp[0]
		tmp = re.findall("X\^(\d*)", left[i][1])
		ltab[i][1] = tmp[0]
		i += 1
	# print ltab

	rtab = [[0] * 2 for _ in range(len(right))]
	i = 0
	while i < len(right):
		tmp = right[i][0].replace(' ', '')
		rtab[i][0] = str(-float(tmp))
		tmp = re.findall("([\-]*\d.*)", rtab[i][0])
		rtab[i][0] = float(tmp[0])
		tmp = re.findall("X\^(\d*)", right[i][1])
		rtab[i][1] = tmp[0]
		i += 1
	# print rtab

	i = 0
	tab = []
	while i < len(rtab):
		j = 0
		flag = 0
		while j < len(ltab):
			if (ltab[j][1] == rtab[i][1]):
				tmp = float(ltab[j][0]) + rtab[i][0]
				ltab[j][0] = tmp
				flag = 1
			j += 1
		if (flag == 0):
			tab1 = [rtab[i][0], rtab[i][1]]
			tab.append(tab1)
		i += 1
	tab = ltab + tab
	# print tab
	return tab

def check_arg(arg):
	if re.search(r'([+\- \d.]*) \* ([X^\d]*)', arg):
		return 1
	else:
		return 0

if len(sys.argv) <= 2:
	if len(sys.argv) == 2:
		arg = sys.argv[1]
	else:
		arg = raw_input('Enter an equation: ')
	if check_arg(arg) == 0:
		print "Wrong input. Please enter a valid equation"
	else:
		tab = parser(arg)
		d = degree(tab)
		reduced_form(tab, d)
		print "Polynomial degree:", d
else:
	print "Too many arguments !"