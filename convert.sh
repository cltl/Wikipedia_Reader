#!/usr/bin/env bash

#check if enough arguments are passed, else print usage information
if [ $# -eq 0 ];
then
    echo
    echo "Usage:                  : $0 input_path output_folder language"
    echo
    echo "input_path            : path to Wikipedia dump *pages-articles.xml.bz2"
    echo "output_folder         : folder where you want to store the extracted files"
    echo "language              : supported: nl en it"
    echo ""
    echo "bash convert.sh /mnt/scistor1/group/home/postma/wikipedia_dumps/nlwiki-latest-pages-articles.xml.bz2 /home/postma/Wikipedia_Reader/wiki_nl nl"
    exit -1;
fi


export input_path=$1
export output_folder=$2
export language=$3

rm -rf $output_folder
mkdir $output_folder
echo "start" `date` >> $output_folder/how_long_it_took.log
cd resources/Annotated-WikiExtractor/annotated_wikiextractor
bzip2 -dc $input_path | python2.7 annotated_wikiextractor.py -co $output_folder

echo "end" `date` >> $output_folder/how_long_it_took.log
cd ../../../
python2.7 create_index.py $output_folder $language
