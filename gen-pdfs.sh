#!/bin/bash
#set -x

mkdir -p pdfs

for page in $(ls -1 html/*.html)
do
file=$(basename $page)
xhtml2pdf $page pdfs/${file%.*}.pdf
done 
