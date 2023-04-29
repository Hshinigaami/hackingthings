# import requests
# url = 'http://ptl-cdd9a63b-1da8636f.libcurl.so/pentesterlab;pentesterlab'
# r = requests.get(url=url)
# print(r.text)

# import requests

# r = requests.get("http://google.com")       
# print(r.status_code)

# >>> import requests
# >>> url='http://ptl-2e8b99aa-d79fcee1.libcurl.so/pentesterlab'
# >>> r=requests.get(url=url,headers={"Content-Type":"multipart/form-data"})
# >>> print(r.text)
# The key for this challenge is: 00d032b0-96e5-4801-992c-e16e5a5b56d6

# Links
# http://ptl-cfe7c419-89a65fcf.libcurl.so/pentesterlab%23pentesterlab
# 'http://ptl-cdd9a63b-1da8636f.libcurl.so/pentesterlab;pentesterlab'

# Curl Requests
# curl -vv 'http://ptl-c67feb25-e2a1c4c9.libcurl.so/pentesterlab' -F 'filename:@ola.txt' --trace-ascii -
# Here, F Option tells to upload some file to webserver, and trace-ascii option is to trace the whole scene from start to finish
# curl -vv 'http://ptl-c67feb25-e2a1c4c9.libcurl.so/pentesterlab' -F 'filename:@ola.txt;filename:../ola.txt' --trace-ascii -
# curl -vv 'http://ptl-c67feb25-e2a1c4c9.libcurl.so/pentesterlab' -F 'filename:@ola.xml' --trace-ascii - => This will upload data from local xml file, check if Content-Type is x-www-urlencoded
# curl -vv 'http://ptl-4bced050-6e3e0ee9.libcurl.so/pentesterlab' -d "<key><value>please</value></key>" -H "Content-Type: application/xml" --trace-ascii -
# curl -vv 'http://ptl-3f2a4c93-5dbba176.libcurl.so/pentesterlab' -d "<key><value>>please</value></key>" -H "Content-Type: application/xml" --trace-ascii -
# curl -vv 'http://ptl-47efecd8-8adb6fa0.libcurl.so/pentesterlab' -d @dummy.xml -H "Content-Type: application/xml" --trace-ascii -
# (If lets say we just want to insert <please> and not close this, we can send the request by XML Encoding the characters) dummy.xml => &amp;please , &lt;please&gt; , <key value="please"></key> , <key value="&quot;please"></key>
# curl -vv 'http://ptl-652ea739-8b846d3b.libcurl.so/pentesterlab' -H "Content-Type: application/json" -d '{"key":"please"}' --trace-ascii -
