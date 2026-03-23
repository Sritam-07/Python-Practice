import threading
import time as tm

no_of_tickets_available = 1
lock = threading.Lock()
def do_reservation(name):
    global no_of_tickets_available
    lock.acquire()
    try:
        if no_of_tickets_available>0:
           print(f"{name} is trying for reservation..")
           tm.sleep(1)
           no_of_tickets_available-=1
           print(f"{name} has allocated tickets happy journey!")
        else:
            print(f"{name} sorry tickets were sold...")
    finally:
        lock.release()
t1=threading.Thread(target=do_reservation,args=('akash',))
t2=threading.Thread(target=do_reservation,args=('Sritam',))

t1.start()
t2.start()