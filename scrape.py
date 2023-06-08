import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.ie.service import Service


driver = webdriver.Chrome()

driver.get('https://www.woolworths.com.au/shop/browse/bakery')


