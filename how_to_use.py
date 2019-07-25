import bz2
import pickle
import os
import json
from datetime import datetime 

input_folder = 'wiki/wiki_en' # where bz2 files are (output from convert.sh)
index_path = 'wiki/wiki_en/page2path.p' # where output is stored (result of running create_index.py)
print "loading index", datetime.now() 
with open(index_path, 'rb') as infile:
    page2relativepath_and_linenumber = pickle.load(infile)
print "loaded index", datetime.now()

wiki_url = 'http://en.wikipedia.org/wiki/Edelweiss_(grape)'
relative_path, line_number = page2relativepath_and_linenumber[wiki_url]

path = os.path.join(input_folder, relative_path)
print(path)
print "loading bz2 file", datetime.now()
with bz2.BZ2File(path, "r") as infile:
    for index, line in enumerate(infile):
        if index == line_number:
            page_info = json.loads(line)
            break

print(page_info)
print "finished", datetime.now()
