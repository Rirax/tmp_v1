#!/usr/bin/env python

import sys
import re

from fonctions import *
from calculs import *

import numpy as np
import matplotlib.pyplot as plt

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
		# if p.search(argument) == None:
		# 	init_tab_noequal(argument)
		# else:
		tab = init_tab(argument)
		degree = find_degree(tab)
		reduce_form(tab, degree)
		print "\033[32mPolynomial degree: %d\033[37m" % (degree)
		if degree <= 2:
			equation = init_equation(tab)
			which_solution(equation, degree, tab)
		if draw == 1 and degree > 0:
			coord = calculate_coord(tab)
			points = np.array(coord)
			# get x and y vectors
			x = points[:,0]
			y = points[:,1]
			# calculate polynomial
			z = np.polyfit(x, y, 3)
			f = np.poly1d(z)
			# calculate new x's and y's
			x_new = np.linspace(x[0], x[-1], 50)
			y_new = f(x_new)
			plt.plot(x,y,'o', x_new, y_new)
			plt.xlim([x[0]-1, x[-1] + 1 ])
			plt.show()
else:
	print "\033[31mToo many arguments.\033[37m"

