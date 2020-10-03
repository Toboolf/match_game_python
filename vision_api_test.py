import http.client, urllib.request, urllib.parse, urllib.error, base64, requests

url = "https://southcentralus.api.cognitive.microsoft.com/vision/v3.0/analyze"

headers = {
  # Request headers
  'Content-Type': 'application/json',
  'Ocp-Apim-Subscription-Key': '',
}

params = urllib.parse.urlencode({
  # Request parameters
  'visualFeatures': 'categories,tags',
  'details': 'landmarks',
  'language': 'en'
})

#data = {"url": "https://matchgameimages.blob.core.windows.net/match-game/4ccc5a28-74e9-4c14-bac2-772751ad6f1c/1ca40290-4130-4c6b-9366-75dbdfb90bef.jpg"}
data = {"url": "https://matchgameimages.blob.core.windows.net/match-game/c1ea009f-bb95-49f4-a8a0-a1a7703dba17/753b486d-af36-437e-a6e4-687aa923cc17.jpg"}

def testApi():
  try:
    conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v3.0/analyze?%s" % params, "{data}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
  except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

x = requests.post(url + "?visualFeatures=Categories,Tags&details=Landmarks", json = data, headers = headers)
#print(x.text)
jsonData = x.json()
print(jsonData)

print("----")

for prop in jsonData["categories"]:
  print(prop)

print("----")

for prop in jsonData["tags"]:
  print(prop)