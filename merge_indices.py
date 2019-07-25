





if __name__ == '__main__':
    import sys
    import os
    import json
    import pickle 
    from datetime import datetime

    language2info = {
        'nl' : {
            'year_month_day': (2019, 7, 20),
            'prefix' : 'http://nl.wikipedia.org/wiki/'
           },
        'en' : {
            'year_month_day': (2019, 7, 20),
            'prefix' : 'http://en.wikipedia.org/wiki/'
           },
        'it' : {
            'year_month_day': (2019, 7, 20),
            'prefix' : 'http://it.wikipedia.org/wiki/'
           },
    }
    
    print "provided arguments:"
    print sys.argv
    wiki_folder = sys.argv[1]
    sub_folders = sys.argv[2:]

    language_path = os.path.join(wiki_folder, 'language2info.json')
    with open(language_path, 'w') as outfile:
        json.dump(language2info, outfile)

    print "written language info to %s" % language_path 

    merged_uri2path_info = {}
    for sub_folder in sub_folders:
        path = os.path.join(wiki_folder, sub_folder, 'page2path.p')
        with open(path, 'rb') as infile:
            uri2path_info = pickle.load(infile)
            print 
            print path
            print 'num keys', len(uri2path_info)
            num_keys_before = len(merged_uri2path_info)
            for uri, (path, line_number) in uri2path_info.items():
                one_folder_up = os.path.join(sub_folder, path)
                merged_uri2path_info[uri] = (one_folder_up, line_number)
            num_keys_after = len(merged_uri2path_info)
            print 'total num keys', num_keys_after

            assert num_keys_before + len(uri2path_info) == num_keys_after


    output_path = os.path.join(wiki_folder, 'page2path.p')
    with open(output_path, 'wb') as outfile:
        pickle.dump(merged_uri2path_info, outfile)
    print "written merged uri -> path info to %s" % output_path



