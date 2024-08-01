import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://olympics.com/en/paris-2024/medals")

try:        
  elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "dataTables_scrollBody")))
finally:        
  print('loaded')

