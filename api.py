import requests

response=requests.get("https://randomuser.me/api")
print (response.status_code)
print(response.json())

# gender =response.json()["results"][0]["gender"]
# print(gender)

first_name=response.json()["results"][0]["name"]["first"]
print(first_name)


last_name=response.json()["results"][0]["name"]["last"]
print(last_name)

# print(f"{first_name} {gender}")