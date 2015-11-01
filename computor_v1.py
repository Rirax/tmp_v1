#!/usr/bin/env python

import sys
import re

if len(sys.argv) <= 2:
	if len(sys.argv) == 2:
		arg = sys.argv[1]
	else:
		arg = raw_input('Enter an equation: ')
	if check_arg(arg) == 0:
		print "\033[31m------> Wrong input. Please enter a valid equation.\033[37m"
	else:
		p = re.compile(r'(.*) = (.*)')
else:
	print "\033[31mToo many arguments.\033[37m"

def check_argument(arg):
	if re.search(r'([+\- \d.]*) \* ([X^\d]*)', arg):
		return 1
	else:
		return 0