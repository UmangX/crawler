#!/usr/bin/python3
#find ~/.config/nvim/colors  -type f > ~/dev/crawler/history.txt
#pipeline the text to this python file and search for word 
import sys
import re 
index = 0; 
try:
    for line in sys.stdin:
        regex_pattern = sys.argv[1];
        pattern = re.compile(regex_pattern)
        if pattern.search(line):
           index +=1;
except UnicodeDecodeError:print("Can't read the file")
print(index);        
