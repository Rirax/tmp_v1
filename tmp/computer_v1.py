#!/usr/bin/env python

import sys
import re

from fonctions import *
from calculs import *

draw = 0
if len(sys.argv) <= 3:
	if len(sys.argv) == 3:
		argument = sys.argv[1]
		if sys.argv[2] != '-d':
			print "\033[31m\n------> Wrong option ! -d to draw graphic.\033[37m\n"
		else:
			draw = 1
	elif len(sys.argv) == 2:
		argument = sys.argv[1]
	else:
		argument = raw_input('Enter an equation: ')
	if check_argument(argument) == 0:
		print "\033[31m------> Wrong input. Please enter a valid equation.\033[37m"
	else:
		p = re.compile(r'(.*) = (.*)')
		tab = init_tab(argument)
		degree = find_degree(tab)
		reduce_form(tab, degree)
		print "\033[32mPolynomial degree: %d\033[37m" % (degree)
		if degree <= 2:
			equation = init_equation(tab)
			which_solution(equation, degree, tab)
else:
	print "\033[31mToo many arguments.\033[37m"

