import requests

r = requests.get('https://api.github.com/repos/sgtlucero1/python-sandbox/events')
data = r.json()
print(data)
print("Output:")
print(f"First event id: {data[0]['actor']['login']}")
