import random
import csv
a=[]
i=0
with open('new.csv','w') as f:
    write=csv.writer(f)
    for j in range(1000):
        r=random.randrange(0,50)
        ind=random.randrange(0,20)
        for i in range(2):
            a=[r,ind]
        write.writerow(a)
    
    
