import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TS_USERNAME(unittest.TestCase): 

        def setUp(self): 
                self.driver = webdriver.Chrome(executable_path="./Belajar QA/chromedriver.exe")

        def test_002_invalid_username_alphanumeric(self): #fungsi def yaitu untuk menjelaskan bawah test_login adalah fungsi
                driver = self.driver
                driver.get('https://www.saucedemo.com/') #untuk membuka web browser
                time.sleep(3)
                driver.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("standard_1234")
                time.sleep(1)
                driver.find_element(By.ID,"password").send_keys("secret_sauce")
                time.sleep(1)
                driver.find_element(By.ID,"login-button").click()

                response_message = driver.find_element(By.XPATH,"//div[@id='login_button_container']//form//h3").text

                self.assertEqual(response_message, "Epic sadface: Username and password do not match any user in this service")

        def test_003_invalid_username_spesial_karakter(self): #fungsi def yaitu untuk menjelaskan bawah test_login adalah fungsi
                driver = self.driver
                driver.get('https://www.saucedemo.com/') #untuk membuka web browser
                time.sleep(3)
                driver.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("@!#@#$#@")
                time.sleep(1)
                driver.find_element(By.ID,"password").send_keys("secret_sauce")
                time.sleep(1)
                driver.find_element(By.ID,"login-button").click()

                response_message = driver.find_element(By.XPATH,"//div[@id='login_button_container']//form//h3").text

                self.assertEqual(response_message, "Epic sadface: Username and password do not match any user in this service")

        def test_003_invalid_username_kosong(self): #fungsi def yaitu untuk menjelaskan bawah test_login adalah fungsi
                driver = self.driver
                driver.get('https://www.saucedemo.com/') #untuk membuka web browser
                time.sleep(3)
                driver.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("abcdje")
                time.sleep(1)
                driver.find_element(By.ID,"password").send_keys("secret_sauce")
                time.sleep(1)
                driver.find_element(By.ID,"login-button").click()

                response_message = driver.find_element(By.XPATH,"//div[@id='login_button_container']//form//h3").text

                self.assertEqual(response_message, "Epic sadface: Username is required")
unittest.main()
