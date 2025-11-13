import os, time
LOG_DIR = "/var/log"
DAYS = 7
now = time.time()
for root, dirs, files in os.walk(LOG_DIR):
    for f in files:
        path = os.path.join(root, f)
        if os.path.isfile(path) and now - os.path.getmtime(path) > DAYS*86400:
            try:
                os.remove(path)
            except PermissionError:
                pass
