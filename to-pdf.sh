#!/bin/bash

mkdir -p new-pdfs

for file in $(ls -1 clean)
do

  pandoc clean/$file -t latex -o "new-pdfs/${file%.txt}.pdf"

done
