import os;
import sys

location = sys.argv[1];
term = sys.argv[2];
test_storage = [];
if len(term) < 5:
   print("Search term too small try with more then 5 char")
   exit();

os.system("find " + location +" -type f > history.txt");
file1 = open('history.txt', 'r')
Lines = file1.readlines()

def execute_locator(file):
    data = os.popen("cat " + file +" | python3 test2.py " + term ).read();
    data = data.strip()
    if data != "Can't read the file\n0":
       test_storage.append(data);
       print(file + " --> " + data);

for line in Lines:
    file = line.strip();
    execute_locator(file);

os.system("rm history.txt")
#print(test_storage);
