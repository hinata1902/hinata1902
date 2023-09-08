import os
file=open("qqq.txt","r")
s=file.readlines()
for i in s:
    if(i.startswith('A')):
        print(i)
