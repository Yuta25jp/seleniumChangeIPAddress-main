## imports
import time
import requests

from driverManager import DriverManager

def check_ip():
    res = requests.get('https://ipinfo.io').json()
    print(f" ... ip: {res['ip']}")
 
def main():
    
    check_ip()
    
    proxy_url1 = "http://172.105.238.80:1234" ## OK
    proxy_url2 = "146.56.173.210:59394" ## 表示OK、codeではダメ＝なぜ？？？
    proxy_url3 = "https://146.56.173.210:59394" ## 表示ダメ
    
    dm = DriverManager()
    dm.start_driver(False, proxy_url1)
    dm.get_source()
    
    ip_url = 'https://ipinfo.io'
    result = dm.open_page(ip_url)
    print(f" ... access was {result}")

    # dm.check_ip()
    
    # stop_tor()
    

if __name__ == "__main__":
    main()