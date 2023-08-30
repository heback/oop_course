import threading
import time

done = False

def worker():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)


threading.Thread(target=worker, daemon=True).start()

input('Press enter to quit')
done = True


