class Equation(object):
	"""docstring for Equation"""
	def __init__(self):
		self.c = 0
		self.b = 0
		self.a = 0

def reduce_form(tab, degree):
	i = 0
	c = 0
	a = 0
	print "\033[36mReduced form:",
	while i <= degree:
		j = 0
		while j < len(tab):
			if (float(tab[j][1]) == i):
				if c == 1 and tab[j][0] != 0:
					if tab[j][0] < 0:
						print "-",
						a = -tab[j][0]
					else:
						print "+",
						a = tab[j][0]
				else:
					a = tab[j][0]
				if (i == 0):
					c = 1
					print "%s" % (a),
				elif i == 1:
					c = 1
					if a == 1:
						print "X",
					else:
						print "%sX" % (a),
				elif a != 0:
					c = 1
					if a == 1:
						print "X^%s" % (tab[j][1]),
					else:
						print "%s * X^%s" % (a, tab[j][1]),
				break;
			j += 1
		i += 1
	print "= 0 \033[37m"


def find_degree(tab):
	c = 0
	i = 0
	while i < len(tab):
		if c < int(tab[i][1]):
			c = int(tab[i][1])
		i += 1
	return c

def init_equation(tab):
	i = 0
	j = 0
	eq = Equation()
	while i < len(tab):
		if float(tab[i][1]) == 0:
			eq.c = float(tab[i][0])
		elif float(tab[i][1]) == 1:
			eq.b = float(tab[i][0])
		elif float(tab[i][1]) == 2:
			eq.a = float(tab[i][0])
		i += 1
	print "\033[33ma:", round(eq.a, 2),
	print " b:", round(eq.b, 2),
	print " c:", round(eq.c, 2),
	print "\033[37m"
	return eq

def determinant(equation):
	delta = (equation.b * equation.b) - (4 * equation.a * equation.c)
	print "\033[35mDelta: ", round(delta, 2),
	print "\033[37m"
	return delta


def which_solution(eq, degree, tab):
	delta = determinant(eq)
	if eq.a == 0 and eq.b == 0 and eq.c == 0 and degree <= 2:
		print "\033[36mCas particulier : La solution est l'ensemble des reels.\033[37m"
	elif degree == 0 and eq.c != 0:
		print "\033[36mPas de solution.\033[37m"
	elif degree > 2:
		print "\033[36mThe polynomial degree is strictly greater than 2, I can't solve.\033[37m"
	elif degree == 1 or eq.a == 0:
		print "\033[32mThere is one solution.\033[37m"
		solution_premier_degre(eq, delta)
	else:
		if delta > 0:
			print "\033[36mDiscriminant is strictly positive, the two solutions are:\033[37m"
			solution_positive(eq, delta)
		elif delta == 0:
			print "\033[36mDiscriminant is null, the solution is:\033[37m"
			solution_unique(eq, delta)
		elif delta < 0:
			print "\033[36mDiscriminant is strictly negative, the two solutions are:\033[37m"
			solution_imaginaire(eq, delta)
	return None


def solution_positive(eq, delta):
	x1 = (- eq.b + (delta ** 0.5)) / (2 * eq.a)
	x2 = (- eq.b - (delta ** 0.5)) / (2 * eq.a)
	print "%f\n%f" % (x1, x2)
	return None

def solution_unique(eq, delta):
	x1 = - eq.b / (2 * eq.a)
	print "%f" % (x1)
	return None

def solution_imaginaire(eq, delta):
	x1 = - eq.b / (2 * eq.a)
	x2 = ((- delta) ** 0.5) / (2 * eq.a)
	print "%f + i * %f\n%f - i * %f" % (x1, x2, x1, x2)
	return None

def solution_premier_degre(eq, delta):
	x1 = - eq.c / eq.b
	print "%f" % x1
	return None

