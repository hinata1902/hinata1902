#tell
import os
file=open("qqq.txt")
file.seek(10)
print(file.read())
print(file.tell())
