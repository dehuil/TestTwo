#
import time
import threading
def fun1(n):
    while n>0:
        n-=1
threading.Thread(target=fun1,args=[50000000])
start=time.time()
fun1(100000000)
total=time.time()-start
print(total)