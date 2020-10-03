import http.client, urllib.request, urllib.parse, urllib.error, base64

headers_vision = {'Ocp-Apim-Subscription-Key': 'API-KEY'}
vision_base_url = "https://southcentralus.api.cognitive.microsoft.com/vision/v2.0/"​

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'API-KEY',
}

params = urllib.parse.urlencode({
    # Request parameters
    'visualFeatures': 'Categories',
    'details': '{string}',
    'language': 'en',
})

try:
    conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v3.0/analyze?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))