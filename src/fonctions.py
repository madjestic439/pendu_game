###!src/bin/python

from random import randint

from src.data import *

def get_mot():
	nb_mots = len(mots)
	index = randint(0, nb_mots-1)
	return mots[index]

def is_caract_valide(the_mot, list_find_caract, caract):
	caract = caract.lower()
	if caract in list_find_caract:
		return -1 #already trying
	if caract in the_mot:
		return 1 #eureka
	return 0 #failed

def get_state_mot(the_mot, list_find_caract):
	rep = ''
	for index, caract in enumerate(the_mot):
		if (caract in list_find_caract):
			rep += caract
		else:
			rep += '*'
	return rep
