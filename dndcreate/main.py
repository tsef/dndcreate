#import json
from Personnage import *

# items = json.loads('[{"id":1, "text": "item 1"}, {"id":2, "text": "item 2"}]')
# a=5

# for item in items:
#     print(item['text'])

perso = personnage()

perso.biographie["Nom"] = input("Un nom à la con: ")
perso.biographie["Classe"] = input("Une classe à la con: ")

for key, value in perso.biographie.items():
    print(key, value)

with open('perso.txt', 'w+') as outfile:
    #outfile.seek(0)
    json.dump(perso.biographie, outfile)