import threading, time
class ThreadEx(threading.Thread):
    def run(self) -> None:
        for i in range(10):
            print(f"id : {self.getName()}, {i}")
            time.sleep(1)
for i in range(2):
    th = ThreadEx()
    th.start()