## created by: christian niebling
## 1/5/2021
## 6 words with 2 words per name is 6^2 = 36 names
##
## 36 names with 2 names per full name is 36^2 = 1296 names
##
## if full names were made up of 4 names... 36^4 = 1679616 names
import random

shuffle_switch = 1 #1=shuffle; 0=no_shuffle

file1 = open("output.txt","w+")
col_count = 10 

words = ["bran","ch","es","ca"]
names=[]

for entry in words:
    for entry2 in words:
        for entry3 in words:
            for entry4 in words:
                names.append(entry+entry2+entry3+entry4)


if shuffle_switch:    
    random.shuffle(names)
for idx, listitem in enumerate(names):
    file1.write('%s, ' % listitem)
    if(idx+1)%col_count == 0:
        file1.write('\n')
file1.close()

