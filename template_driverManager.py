import os
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import settings

# _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_

class DriverManager(object):

    def __init__(self):
        self.driver = None

    def set_options(self, isHeadless:bool, proxy:str):
        proxy_url = ""
        if proxy == "tor":
            # tor 利用する場合
            proxy_url = "socks5://localhost:9050"
        else:
            # tor 利用しない場合
            proxy_url = proxy

        options = webdriver.ChromeOptions()
        if isHeadless:
            options.add_argument('--headless')
        if len(proxy_url) > 0:
            print(f" ... setted [{proxy_url}] as Proxy")
            options.add_argument('--proxy-server=%s' % proxy_url)
        options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option("detach", True)
        return options

    def start_driver(self, isHeadless:bool, proxy:str):
        if self.driver is None:
            options = self.set_options(isHeadless, proxy)
            self.driver = webdriver.Chrome(executable_path=settings.BASE_PATH + "chromedriver", options=options)
            print(f" ... new driver id: {self.driver.session_id}")
        else:
            print(f" ... existing driver id: {self.driver.session_id}")

    def open_page(self, url):
        print(f" ... going to open page [{url}]")
        self.driver.get(url)
        WebDriverWait(self.driver, timeout=10).until(EC.presence_of_all_elements_located)

    def get_source(self):
        return self.driver.page_source

    def get_page_url(self):
        return self.driver.current_url

    def get_element(self, xpath: str):
        element = self.driver.find_element_by_xpath(xpath)
        return element

    def get_elements_count(self, xpath: str):
        elements = self.driver.find_elements_by_xpath(xpath)
        print(f" ... the count was {len(elements)}!")

    def get_elements(self, xpath: str):
        elements = self.driver.find_elements_by_xpath(xpath)
        return elements

    def select(self, xpath: str, select_index: int):
        select_element = self.driver.find_elements_by_xpath(xpath)
        selector = Select(select_element[0])
        selector.select_by_index(select_index)

    def set_input(self, xpath: str, index: int, input: str):
        """Set html input text"""
        time.sleep(0.5)
        input_elements = self.driver.find_elements_by_xpath(xpath)
        print(f" ... found {len(input_elements)} inputs")
        # if index > len(input_elements) - 1:
            # raise chrome_error.ChromeElementCountError
        input_elements[index].send_keys(input)

    def limit_element(self, xpath: str):
        time.sleep(2)
        element = self.driver.find_element_by_xpath(xpath)
        return element

    def click_element_by_tag(self, element:WebElement, tag: str):
        button = element.find_element_by_tag_name(tag)
        button.click()

    def click_element(self, xpath: str, index: int):
        """Click element"""
        # WAIT = WebDriverWait(self.driver, 10)
        # element = WAIT.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        # element.click()
        time.sleep(3)
        elements = self.driver.find_elements_by_xpath(xpath)
        print(f" ... found {len(elements)} element for click")
        # if index > len(elements) - 1:
            # raise chrome_error.ChromeElementCountError
        elements[index].click()
        time.sleep(2)

    def click_a_tag_from_element(self, element):
        element = element.find_element_by_tag_name("a");
        element.click()

    def scrape_xpath_elements(self, xpath:str):
        elements = self.driver.find_elements_by_xpath(xpath)
        return elements

    def scrape_css_element(self, css:str):
        elements = self.driver.find_elements_by_css_selector(css)
        print("css", len(elements))
        return elements

    def scrape_name_element(self, name:str):
        elements = self.driver.find_elements_by_class_name(name)
        print("name", len(elements))
        return elements

    def scrape_xpath_element(self, xpath:str):
        element = self.driver.find_element_by_xpath(xpath)
        return element

    def scrape_text_from_elements(self, xpath:str, index:int):
        text = ""
        elements = self.driver.find_elements_by_xpath(xpath)
        if len(elements) > 0:
            text = elements[index].text
        return text

    def scrape_text_from_element(self, xpath:str):
        text = self.driver.find_element_by_xpath(xpath).text
        return text

    def scrape_herf(self, xpath:str):
        href = self.driver.find_element_by_xpath(xpath).get_attribute("href")
        return href

    def scrape_tags(self, element, tag_name:str):
        tag = element.find_elements_by_tag_name(tag_name)
        return tag

    def scrape_tag(self, element, tag_name:str):
        tag = element.find_element_by_tag_name(tag_name)
        return tag

    def scrape_text_from_tag(self, element, tag_name:str):
        text = element.find_element_by_tag_name(tag_name).text
        return text

    def scroll_to_element(self, xpath:str):
        self.driver.find_element_by_xpath(xpath).location_once_scrolled_into_view

    def navigate_back(self):
        self.driver.back()

    def close_driver(self):
        self.driver.close()

    def quit_driver(self):    
        self.driver.quit()

    def __del__(self):
        print("[driverManager]__del__")
        # if self.driver is not None:
        #     self.close_driver()
        #     self.quit_driver()

# main処理
def main():
    print("main")

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()