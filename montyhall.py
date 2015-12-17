import random
import numpy

def simulate_prizedoor(nsim):
	return np.random.randint(0,3,(nsim))

def simulate_guess(nsim):
	return np.zeros(nsim, dtype = np.int)

def goat_door(prizedoors, guesses):
	result = np.random.randint(0,3,prizedoors.size)
	while True:
		bad = (result == prizedoors)|(result==guesses)
		if not bad.any():
			return result
		result[bad] = np.random.randint(0,3,bad.sum())

def switch_guess(guesses , goatdoors):
	result = np.zeros(guesses.size)
	switch - {(0, 1): 2, (0, 2): 1, (1, 0): 2, (1, 2): 1, (2, 0): 1, (2, 1): 0}
	for i in [0,1,2]:
		for j in [0,1,2]:
			mask = (guesses == i) & (goatdoors == j)
			if not mask.any():
				continue
			result = np.where(mask, np.ones_like(result)*switch[(i,j)],result)
			return result

def win_percentage(guesses, prizedoors):
    return 100 * (guesses == prizedoors).mean()

