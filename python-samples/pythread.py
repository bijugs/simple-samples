import concurrent.futures
import threading
import logging
import time

sema = threading.BoundedSemaphore(2)

def thread_function(name):
  with sema:
    logging.info("Thread %s: starting:", name)
    time.sleep(2)
    logging.info("Thread %s: stopping:", name)

if __name__ == "__main__":
  
  threads = list()
  format = "%(asctime)s: %(message)s"
  logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

  for i in range(3):
    x = threading.Thread(target=thread_function, args=(i,))
    threads.append(x)
    x.start()

  for index, thread in enumerate(threads):
    thread.join()

  with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(thread_function, range(3))
