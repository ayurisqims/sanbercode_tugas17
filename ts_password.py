import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TS_PASSWORD(unittest.TestCase): 

        def test_002_invalid_password_alphanumeric(self): #fungsi def yaitu untuk menjelaskan bawah test_login adalah fungsi
                driver = self.driver
                driver.get('https://www.saucedemo.com/') #untuk membuka web browser
                time.sleep(3)
                driver.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("standard_user")
                time.sleep(1)
                driver.find_element(By.ID,"password").send_keys("secret_sauce1223234")
                time.sleep(1)
                driver.find_element(By.ID,"login-button").click()

                response_message = driver.find_element(By.XPATH,"//div[@id='login_button_container']//form//h3").text

                self.assertEqual(response_message, "Epic sadface: Username and password do not match any user in this service")

        def test_003_invalid_password_spesial_karakter(self): #fungsi def yaitu untuk menjelaskan bawah test_login adalah fungsi
                driver = self.driver
                driver.get('https://www.saucedemo.com/') #untuk membuka web browser
                time.sleep(3)
                driver.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("standard_user")
                time.sleep(1)
                driver.find_element(By.ID,"password").send_keys("!@#!@#!@")
                time.sleep(1)
                driver.find_element(By.ID,"login-button").click()

                response_message = driver.find_element(By.XPATH,"//div[@id='login_button_container']//form//h3").text

                self.assertEqual(response_message, "Epic sadface: Username and password do not match any user in this service")

        def test_003_invalid_password_kosong(self): #fungsi def yaitu untuk menjelaskan bawah test_login adalah fungsi
                driver = self.driver
                driver.get('https://www.saucedemo.com/') #untuk membuka web browser
                time.sleep(3)
                driver.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("abcdje")
                time.sleep(1)
                driver.find_element(By.ID,"password").send_keys("  ")
                time.sleep(1)
                driver.find_element(By.ID,"login-button").click()

                response_message = driver.find_element(By.XPATH,"//div[@id='login_button_container']//form//h3").text

                self.assertEqual(response_message, "Epic sadface: Username is required")

unittest.main()