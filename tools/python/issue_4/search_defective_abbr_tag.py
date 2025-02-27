import json
import pathlib

# Ottengo il path della risorsa relativo a questo file python e apro il file
json_file_path = pathlib.Path(__file__).parent.parent.joinpath('resources/7caba5736b1d9e26c1a5a8af278a3383.json')
json_file = open(json_file_path, 'r', encoding="utf-8")

# Decoding JSON to a dict
json_document = json.load(json_file)

# The length of the text
plainText = json_document['hits']['hits'][0]['_source']['plainText']
print("Plain text length: %d" % len(plainText))

for tag in (tag for tag in json_document['hits']['hits'][0]['_source']['tags'] if tag['externalName'] == 'abbr'):
    if (tag['startPosition'] >= tag['endPosition']):
        # print(tag['startPosition'])
        print(tag)
        print(plainText[tag['startPosition']:tag['endPosition'] + 25])
    
json_file.close()
