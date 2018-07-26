from creepycrawler import start_crawl
import sys


def main():
    name = sys.argv[1]
    url = sys.argv[2]
    ally = sys.argv[3]
    start_crawl.main_execute(name, url, ally)
    # start_crawl.main_execute("Data Science", "https://www.ryerson.ca/graduate/datascience/", True)


if __name__ == "__main__":
    main()
