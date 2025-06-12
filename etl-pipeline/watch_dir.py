'''
This script is to watch for any event of the local file directory.
When a file is saved with updates, it will generate a 'modified event', which will 
make the os.system() method run the script to transform the file and send the updates to AWS S3.
'''

import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    DIRECTORY_TO_WATCH = "/Users/binggangliu/downloads/mtest_excel"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            print("Created event- %s." % event.src_path)

        elif event.event_type == 'modified':
            print("Modified event - %s." % event.src_path)
            os.system(
                "python3 /Users/binggangliu/gitprojects/excel_realtime_to_s3.py")


if __name__ == '__main__':
    watch = Watcher()
    watch.run()
