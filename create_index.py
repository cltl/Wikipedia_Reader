import fnmatch
import os
import json
import pickle
import sys
import bz2
from datetime import datetime


def find_all_files(source_folder, suffix, verbose=0):
    matches = []
    for root, dirnames, filenames in os.walk(source_folder):
        for filename in fnmatch.filter(filenames, '*.%s' % suffix):
            matches.append(os.path.join(root, filename))

    if verbose >= 1:
        print ""
        print 'found %s files' % len(matches)
    return matches


if __name__ == '__main__':
    arguments = sys.argv
    print
    if len(arguments) != 3:
        print
        print 'usage: python create_index.py input_folder language'
        print ''
        print 'this script is written in Python2.7'
        print 'input_folder: output from running convert.sh'
        print 'language: tested with: nl | it | en'
        sys.exit()

    print datetime.now()
    print 'provided arguments'
    print arguments[1:]
    input_folder = arguments[1]
    language = arguments[2]
    number_of_wiki_pages = 0
    assert language in {'nl', 'it', 'en'}, '%s not part of supported languages: nl | it | en' % language
    output_path = os.path.join(input_folder, 'page2path.p')
    stats_path = os.path.join(input_folder, 'stats.json')

    matches = find_all_files(source_folder=input_folder,
                         suffix='bz2',
                         verbose=1)

    old = 'http://en.wikipedia'
    new = 'http://%s.wikipedia' % language

    wiki_url2path_index = {}
    for match in matches:
        with bz2.BZ2File(match, "r") as infile:
            for index, line in enumerate(infile):
                number_of_wiki_pages +=1
                page_info = json.loads(line)
                correct_url = page_info['url'].replace(old, new)

                if correct_url in wiki_url2path_index:
                    print '%s already found before, will use first occurrence' % correct_url
                    continue 

                rsplit_on_slash = match.rsplit('/', 2)
                relative_path = '/'.join([rsplit_on_slash[-2], rsplit_on_slash[-1]])
                wiki_url2path_index[correct_url] = (relative_path, index)


    stats = {
        'num_pages' : number_of_wiki_pages
    }

    with open(output_path, 'wb') as outfile:
        pickle.dump(wiki_url2path_index, outfile)
        print 'written output to %s' % output_path

    with open(stats_path, 'w') as outfile:
        json.dump(stats, outfile)
        print 'written stats to %s' % stats_path


    print 'finished at %s' % datetime.now()
