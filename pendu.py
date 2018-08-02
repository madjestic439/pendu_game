###!src/bin/python

import os

from src.fonctions import *

the_mot = get_mot()
print(the_mot)
print(is_caract_valide(the_mot, ['a', 'b'], 't'))
print(get_state_mot(the_mot, ['a', 'b']))

os.system("pause")
