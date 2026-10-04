import requests

url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"

r = requests.get(url)
print(r.text)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")

for heading in soup.find_all("h2"):
    print(heading.text)

# data = {
#     "title" : "foo",
#     "body" : "bar",
#     "userID" : 1,
# }

# headers = {
#     'Content-type' : 'application/json;charset=UTF-8',
# }

# response = requests.post(url, headers = headers, json = data)

# print(response.text)