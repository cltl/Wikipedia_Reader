import bz2
import pickle
import os
import json

input_folder = '/Users/marten/Downloads/wiki_nl' # where bz2 files are (output from convert.sh)
index_path = '/Users/marten/Downloads/wiki_nl/page2path.p' # where output is stored (result of running create_index.py)
with open(index_path, 'rb') as infile:
    page2relativepath_and_linenumber = pickle.load(infile)

wiki_url = 'http://nl.wikipedia.org/wiki/Edelweiss'
relative_path, line_number = page2relativepath_and_linenumber[wiki_url]

path = os.path.join(input_folder, relative_path)
print(path)

with bz2.BZ2File(path, "r") as infile:
    for index, line in enumerate(infile):
        if index == line_number:
            page_info = json.loads(line)
            break

print(page_info)