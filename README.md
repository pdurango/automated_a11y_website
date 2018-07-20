# automated_a11y Version 2.0

automated_a11y crawls specific websites, gathers url's within, and performs a web accessibility audit for each page. The accessibility audit is completed using Pa11y. A formatted HTML document is created to display the audit details.

To use:
1. Install dependencies (Both for Javascript and Python - Review setup.py and package.json)
2. Go to main directory (automated_a11y)
3. Execute command: python3 automated_a11y.py site_name URL ally
  - "site_name" is the folder which will be made to contain crawled list and accessibility review document
  - "URL" is the starting URL for the web site to be test (Generally the home page)
  - "ally" is either of value "True" or "False", where "True runs accessibility test of each page, and "False" just crawls the      site and makes a list of pages
  - Ex: python3 automated_a11y.py DataScience https://www.ryerson.ca/graduate/datascience/ True
4. After program is finished executing, go to directory made named after "site_name". 
5. Crawled.txt contains all pages gather during the crawl and in the folder "audits", results-pally.html is the formatted        document containing audit details for each page.

Note: Crawled and queued pages saved offline so that automated_a11y can restart from where it left off.

To contact, email me at: SilveslaCreates@gmail.com
