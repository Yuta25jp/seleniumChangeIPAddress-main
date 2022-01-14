## imports
import time
import subprocess
import urllib.request, urllib.error

from driverManager import DriverManager

def start_tor():
    print(' ... going to start tor')
    args = ['brew', 'services', 'start', 'tor']
    subprocess.call(args)
    
def reload_tor():
    print(' ... going to change ip')
    args = ['brew', 'services', 'reload', 'tor']
    subprocess.call(args)

    # res = requests.get('https://ipinfo.io').json()
    # print(res)

def stop_tor():
    print(' ... going to end tor')
    args = ['brew', 'services', 'stop', 'tor']
    subprocess.call(args)

 
def main():
    start_tor()
    
    dm = DriverManager()
    dm.start_driver(False, 'tor')

    dm.check_ip()
    
    # reload_tor()
    time.sleep(10)
    
    dm.check_ip()
    
    stop_tor()
    

if __name__ == "__main__":
    main()