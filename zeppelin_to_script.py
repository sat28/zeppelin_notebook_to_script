import sys
input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

import json
import codecs
notebook = json.load(codecs.open(input_file_name, 'r', 'utf-8-sig'))

script = []
for i in notebook["paragraphs"]:
    if "text" in i:
        para = i["text"].splitlines()[1:]
        if len(para) > 0:
            para = '\n'.join(para)
            script.append(para)
script_f = '\n\n'.join(script)

with open(output_file_name, 'w') as the_file:
    the_file.write(script_f)
