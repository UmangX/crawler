import os; 
import sys

term = sys.argv[1]; 

file1 = open('history.txt', 'r')
Lines = file1.readlines() 

# Strips the newline character
for line in Lines:
    file = line.strip();
    data = os.popen("cat " + file +" | python3 ~/dev/crawler/test2.py " + term ).read();
    if data != 0:   
       print(file + " --> " + data); 
