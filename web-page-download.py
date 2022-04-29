import requests
import os
import webbrowser as wb

url = input("Enter website name: ")

response = requests.get(url)

with open ("site.html","w", encoding=response.encoding) as f:
    f.write(response.text)

f_path = os.path.realpath("site.html")
print(f_path)
wb.open("file://"+f_path)
