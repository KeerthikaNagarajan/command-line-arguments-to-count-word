import sys
fp=open(sys.argv[1])
data=fp.read()
words=data.split()
print("no of words",len(words))

