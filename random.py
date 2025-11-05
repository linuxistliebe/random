import random
import time
n=0
while True:
    a,b,c=random.randint(1,3),random.randint(1,3),random.randint(1,3)
    print(a,b,c)
    n=n+1
    if a==1 and b==2 and c==3:
        print("Match Found")
        break
    time.sleep(2)
    
print("Loop ran",n,"times")
