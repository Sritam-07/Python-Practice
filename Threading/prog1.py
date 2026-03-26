import threading
import time


def func(seconds):
    thread_name = threading.current_thread().name
    print(f"sleeping for {seconds} seconds\n")
    time.sleep(seconds)
    print(f"{thread_name} hello")
    
t1 = threading.Thread(target=func,args=(5,))
t2 = threading.Thread(target=func,args=(2,))

t1.start()
t2.start()
# func(5)
 