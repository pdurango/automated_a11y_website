# AutomatedA11y
# base_funcs.py
# Purpose: Create basic functions to make a directory and files as well as interact with them
#
# @author Lucas Silvestri
# @version 2.0


import os
import sys


# each website crawled_set creates a new directory
def create_project_dir(dirs):
    if not os.path.exists(dirs):
        print("Creating website directory: " + dirs)
        os.makedirs(dirs)
    audits_path = dirs + "/audits/"
    if not os.path.exists(audits_path):
        os.makedirs(audits_path)


# Create queue_set and crawled_set files (if not created)
def create_files(site_name, start_url):
    queue_set = site_name + "/queue.txt"
    crawled_set = site_name + "/crawled.txt"
    # formatted_html = site_name + "/audits/formatted-results.html"
    if not os.path.isfile(queue_set):
        write_new_file(queue_set, start_url)
    if not os.path.isfile(crawled_set):
        write_new_file(crawled_set, "")
    # if not os.path.isfile(formatted_html):
    #     write_new_file(formatted_html, "")


def check_for_files(site_name):
    files = False
    queue_set = site_name + "/queue.txt"
    crawled_set = site_name + "/crawled.txt"
    #formatted_html = site_name + "/audits/formatted-results.html"
    num_lines = sum(1 for line in open(crawled_set))
    # if num_lines > 200:
    # sys.exit(0)
    if os.path.isfile(queue_set):
        files = True
    if os.path.isfile(crawled_set):
        files = True
    # if os.path.isfile(formatted_html):
    #     files = True
    return files


# Creates new file
def write_new_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close


# Adds data to existing file (created via write_new_file)
def append_to_file(path, data):
    with open(path, "a") as file:
        file.write(data + "\n")


def read_entire_file(file):
    f = open(file, "r")
    if f.mode == "r":
        contents = f.read()
    return contents


# Deletes contents of file
def delete_file_contents(path):
    # with open(path, "w"):
    # pass
    open(path, 'w').close()


# Read a file and convert contents to a Set (delete duplicates)
def file_to_set(file):
    results = set()
    with open(file, "rt") as f:
        for item in f:
            results.add(item.replace("\n", ""))
    return results


def set_to_file(links, file_name):
    with open(file_name, "w") as f:
        for l in sorted(links):
            f.write(l + "\n")

# print("hello")
# create_project_dir("yiiframework")
# create_files("yiiframework", "http://www.yiiframework.com/")
