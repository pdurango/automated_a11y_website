# AutomatedA11y
# creepy_crawler.py
# Purpose: Creates a crawler that traverses though webpafes and collects links. It then adds those lnks to a queue until it is their turn to be traversed. After being traversed, the link is moved to a crawled list.
#
# @author Lucas Silvestri
# @version 2.0

from urllib.request import urlopen
import urllib.request
from creepycrawler.link_spy import LinkSpy
from creepycrawler.base_funcs import *
# from script import site_script_axe


class CreepyCrawler:
    # Class variables (shared between all CreepyCrawlers)
    site_name = ""
    home_url = ""
    domain_name = ""
    queue_set = set()
    crawled_set = set()
    focused_set = set()
    queue_file = ""
    crawled_file = ""
    temp_html_string = ""
    a11y_audit = None

    def __init__(self, site_name, home_url, domain_name, a11y_audit):
        CreepyCrawler.site_name = site_name
        CreepyCrawler.home_url = home_url
        CreepyCrawler.domain_name = domain_name
        CreepyCrawler.a11y_audit = a11y_audit
        CreepyCrawler.queue_file = CreepyCrawler.site_name + "/queue.txt"
        CreepyCrawler.crawled_file = CreepyCrawler.site_name + "/crawled.txt"
        self.start()
        self.crawl("First CreepyCrawler ", CreepyCrawler.home_url)

    @staticmethod
    def start():
        create_project_dir(CreepyCrawler.site_name)
        create_files(CreepyCrawler.site_name, CreepyCrawler.home_url)
        CreepyCrawler.queue_set = file_to_set(CreepyCrawler.queue_file)
        CreepyCrawler.crawled_set = file_to_set(CreepyCrawler.crawled_file)

    @staticmethod
    def crawl(thread, page_url):
        if page_url not in CreepyCrawler.crawled_set:
            print(thread + " is currently crawling " + page_url)
            print("Queue: " + str(len(CreepyCrawler.queue_set)) + " ....... Crawled: " + str(
                len(CreepyCrawler.crawled_set)))
            CreepyCrawler.add_links_to_queue(CreepyCrawler.collect_links(page_url))
            # print("collect_links called")

            try:
                CreepyCrawler.queue_set.remove(page_url)
                CreepyCrawler.crawled_set.add(page_url)
            except KeyError as e:
                print('{!r}; Not found'.format(e))

            CreepyCrawler.update_files()

    @staticmethod
    def collect_links(page_url):
        html_string = ""
        # print("page url" + page_url)
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'CreepyCrawler-LS/2.0')]
        #print("COLLECT " + page_url)

        # if CreepyCrawler.a11y_audit:
        #     site_script_axe(page_url, CreepyCrawler.site_name)

        try:
            response = urlopen(page_url)
            # if response.getHeader("Content-Type") == 'text/html': TheNewBostons code
            if 'text/html' in response.getheader('Content-Type'):  # comment fix code ep 15
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
                #print(html_string)
                spy = LinkSpy(CreepyCrawler.home_url, page_url)
                spy.feed(html_string)
            return spy.page_link_set()
        except:
            # print("Error: Can't crawl page")
            return set()

    @staticmethod
    def add_links_to_queue(links=None):
        if links is None:
            pass
        else:
            for url in links:
                if url in CreepyCrawler.queue_set:
                    continue
                if url in CreepyCrawler.crawled_set:
                    continue
                # COMMENT THE FOLLOWING IF STATEMENT TO ALLOW CRAWLER TO CRAWL OUTSIDE OF ORIGINAL WEBSITE
                if CreepyCrawler.domain_name not in url:  # This stops crawler from adding links from other domains
                    # besides main domain (Crawler will only crawl "site_name" domain)
                    continue
                if "javascript" in url:
                    continue
                #May not work - Test Arts site
                if url.endswith(".html"):
                    short = url[:-5]
                    short = short + "/"
                    if short in CreepyCrawler.crawled_set or short in CreepyCrawler.queue_set:
                        continue
                if url.endswith("/"):
                    short = url[:-1]
                    short = short + ".html"
                    if short in CreepyCrawler.crawled_set or short in CreepyCrawler.queue_set:
                        continue
                if "#" in url:
                    continue

                CreepyCrawler.queue_set.add(url)

    @staticmethod
    def update_files():
        set_to_file(CreepyCrawler.queue_set, CreepyCrawler.queue_file)
        set_to_file(CreepyCrawler.crawled_set, CreepyCrawler.crawled_file)

    @staticmethod
    def check_page_limit():
        # FOLLOWING CODE LIMITS CRAWL TO 200 PAGES
        temp = len(CreepyCrawler.crawled_set)
        if temp > 10:
            print("100 page limit crawled. Focused crawl closing...")
            #quit()
            return True
        else:
            return False
