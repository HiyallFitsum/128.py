from selenium import webdriver
from bs4 import BeautifulSoup 
import time, os, ssl
import csv
import requests

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
star_table = soup.find_all('table')

table_rows = star_table[7].find_all('tr')
list = []

browser = webdriver.Chrome("D:/MyPythonCode/Web_Scraping_1/chromedriver")
browser.get(url)
time.sleep(10)


def scrape():
    headers = ["Proper name", "Distance", "Mass", "Radius"]
    star_data = []
    for i in range(0, 457):
        for td in soup.find_all("td", attrs={"class", "headerSort"}):
            td_tag = td.strip("td")
            list.append(td_tag)
            tr_tags = td.find_all("tr")
            temp_list = []
            for index, tr_tag in enumerate(tr_tags):
                if index == 0: 
                    temp_list.append(tr_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append("")
        star_data.append(temp_list)
    browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/h2[1]/span[2]/a').click()
    with open("scraper300.csv", "w")as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)

scrape()


