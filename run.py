import os; 
import sys

location = sys.argv[1];
term = sys.argv[2]; 
os.system("find " + location +" -type f > history.txt"); 

file1 = open('history.txt', 'r')
Lines = file1.readlines() 

def execute_locator(file):    
    data = os.popen("cat " + file +" | python3 ~/dev/crawler/test2.py " + term ).read(); 
    if data != 0:   
       print(file + " --> " + data);

for line in Lines:
    file = line.strip();
    execute_locator(file); 

os.system("rm history.txt")       
