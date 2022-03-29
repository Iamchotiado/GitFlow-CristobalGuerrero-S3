from collections import Counter
tokens = [{"Value": "Blah", "SO": 0}, {"Value": "zoom", "SO": 5}, {"Value": "Blah", "SO": 2}, {"Value": "Blah", "SO": 3}]
contador = Counter(tok['Value'] for tok in tokens)
print(contador)


for value in contador.values():
    print(value)

for value in contador.keys():
    print(value)