import time
import os

LOG_FILE_PATH = os.path.join("/", "Users", "gauravsarangi", "Downloads", "log-watcher", "logfile.log")

with open(LOG_FILE_PATH, 'a') as log_file:
    while True:
        log_file.write(f"Test log entry at {time.ctime()}" + "\n")
        log_file.flush()
        time.sleep(1)