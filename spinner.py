import sys
import time
import threading

class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1: 
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self, message):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.write( message)
            sys.stdout.flush()
            time.sleep(self.delay) 
            sys.stdout.write('\r')
            sys.stdout.flush()

    def start(self, message):
 
        self.busy = True
        threading.Thread(target=self.spinner_task, args=(message,)).start()

    def stop(self):
        self.busy = False
        time.sleep(self.delay)
        sys.stdout.write('\r')
        sys.stdout.flush()