import os
file=open("qqq.txt","r")
s=file.read()
l=len(s)
for i in range(0,l):
    if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
        print(s[i])
