from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
brower = webdriver.Chrome("C:/Users/sanju/OneDrive/Desktop/Whjr/Class126/chromedriver_win32/chromedriver")
brower.get(start_url)
time.sleep(10)

def scrape():
    header = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []

    for i in range(0, 447):
        soup = BeautifulSoup(brower.page_source, "html.parser")
        
        for ul_tag in soup.find_all("ul", attrf = {"class", "exoplanets"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a"[0].contents[0]))
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
    
        brower.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    
    with open("scraper2.csv", 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(header)
        csv_writer.writerows(planet_data)

scrape()