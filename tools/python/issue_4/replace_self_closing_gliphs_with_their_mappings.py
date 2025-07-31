import xml.etree.ElementTree as ET
import re
import sys

tei_path = sys.argv[1]
tree = ET.parse(tei_path)
gliphs_mappings = {}
ns = {'tei':'http://www.tei-c.org/ns/1.0','xml':'http://www.w3.org/XML/1998/namespace'}
for char in tree.findall(".//tei:teiHeader/tei:encodingDesc/tei:charDecl/tei:char", ns):
    key = char.get('{http://www.w3.org/XML/1998/namespace}id')
    value = char.find(".//tei:mapping[2]", ns).text
    if key and value:
        value = value.strip()
        if (value):
            gliphs_mappings[key] = value

print(gliphs_mappings)


# Questo sarebbe stato il modo più corretto, ma:
# 1. sostituisce i caratteri unicode con xml entities
# 2. non voglio toccare niente dell'XML originale (commenti compresi)

'''
for g in tree.findall(".//tei:g", ns):
    ref = g.get('ref')
    if (ref):
        key = ref[1:]
        if key in gliphs_mappings:
            g.text = gliphs_mappings[key]
        else:
            print(key)

tree.write(tei_path + ".corr")
'''

# quindi userò le regexp

def replace_gliph(matchobj: re.Match):
    key = matchobj.group(1)[1:]
    if (key in gliphs_mappings):
        return '<g ref="{ref}">{gliph}</g>'.format(ref = matchobj.group(1), gliph = gliphs_mappings[key])
    return matchobj.group(0)


with open(tei_path, 'r') as f:
   # Read the file contents into a single variable
   contents = f.read()


# Replace the whole contents
new_contents = re.sub('<g\s+ref="(#[^"]+)"\s*/>', replace_gliph, contents, flags=re.IGNORECASE)

with open(tei_path + ".corr", 'w') as f:
     # actually write the lines
     f.write(new_contents)