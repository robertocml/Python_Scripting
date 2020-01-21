from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import pandas as pd
import time
path = 'C:\Users\rober\Downloads\archives\chromedriver_win32'
chrome_options = Options()
chrome_options.add_argument("- incognito")