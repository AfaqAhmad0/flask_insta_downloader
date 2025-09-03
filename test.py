import requests

url = "http://127.0.0.1:5000/get_video_link"
data = {"url": "https://www.instagram.com/reel/DMao3-rxIO8/?hl=en"}

response = requests.post(url, json=data)
print("test",response.json())
