#!/bin/bash

mkdir $1
cp -R template.py "${1}/${1}.py"

# Download input
# Put this in .cookie.txt
#  # Netscape HTTP Cookie File
#  .adventofcode.com	TRUE	/	FALSE	0	session	<token-copied-from-browser-devtools>
curl -o $1/input.txt --cookie .cookie.txt https://adventofcode.com/2017/day/$1/input
