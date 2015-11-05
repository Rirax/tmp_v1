def determinant(coef):
	dlta = (coef.b * coef.b) - (4 * coef.a * coef.c)
	return dlta


def which_solution(coef, d, tab):
	dlta = determinant(coef)
	if coef.a == 0 and coef.b == 0 and coef.c == 0 and d <= 2:
		print "Cas particulier : La solution est l'ensemble des reels."
	elif d == 0 and coef.c != 0:
		print "Pas de solution."
	elif d > 2:
		print "The polynomial degree is strictly greater than 2, I can't solve."
	elif d == 1 or coef.a == 0:
		print "There is one solution."
		solution_premier_degre(coef, dlta)
	else:
		if dlta > 0:
			print "Discriminant is strictly positive, the two solutions are:"
			solution_positive(coef, dlta)
		elif dlta == 0:
			print "Discriminant is null, the solution is:"
			solution_unique(coef, dlta)
		elif dlta < 0:
			print "Discriminant is strictly negative, the two solutions are:"
			solution_imaginaire(coef, dlta)
	return None


def solution_positive(coef, dlta):
	x1 = (- coef.b + (dlta ** 0.5)) / (2 * coef.a)
	x2 = (- coef.b - (dlta ** 0.5)) / (2 * coef.a)
	print "%f\n%f" % (x1, x2)
	return None

def solution_unique(coef, dlta):
	x1 = - coef.b / (2 * coef.a)
	print "%f" % (x1)
	return None

def solution_imaginaire(coef, dlta):
	x1 = - coef.b / (2 * coef.a)
	x2 = ((- dlta) ** 0.5) / (2 * coef.a)
	print "%f + i * %f\n%f - i * %f" % (x1, x2, x1, x2)
	return None

def solution_premier_degre(coef, dlta):
	x1 = - coef.c / coef.b
	print "%f" % x1
	return None