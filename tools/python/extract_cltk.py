import json
import json.tool
from pathlib import Path

file = Path(__file__).parent.joinpath('7caba5736b1d9e26c1a5a8af278a3383.json')

with file.open("r") as fp:
    file_obj = json.load(fp)
    cltk = file_obj['_source']['cltk']
    cltk_obj = json.loads(cltk)

output = Path(__file__).parent.joinpath('7caba5736b1d9e26c1a5a8af278a3383.cltk.json')
with output.open("w") as fp:
    json.dump(cltk_obj, fp, indent=4)
