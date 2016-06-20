import httplib, urllib, base64
import json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '660e9ac018c94b51b2e41db3b9b1c012',
}

params = urllib.urlencode({
})


body = {
  "documents": [
  ]
}
sinstances = []
f = open('text.json')
texts = json.load(f)
number = 0
for text in texts:
    if len(text[u'desc']) <= 2:
        continue
    number += 1
    item = {
        "text": text[u'desc'],
        "language":"en",
        "id": str(number)
    }
    body["documents"].append(item)

body = json.dumps(body)
conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, body, headers)
response = conn.getresponse()
data = response.read()
output = open('result.json', 'w')
output.write(data)
output.close( )
conn.close()