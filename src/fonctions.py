"""all functionality of the pendu game"""

###!src/bin/python

from random import randint
import pickle

"""main config importation from data.py"""
from src.data import *

def get_param():
	"""get the main config"""
	param = {}
	param['trying_number'] = trying_number
	return param

def get_mot():
	"""provide randomly a word from 'mot' (data.py)"""
	nb_mots = len(mots)
	index = randint(0, nb_mots-1)
	return mots[index]

def is_caract_valide(the_mot, list_find_caract, caract):
	"""evaluate a candidate character"""
	caract = caract.lower()
	if caract in list_find_caract:
		return -1 #already trying
	if caract in the_mot:
		return 1 #eureka
	return 0 #failed

def get_state_mot(the_mot, list_find_caract):
	"""return the state of the word after applicating the finding caracters list"""
	rep = ''
	for index, caract in enumerate(the_mot):
		if (caract in list_find_caract):
			rep += caract
		else:
			rep += '*'
	return rep

def is_complet(the_mot, list_find_caract):
	"""test if all word'scharacter is released"""
	for index, caract in enumerate(the_mot):
		if (caract not in list_find_caract):
			return False
	return True

def saisi_caract():
	"""get a character from the gamer"""
	while 1:
		caract = str(input('tape one character: '))
		caract = caract.strip()
		if len(caract) < 1 :
			print('we need one character like "a" or "b"...')
		else:
			return str(caract[0])

def saisi_nom():
	"""get the gamer's name"""
	while 1:
		nom = str(input('your name: '))
		nom = nom.strip()
		if len(nom) < 1 :
			print('tape your name following by <Enter>')
		else:
			return str(nom)

def save_scores(scores):
	"""save the scores to a file"""
	with open(file_data, 'wb') as scores_file:
		data = pickle.Pickler(scores_file)
		data.dump(scores)

def recup_scores():
	"""read the scores data from a file"""
	scores = {}
	try:
		with open(file_data, 'rb') as scores_file:
			data = pickle.Unpickler(scores_file)
			scores = data.load()
	except FileNotFoundError as e:
		scores = {}
	return scores

def get_his_score(name, scores):
	"""provide the gamer score from the saved data"""
	score = 0
	try:
		score = scores[name]
	except KeyError as e:
		scores[name] = score
	finally:
		return score

def saisi_exit(score):
	"""ask if the gamer want to plaing again or to exit"""
	print('your score: {}'.format(score))
	rep = str(input('ready for one more? or tape "x" to exite: '))
	if rep.strip().lower() == 'x' :
		return True
	return False

def tour(nb_try_init):
	"""one round's game"""
	nb_try = nb_try_init
	the_mot = get_mot()
	find_caract = []
	print('le mot à trouver: '+get_state_mot(the_mot, find_caract))
	while nb_try > 0:
		if is_complet(the_mot, find_caract):
			print('word completed: '+the_mot)
			return nb_try
		print("remain {} try".format(nb_try))
		print('=>'+get_state_mot(the_mot, find_caract))
		caract = saisi_caract()
		commit = is_caract_valide(the_mot, find_caract, caract)
		if commit == -1 :
			print('character revealed yet, please try another.')
			continue
		elif commit == 0 :
			print('No chance! wrong character.')
			nb_try -= 1
			continue
		else :
			print(":) {} new reveal".format(the_mot.count(caract)))
			find_caract.append(caract)
			if is_complet(the_mot, find_caract):
				print('word completed: '+the_mot)
				return nb_try
			continue
	print('you lose :(')
	return 0
