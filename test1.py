#todo crawler the directory and search for term 
#create a hitmap and displays 
import sys 
from os import listdir
from os import scandir
from os.path import isfile
from os.path import isdir 
from os.path import join
from os import walk

term = sys.argv[1]; 
dictory = sys.argv[2]; 

target_extensions = ['txt','bat','cpp','java','sh']; 
print(term,dictory); 

def search_file(file):
    index = 0
    subject = open(file,"r");
    subject = subject.read(); 
    for line in subject:
        if term in line:
           index += 1; 
    return(index); 
    subject.close();

for root, dirs, files in walk(dictory, topdown=False):
   for name in files:
       file =join(root, name);
       for extension in target_extensions:
           print(file)
           if file[-3:len(file)] == extension or file[-2:len(file)] == extension:
              count = str(search_file(file))
              print("In File "+ file +" Occunerances "+ count); 
