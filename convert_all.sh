#rm -rf wiki
#mkdir wiki
#bash convert.sh /mnt/scistor1/group/home/postma/wikipedia_dumps/nlwiki-20190720-pages-articles.xml.bz2 /home/postma/Wikipedia_Reader/wiki/wiki_nl nl > log/nl.out 2> log/nl.err
#bash convert.sh /mnt/scistor1/group/home/postma/wikipedia_dumps/itwiki-20190720-pages-articles.xml.bz2 /home/postma/Wikipedia_Reader/wiki/wiki_it it > log/it.out 2> log/it.err 
#bash convert.sh /mnt/scistor1/group/home/postma/wikipedia_dumps/enwiki-20190720-pages-articles.xml.bz2 /home/postma/Wikipedia_Reader/wiki/wiki_en en > log/en.out 2> log/en.err

python2.7 merge_indices.py wiki wiki_nl wiki_it wiki_en
