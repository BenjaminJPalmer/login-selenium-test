import unittest
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# TODO add csv with test data
with open(r"csv here", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    
    # Print here to check two column formatting
    print(data)

# TODO This might not work, something to test with two columns, may need refactoring
newData = []
for s in data:
    s1 = ''.join(s)
    newData.append(s1)

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def login(self):
        driver = self.driver
        # Placeholder to try with website
        driver.get(url) # TODO update url
        # self.assertIn("title", driver.title) - unnecessary assertion
        i = 1 # Again might not work, debug this

        # Loop to run through emails and passwords
        for e, p in newData:
            try:
                # Find, clear and input new email
                email = driver.find_element_by_name("email")
                email.clear()
                email.send_keys(e)

                # Find, clear and input new password
                password = driver.find_element_by_name("password")
                password.clear()
                password.send_keys(p)

                # Submit form by clicking login button
                driver.find_element_by_class_name("btn-cir").click()
            else:
                print("ERROR")

            sleep(1)
            driver.save_screenshot(i)
            i += 1
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()