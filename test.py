import re
import requests

url = "https://books.toscrape.com"

response = requests.get(url)

with open("web-page.html", "w") as f:
    f.write(response.text)
with open("web-page.html", "r") as fp:
    content = fp.read()

result = re.findall(r'<div class="side_categories">(.*?)</div>', content, re.M | re.DOTALL)

with open("web-page.html", "w") as fa:
    fa.write(result[0])

print(len(result))
