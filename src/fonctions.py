###!src/bin/python

from random import randint
import pickle

from src.data import *

def get_param():
	param = {}
	param['trying_number'] = trying_number
	return param

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

def is_complet(the_mot, list_find_caract):
	for index, caract in enumerate(the_mot):
		if (caract not in list_find_caract):
			return False
	return True

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

def save_scores(scores):
	with open(file_data, 'wb') as scores_file:
		data = pickle.Pickler(scores_file)
		data.dump(scores)

def recup_scores():
	scores = {}
	try:
		with open(file_data, 'rb') as scores_file:
			data = pickle.Unpickler(scores_file)
			scores = data.load()
	except FileNotFoundError as e:
		scores = {}
	return scores

def get_his_score(name, scores):
	score = 0
	try:
		score = scores[name]
	except KeyError as e:
		scores[name] = score
	finally:
		return score

def saisi_exit(score):
	print('your score: {}'.format(score))
	rep = str(input('ready for one more? or tape "x" to exite: '))
	if rep.strip().lower() == 'x' :
		return True
	return False

def tour(nb_try_init):
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
