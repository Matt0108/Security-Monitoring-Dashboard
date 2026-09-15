from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os


class Monitor(FileSystemEventHandler):

    def on_modified(self, event):
        if not event.is_directory:
            print(f"FILE MODIFIED: {event.src_path}")

    def on_created(self, event):
        if not event.is_directory:
            print(f"FILE CREATED: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"FILE DELETED: {event.src_path}")


folder_to_watch = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "test_files"
)

event_handler = Monitor()
observer = Observer()

observer.schedule(
    event_handler,
    folder_to_watch,
    recursive=True
)

observer.start()

print("Security Monitor Running")
print(f"Watching: {folder_to_watch}")
print("Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()