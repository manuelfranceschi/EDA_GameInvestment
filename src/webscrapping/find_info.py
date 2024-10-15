from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# import urllib3 # urllib3 es un cliente HTTP potente y fácil de usar para Python.
import re # Expresiones regulares 
import time
import pandas as pd

service = Service(executable_path='../webscrapping/chromedriver')
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

driver.get("http://www.google.es")