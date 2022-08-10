import threading
import time

def requsicao_web():
    print("Fazendo...")
    time.sleep(3)
    print("Terminou...")

    thread_1 = threading.Thread(target=requsicao_web)
    thread_1.start()

    thread_2 = threading.Thread(target=requsicao_web)
    thread_2.start()

    thread_3 = threading.Thread(target=requsicao_web)
    thread_3.start()






