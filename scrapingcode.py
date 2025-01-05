
#purpose: takes website url and returns all the content from that website

import selenium.webdriver as webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
AUTH = 'brd-customer-hl_fdb78836-zone-webscraper:xjndx7pkzk97' #connecting to a remote browser instance
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

#scraping file using selenium modules/classes
def scrape_website(website):
    print("Launching Chrome Browser")

    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating...')
        driver.get(website)
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('./page.png')
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html





#parsing the website (html) using beautiful soup to view DOM content (menus, sidebars, login, data, etc...)

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content: #if the body exists, return it, otherwise return an empty string (for no errors)
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')

    #looks inside the parsing contents for scripts and tags and removes them (Don't need extra characters)
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator='\n')
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip()) # removes all empty text strings
    return cleaned_content




#split the content into batches (There is a limit for 8000 characters so the text needs to be split into small batches to be processed past the limit)
def split_dom_content(dom_content, max_length = 6000): #make the max of each batch 6000 characters
    return[dom_content[i : i +max_length] for i in range(0, len(dom_content), max_length)] #iterates through 6000 characters and then goes to the next 6000 characters until end of dom content


