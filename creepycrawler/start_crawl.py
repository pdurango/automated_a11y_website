# AutomatedA11y
# start_crawl.py
# Purpose: Get initial seed website link, executes the crawlers using multi-threading, and runs accessibility test
#
# @author Lucas Silvestri
# @version 2.0

# pip install Naked


import threading
from queue import Queue
from creepycrawler.creepy_crawler import CreepyCrawler
from creepycrawler.domain_name_fetcher import *
from creepycrawler.base_funcs import *
import time
from Naked.toolshed.shell import execute_js

start_time = time.time()


SITE_NAME = ""  # make the user fill this in
HOME_PAGE = ""
DOMAIN_NAME = ""
A11Y_AUDIT = False
QUEUE_FILE = ""
CRAWLED_FILE = ""
NUMBER_OF_THREADS = 4
queue = Queue()  # thread queue


def setup(name, home_url, ally):
    global SITE_NAME
    SITE_NAME = name
    global HOME_PAGE
    HOME_PAGE = home_url
    global DOMAIN_NAME
    DOMAIN_NAME = get_domain_name(home_url)
    global A11Y_AUDIT
    A11Y_AUDIT = ally
    global QUEUE_FILE
    QUEUE_FILE = name + "/queue.txt"
    global CRAWLED_FILE
    CRAWLED_FILE = name + "/crawled.txt"

    CreepyCrawler(SITE_NAME, HOME_PAGE, DOMAIN_NAME, A11Y_AUDIT)


# Create worker threads
def create_threads():
    for _ in range(NUMBER_OF_THREADS):
        thread = threading.Thread(target=work)
        thread.daemon = True
        thread.start()


# Do next job in queue
def work():
    while True:
        try:
            url = queue.get()
            CreepyCrawler.crawl(threading.current_thread().name, url)
            queue.task_done()
            # time.sleep(5)
        except (UnboundLocalError, TypeError, ValueError) as e:
            print('{!r}; restarting thread'.format(e))


# Each queued link is a new job
def create_jobs():
    for i in file_to_set(QUEUE_FILE):
        queue.put(i)
    queue.join()
    crawl()


# Check if items are in queue, if so then crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + " links in the queue")
        create_jobs()


def main_execute(name, url, ally):
    setup(name, url, ally)
    create_threads()
    crawl()

    if A11Y_AUDIT:
        if len(SITE_NAME) > 0:
            # js_command = "/var/www/FlaskApps/automated_a11y_website/script/auto_script2.js '" + SITE_NAME + "'" #ubuntu server
            js_command = "script/auto_script2.js '" + SITE_NAME + "'"
            success = execute_js(js_command)
            if success:
                print("Finished accessibility testing " + SITE_NAME)
            else:
                print("Problem with testing " + SITE_NAME)

    print("--- %s seconds ---" % (time.time() - start_time))
