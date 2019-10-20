import json
import turtle
import urllib.request

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('People in space: ', result['number'])

people = result['people']

for p in people:
  print(p['name'])

  if __name__ == '__main__':
    app.run(debug=True)
