# AutomatedA11y
# domain_name_fetcher.py
# Purpose: Gets the domain mame from full web link
#
# @author Lucas Silvestri
# @version 2.0

from urllib.parse import urlparse


# from https://www.taco.ryerson.ca, returns taco.ryerson.ca
def get_sub_domain(url):
    try:
        return urlparse(url).netloc + urlparse(url).path
    except:
        return ""


# from https://www.ryerson.ca, returns ryerson.ca
def get_domain_name(url):
    try:
        domain = get_sub_domain(url).split(".")
        return domain[-2] + "." + domain[-1]
    except:
        return ""


# from https://www.ryerson.ca, returns ryerson
def get_domain_no_top_level(url):
    try:
        domain = get_sub_domain(url).split(".")
        return domain[-2]
    except:
        return ""


# print(get_domain_name("http://ryerson.ca"))