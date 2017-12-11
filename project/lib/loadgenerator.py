from threading import Thread
import requests
import time
import json

start_time = time.time()

def fetch_url(url, interval):
    response = requests.get(url)

    print("'%s\' fetched in %ss" % (url, (time.time() - start_time)))
    print('Results - ' + response.text)

    time.sleep(interval)

def load_server(url, concurrent_calls, interval, iterations):
    for iteration in range(iterations):
        threads = [Thread(target=fetch_url, args=(url, interval)) for i in range(concurrent_calls)]

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
