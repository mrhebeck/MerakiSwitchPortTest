import requests

url = "https://dashboard.meraki.com/api/v0/devices/{INSERT YOUR NETWORK ID HERE}/switchPorts"

headers = {
    'x-cisco-meraki-api-key': "{INSERT YOUR MERAKI API KEY HERE}
    }

response = requests.request("GET", url, headers=headers)

print(response.text)