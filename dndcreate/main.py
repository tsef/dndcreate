#import json
from Personnage import personnage

# items = json.loads('[{"id":1, "text": "item 1"}, {"id":2, "text": "item 2"}]')
# a=5

# for item in items:
#     print(item['text'])

perso = personnage()

for item in perso.biographie:
    print(item)