import requests

url = "https://flask-insta-downloader.onrender.com/get_video_link"
data = {"url": "https://www.instagram.com/reel/DMao3-rxIO8/?hl=en"}

response = requests.post(url, json=data)
print("test",response.json())
