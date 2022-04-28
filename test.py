import requests
import sys

img_url = sys.argv[1]
img_name = sys.argv[2]

response = requests.get(img_url)

with open(img_name+".jpg", "wb") as f:
    f.write(response.content)


