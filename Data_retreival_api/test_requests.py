
import requests
url = "http://127.0.0.1:5000/api/stocks"
headers = {"X-API-KEY": "j5a!20kqa7s9821"}  
try:
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code) 
    print("Response:", response.text)  
    if response.status_code == 200:
        print(response.json())  
        print("Error:", response.json())  

except requests.exceptions.RequestException as e:
    print("Request Error:", e)
