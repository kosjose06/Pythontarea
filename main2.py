from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome('C:/Selenium/chromedriver.exe')
driver.maximize_window()
driver.delete_all_cookies()
driver.get('https://www.amazon.com/')


driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("HP Pavilion azul")

driver.find_element(By.ID, 'nav-search-submit-button').click()

driver.find_element(By.XPATH, './/a[contains(@class, "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")]').click()

driver.find_element(By.ID, 'quantity').send_keys(2)
driver.find_element(By.ID, 'add-to-cart-button').click()
driver.find_element(By.ID, 'sw-gtc').click()

driver.implicitly_wait(10)

driver.quit()