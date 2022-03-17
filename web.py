from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
browser = webdriver.Chrome("C:/Users/yashr/Desktop/C128-main/chromedriver")
browser.get = (START_URL)

time.sleep(12)

headers = ["star","distance","mass","radius"]
planet_data = []


def scrape():
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,'html.parser')
       
        for ul_tag in soup.find_all('ul',attrs={'class','expoplanet'}):
            li_tags = ul_tag.find_all('li')
            temp_list = []
            for index , li_tag in enumerate(li_tags):
                if index == 0:

                     temp_list.append(li_tag.find_all('a')[0].contents[0] )
                else:

                     try:
                         temp_list.append(li_tag.contents[0])
                     except:
                         temp_list.append('')
            hyperlink_li_tag = li_tags[0]
            temp_list.append("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_coloum"]/footer/div/div/div/nav/span[2]/a').click()

def scrape_more_data(hyperlink):
    page = requests.get(hyperlink)

    soup = BeautifulSoup(page.content,'html.parser')
       
    for tr_tag in soup.find_all('tr',attrs={'class','fact_row'}):
            td_tags = tr_tag.find_all('td')
            temp_list = []
            for td_tag in td_tags:
                     try:
                         temp_list.append(tr_tag.find_all("div" , attrs={"class":"value"})[0].contents[0] )
                     except:
                         temp_list.append('')

scrape()
for data in planet_data:
    scrape_more_data(data[5])

final_planet_data = []

for index , li_tag in enumerate(planet_data):
    final_planet_data.append(data + final_planet_data[index])



with open('scrapper_2.csv','w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerow(planet_data)






                        

            







        
