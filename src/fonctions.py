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

def saisi_caract():
	while 1:
		caract = str(input('tape one character: '))
		caract = caract.strip()
		if len(caract) < 1 :
			print('we need one character like "a" or "b"...')
		else:
			return str(caract[0])

def saisi_nom():
	while 1:
		nom = str(input('your name: '))
		nom = nom.strip()
		if len(nom) < 1 :
			print('tape your name following by <Enter>')
		else:
			return str(nom)
