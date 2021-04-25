# Extract from json
# Version 0.1
import json

result = []

with open ('loremjsonipsum.txt', 'r') as read_file:           # Read file
    data = json.load(read_file)
    print(data)
    print('\n')

    for item in data:
        print('Item: ' + item)
        print('ItemData: ' + item['secondSubLeaf'])
        # result.append(item.get('secondLeaf'))
        # result.append(item['secondLeaf'])

    print (result)


'https://hackersandslackers.com/extract-data-from-complex-json-python/'