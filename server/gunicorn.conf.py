import multiprocessing

bind = '127.0.0.1:1122'
workers = multiprocessing.cpu_count() + 1
user = 'ildar'
timeout = 120