import threading
import time

class Thread1(threading.Thread):

    def run(self):
        # Print 0,3,6...
        for i in range(0, 100, 3):
            with cond3:
                cond3.wait()
            print('[{}] - {}'.format(self.name, i))
            time.sleep(1)
            # Thread2 waiting on this
            with cond1:
                cond1.notify()

class Thread2(threading.Thread):

    def run(self):
        # Print 1,4,7...
        for i in range(1, 100, 3):
            with cond1:
                cond1.wait()
            print('[{}] - {}'.format(self.name, i))
            time.sleep(1)
            # Thread3 waiting on this            
            with cond2:
                cond2.notify()

class Thread3(threading.Thread):
        
    def run(self):
        # Print 2,5,8...
        for i in range(2, 100, 3):
            with cond2:
                cond2.wait()
            print('[{}] - {}'.format(self.name, i))
            time.sleep(1)
            # Thread1 waiting on this                        
            with cond3:
                cond3.notify()

if __name__ == "__main__":
    cond1 = threading.Condition()
    cond2 = threading.Condition()
    cond3 = threading.Condition()

    t1 = Thread1()
    t2 = Thread2()
    t3 = Thread3()

    t1.start()
    t2.start()
    t3.start()

    with cond3:
        cond3.notify()
