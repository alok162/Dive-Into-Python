import threading
import time 

def cal_square(arr):
    for i in arr:
        time.sleep(0.2)
        print 'square ', i*i

def cal_cube(arr):
    for i in arr:
        time.sleep(0.2)
        print 'cube ', i*i*i


t = time.time()
arr = [1,2,3,4,5]
t1 = threading.Thread(target=cal_square, args=(arr, ))
t2 = threading.Thread(target=cal_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print 'total time execution ', time.time()-t



