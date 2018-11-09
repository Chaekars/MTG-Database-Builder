import json

#Opens json file
with open("AllSets.json","r", encoding="utf-8") as f:
	data = json.load(f)

for val in data:
	try:
		print(data[val]['magicCardsInfoCode'].lower())
	except:
		print(data[val]['code'].lower())

