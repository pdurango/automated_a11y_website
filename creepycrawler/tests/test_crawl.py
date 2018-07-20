from creepycrawler import start_crawl
import unittest
import filecmp


class TestCrawl(unittest.TestCase):

    def test_crawler(self):
        file_loc = start_crawl.crawl_test("DataScience", "https://www.ryerson.ca/graduate/datascience/", True)
        self.assertEqual(filecmp.cmp(file_loc, "crawled_datascience.txt", shallow=False), True)


if __name__ == "__main__":
    unittest.main()