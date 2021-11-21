import os;
import sys

location = sys.argv[1];
term = sys.argv[2];

if len(term) < 5:
   print("Search term too small try with more then 5 character")
   exit();

os.system("find " + location +" -type f > history.txt");

file_viewed = 0;

file1 = open('history.txt', 'r')
Lines = file1.readlines()

def execute_locator(file):
    data = os.popen("cat " + file +" | python3 ~/dev/crawler/test2.py " + term ).read();
    print(file + " --> " + data);

for line in Lines:
    file = line.strip();
    execute_locator(file);
    file_viewed +=1;
    
print("------------------------------------------------------------------")
print("Read",file_viewed,"Files In",location)
os.system("rm history.txt")
