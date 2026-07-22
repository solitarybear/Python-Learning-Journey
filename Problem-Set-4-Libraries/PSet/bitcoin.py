import resource
resource.setrlimit(resource.RLIMIT_AS, (2*1024*1024*1024, resource.RLIM_INFINITY))
import requests
import sys

if len(sys.argv) < 2:
    sys.exit("missing command line argument")

try:
    unit = float(sys.argv[1])
except ValueError:
    sys.exit("command line argument is not a number")

api_key = "put your api key here"

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + api_key)
except requests.RequestException as e :
    print(f"Error occurred i.e. {e}")
o = response.json()

data  = o["data"]

print(f"${float(data['priceUsd'])*unit:,.4f}")
