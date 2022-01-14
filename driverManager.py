from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def start_driver(self, isHeadless:bool = True, proxy: str = ''):
        if self.driver is None:
            options = self.set_options(isHeadless, proxy)
            self.driver = webdriver.Chrome(executable_path=settings.BASE_PATH + "chromedriver", options=options)
            print(f" ... new driver id: {self.driver.session_id}")
        else:
            print(f" ... existing driver id: {self.driver.session_id}")

    def open_page(self, url:str):
        print(f" ... going to open page [{url}]")
        self.driver.set_page_load_timeout(20)
        try:
            self.driver.get(url)
            print(" ... URL successfully Accessed")
            WebDriverWait(self.driver, timeout=10).until(EC.presence_of_all_elements_located)
            return True
        except:
            print(" ... Page load Timeout Occured. Quiting !!!")
            return False
        
    def get_source(self):
        return self.driver.page_source
        
    def check_ip(self):
        url = 'https://ipinfo.io'
        self.open_page(url)
        self.get_data()
        
    def get_data(self):
        # xpath = '//div[@class="json-widget-entry"]'
        # elements =self.driver.find_element_by_xpath(xpath)
        elements = self.driver.find_elements(By.CLASS_NAME, "json-widget-entry")
        for i, element in enumerate(elements):
            key = element.find_element(By.CLASS_NAME, 'key').text
            value = element.find_element(By.CLASS_NAME, 'value').text
            if i == 0:
                print(f"{key}{value}")

    def close_driver(self):
        self.driver.close()

    def quit_driver(self):    
        self.driver.quit()

    def __del__(self):
        print("[driverManager]__del__")
        # if self.driver is not None:
        #     self.close_driver()
        #     self.quit_driver()

def main():
    print("main")

if __name__ == "__main__":
    main()