import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = {
	"q": "Hello, world!",
	"target": "uz",
	"source": "en"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "7fa97f1552msh0b1cfd81a9a9ad5p162bbajsnd5687cbae1b2",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())


