import json
import pathlib

# Ottengo il path della risorsa relativo a questo file python e apro il file
# json_file_path = pathlib.Path(__file__).parent.joinpath('resources/7caba5736b1d9e26c1a5a8af278a3383.json')
json_file_path = pathlib.Path(__file__).parent.joinpath('resources/b76f9b1a74d8c152bfc33126bb614db6.json')
plain_text_file_path = pathlib.Path.home().joinpath('b76f9b1a74d8c152bfc33126bb614db6.plainText.txt')

json_file = open(json_file_path, 'r', encoding="utf-8")

# Decoding JSON to a dict
json_document = json.load(json_file)

try:
    plain_text_file = open(plain_text_file_path, 'w', encoding="utf-8")
    plain_text_file.write(json_document['_source']['plainText'])
finally:
    plain_text_file.close()

json_file.close()
