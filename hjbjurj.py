#question
import os
file=open("qqq.txt","a")
f=open("newfile.txt","r")
s=f.readlines() 
for i in s:
    file.write(i)
file.close()
