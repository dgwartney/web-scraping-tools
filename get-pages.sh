#!/bin/bash
set -x

mkdir -p html

for url in $(cat "$1")
do
  # Remove trailing slash from the URL if present
  url=${url%/}
  echo $url

  # Extract the last path element using awk and print it
  path_element=$(echo "$url" | awk -F'/' '{print $NF}')
  curl -L --header "user-agent: Mozilla/5.0" $url -o html/${path_element}.html
  sleep 0

done 
