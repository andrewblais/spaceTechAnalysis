from bs4 import BeautifulSoup
import json
import pandas as pd
from random import randint
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from webdriver_manager.chrome import ChromeDriverManager as ChDrManager


# Use os tools to improve directory location.

nsp_prefix = "https://nextspaceflight.com/launches/past/?page=" 
nsp_page = 0

# Scrape Entries Stop Point:
latest_date = "Fri Aug 7, 2020"

driver = webdriver.Chrome(service=ChService(ChDrManager().install()))

macro_list = []

stop_scrape = False

while not stop_scrape:
    try:
        nsp_page += 1
        nsp_url = f"{nsp_prefix}{nsp_page}"
        print(f"Going to Page {nsp_page}.")
        driver.get(nsp_url)
        time.sleep(randint(5, 7))
    except Exception as e:
        print(e)
        continue

    links = driver.find_elements(By.XPATH, "//*[contains(text(), 'Details')]")
    links_num = len(links)
    for link in links:
        link_num = links.index(link) + 1
        micro_dict = {}
        link.click()
        time.sleep(randint(5, 7))

        #  # #  #  # # # # #  #  # #  #
        # ↓↓ Gather and store data ↓↓ #
        #  # #  #  # # # # #  #  # #  #
        try:
            print(f"Analyzing Page {nsp_page}: Launch {link_num}/{links_num}.")
            # Print most recent main list upon iteration:
            with open("space_data_update.json", "w", encoding="utf-8") as f:
                json.dump(macro_list, f, ensure_ascii=False, indent=4)
            
            try:
                date_launch = driver.find_element(By.ID, "localized").text
                if date_launch == latest_date:
                    stop_scrape = True
                    print("Reached previously scraped items. Exiting.")
                    break
                micro_dict["Date"] = f'"{date_launch}"'
            except StaleElementReferenceException:
                pass
            except Exception as e:
                print(f"date '//br' strategy ineffective: {e}.")
                try:
                    date_xpath = driver.find_element(By.XPATH, "//br")
                    date_launch = date_xpath.get_attribute("nextSibling").strip()
                    micro_dict["Date"] = f'"{date_launch}"'
                except Exception as e:
                    print(f"Unable to parse date: {e}.")
                    pass

            rocket_container = driver.find_element(By.CSS_SELECTOR, "div[style='margin: -10px']")

            organisation = rocket_container.find_element(By.XPATH, "./div[1]")
            micro_dict["Organisation"] = organisation.text

            rocket_status = rocket_container.find_element(By.XPATH, "./div[2]")
            micro_dict["Rocket_Status"] = rocket_status.text

            loc_search = "//h3[.='Location']/following-sibling::section[1]/div[1]/h4[1]"
            location = driver.find_element(By.XPATH, loc_search).text
            micro_dict["Location"] = f'"{location}"'

            detail_01 = driver.find_element(By.CSS_SELECTOR, "span[style='color: black']").text
            detail_02 = driver.find_element(By.CSS_SELECTOR, "[style='margin-right: 40px']").text
            micro_dict["Detail"] = f"{detail_01} | {detail_02}"

            price_maybe = rocket_container.find_element(By.XPATH, "./div[3]")
            try:
                if "Price" in price_maybe.text:
                    micro_dict["Price"] = price_maybe.text
            except (NoSuchElementException, Exception) as e:
                print(e)
                pass

            mission_status = driver.find_element(By.CSS_SELECTOR, "span[style='color: white']").text
            micro_dict["Mission_Status"] = mission_status

            macro_list.append(micro_dict)
        except Exception as e:
            print(f"Iteratable issue: {e}.")
            continue
        #  # #  #  # # # # #  #  # #  #
        # ↑↑ Gather and store data ↑↑ #
        #  # #  #  # # # # #  #  # #  #

        driver.back()
        time.sleep(randint(5, 7))

    time.sleep(randint(5, 7))

driver.quit()
