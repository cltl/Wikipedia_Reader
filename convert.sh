#!/usr/bin/env bash

#check if enough arguments are passed, else print usage information
if [ $# -eq 0 ];
then
    echo
    echo "Usage:                  : $0 input_path output_folder"
    echo
    echo "input_path            : path to Wikipedia dump *pages-articles.xml.bz2"
    echo "output_folder         : folder where you want to store the extracted files"
    echo ""
    echo "bash convert /mnt/scistor1/group/home/postma/wikipedia_dumps/nlwiki-latest-pages-articles.xml.bz2 wiki_nl"
    exit -1;
fi


export input_path=$1
export output_folder=$2


rm -rf $output_folder
cd resources/Annotated-WikiExtractor/annotated_wikiextractor
bzip2 -dc $input_path | python2.7 annotated_wikiextractor.py -co $output_folder > $output_folder/log.out $output_folder/log.err &