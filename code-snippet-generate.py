import json

data = {}

with open("input.txt", "r") as file:
    lineAll = file.readlines()

for line in lineAll:
    words = line.split()
    data[words[1]] = {
        'prefix': words[1],
        'scope': 'c',
        'body': words[1]
    }

with open('stm32-spi.code-snippets', 'w') as outfile:
    json.dump(data, outfile, indent=4)

