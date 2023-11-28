import threading
import time

start_time = time.time()
def task1():
    print("Task 1 is starting...")
    time.sleep(2)
    print("Task 1 is done.")
def task2():
    print("Task 2 is starting...")
    time.sleep(3)
    print("Task 2 is done.")
def task3():
    print("Task 3 is starting...")
    time.sleep(5)
    print("Task 3 is done.")

thread_1 = threading.Thread(target=task1)
thread_2 = threading.Thread(target=task2)
thread_3 = threading.Thread(target=task3)

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()

end_time = time.time()
print(f"Execution time : {end_time - start_time}")
print("All tasks have finished.")
