#!/usr/bin/env python3
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from unicodedata import normalize
import string

def remove_control_characters(text):
    return ''.join(char for char in text if char in string.printable)

def save_html(url):
    print(url)
    # Start a new browser session
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (without opening browser window)

    driver = webdriver.Chrome(options=options)
#    driver = webdriver.Chrome()

    # Fetch the web page
    driver.get(url)

    # Wait for 10 seconds
    time.sleep(10)

    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    # print(html)
    if html == None:
       return

    # Save the HTML file
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style", "link", "title"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # Get the base file name from the url
    file = url.split('/')[-1]

    # Write the text from the HTML
    text_path = f"text2/{file}.txt"
    with open(text_path, 'wt', encoding="utf-8") as f:
        f.write(text)

    html_path = f"html/{file}.html"
    with open(html_path, 'wt', encoding="utf-8") as g:
        g.write(html)

    # Close the browser session
    driver.quit()

# Read the list of URLs from an input file
with open('urls.txt', 'r') as file:
    urls = file.read().splitlines()

# Process each URL
for url in urls:
    save_html(url)
