import time
from threading import *
class Flight:
    def __init__(self,available_seat):
        self.available_seat = available_seat
        self.l = Lock()
        # print(self.l)
    def reverse(self,need_seat):
        self.l.acquire()
        # print(self.l)
        # self.l.acquire(blocking=True,timeout=-1)
        print('Available Seat: ',self.available_seat)
        if(self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat},seat is a allocated for {name}')
            self.available_seat -= need_seat
            time.sleep(2)
        else:
            print('Sorry! All seats has allocated.')
        self.l.release()
f = Flight(2)
t1 = Thread(target=f.reverse,args=(1,),name='snehal')
t2 = Thread(target=f.reverse,args=(1,),name='satabdi')
t3 = Thread(target=f.reverse,args=(1,),name='Raja')
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("main thread")