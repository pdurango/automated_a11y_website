# https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path#answer-40208762

# pip install selenium
# pip install axe_selenium_python
# Add $PATH to installed folder

import os
from selenium import webdriver
from axe_selenium_python import Axe
from selenium.webdriver.firefox.options import Options
from base_funcs import append_to_file, read_entire_file
from json2html import *


def site_script_axe(site_address, site_name):
    res_json = site_address.replace("https://", "").replace("http://", "").replace("www.", "").replace("/",
                                                                                                       "%2F") + ".json"
    location_json = site_name + "/audits/" + res_json

    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    driver = webdriver.Firefox(firefox_options=options)
    driver.get(site_address)

   # axe = Axe(driver.driver.find_element_by_tag_name('html').get_attribute('innerHTML'))
    axe = Axe(driver)
    axe.inject()
    results = axe.execute()

    axe.write_results(location_json, results['violations'])
    driver.close()


# Adds to html file after crawl and audit for all pages is complete
def make_html(site_name):
    location_html = site_name + "/audits/formatted-results.html"
    items = os.listdir(site_name + "/audits")

    for names in items:
        if names.endswith(".json"):
            file_name = names.replace("%2F", "/")
            location_json = site_name + "/audits/" + names
            append_to_file(location_html,
                           "\n<br><h1>" + file_name + "</h1>" + json2html.convert(read_entire_file(location_json)))

# make_html("smoradi")
