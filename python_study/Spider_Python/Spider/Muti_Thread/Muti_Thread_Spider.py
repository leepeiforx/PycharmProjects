import _thread
import threading
import time


def print_time(threadName, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(threadName, time.ctime())


# _thread.start_new_thread(print_time, ('Thread1', 1))
# _thread.start_new_thread(print_time, ('Thread2', 2))


class myThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self) -> None:
        print('Starting' + self.name)
        print_time(self.name, self.delay)


threads = []

# 创建新进程\
thread1 = myThread('Thread1',1)
thread2 = myThread('Thread2',2)

# 开启新进程
thread1.start()
thread2.start()