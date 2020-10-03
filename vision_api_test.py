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

data = {"url": "https://static.nationalgeographic.es/files/styles/image_3200/public/2928.600x450.jpg"}

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

x = requests.post(url + "?{params}", json = data, headers = headers)
print(x.text)
print(x.json())