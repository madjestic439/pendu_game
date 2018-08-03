"""the main structure of the pendu game"""

###!src/bin/python

import os

from src.fonctions import *

param = get_param()
scores = recup_scores()
gamer = saisi_nom()

point = get_his_score(gamer, scores)

print("welcome {}, your score: {}. ready for game?".format(gamer, point))
os.system("pause")

while 1:
	scores[gamer] += tour(param['trying_number'])
	save_scores(scores)
	if saisi_exit(scores[gamer]) :
		print('bye :)')
		os.system("pause")
		break
