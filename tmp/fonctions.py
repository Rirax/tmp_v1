import re

def init_tab(argument):
	p = re.compile(r'(.*) = (.*)')
	b = p.findall(argument)

	p = re.compile(r'[ ]*([+\- \d.]*) \* ([X^\d]*)')
	match1 = p.findall(b[0][0])
	match2 = p.findall(b[0][1])

	tab1 = [[0] * 2 for _ in range(len(match1))]
	i = 0
	while i < len(match1):
		a = match1[i][0].replace(' ', '')
		tab1[i][0] = a
		p = re.compile(r'([\-]*\d.*)')
		ret = p.findall(tab1[i][0])
		tab1[i][0] = ret[0]
		p = re.compile(r'X\^(\d*)')
		ret = p.findall(match1[i][1])
		tab1[i][1] = ret[0]
		i += 1

	tab2 = [[0] * 2 for _ in range(len(match2))]
	i = 0
	while i < len(match2):
		a = match2[i][0].replace(' ', '')
		a = float(a)
		a = -a
		a = str(a)
		tab2[i][0] = a
		p = re.compile(r'([\-]*\d.*)')
		ret = p.findall(tab2[i][0])
		tab2[i][0] = float(ret[0])
		p = re.compile(r'X\^(\d*)')
		ret = p.findall(match2[i][1])
		tab2[i][1] = ret[0]
		i += 1

	j = 0
	k = 0
	tab3 = []
	tab = []
	while j < len(tab2):
		k = 0
		c = 0
		while k < len(tab1):
			if (tab1[k][1] == tab2[j][1]):
				x = float(tab1[k][0]) + tab2[j][0]
				tab1[k][0] = x
				c = 1
			k += 1
		if (c == 0):
			tab3 = [tab2[j][0], tab2[j][1]]
			tab.append(tab3)
		j += 1
	tab = tab1 + tab
	print tab
	return tab

def check_argument(arg):
	if re.search(r'([+\- \d.]*) \* ([X^\d]*)', arg):
		return 1
	else:
		return 0
