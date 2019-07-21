#!/usr/bin/env bash

#check if enough arguments are passed, else print usage information
if [ $# -eq 0 ];
then
    echo
    echo "Usage:                  : $0 data_folder"
    echo
    echo "data_folder            : folder where dumps of Wikipedia will be stored (repositories will be stored in resources)"
    exit -1;
fi

rm -rf resources
mkdir resources
cd resources
git clone https://github.com/jodaiber/Annotated-WikiExtractor
cd ..

export data_folder=$1

rm -rf $data_folder
mkdir $data_folder
cd $data_folder

wget https://dumps.wikimedia.org/nlwiki/latest/nlwiki-latest-pages-articles.xml.bz2
wget https://dumps.wikimedia.org/itwiki/latest/itwiki-latest-pages-articles.xml.bz2
wget https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
