import os 
import time 
a = ""
for i in range(1000000): #a = 1MB
    a += "0"
size = input("Enter the size of the file: ")
b = ""
for i in range(100): #b = 100MB
    b += a

print size
print ""
f= open("stf.txt","w+")
start = time.time()
for i in range(10*size):
    os.system("clear")
    print i
    percent = float(i)/(size)*10
    print percent
    prevtime = time.time()-start
    try:one = float(prevtime) / percent 
    except:
        one = 0
    print "ETA:{}".format(str((100-percent)*one))
    f.write(b)
    
