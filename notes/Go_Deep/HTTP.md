# Notes
Escape Characters
⇒ There are total 256 number of characters in characters set which are divided into two parts ASCII and Extended ASCII and there are also escape characters
⇒ Now, this escape characters are not printed in terminal, but they are used to format the output.
⇒ Some of the escape characters used:
1. /r denotes carriage return -> Which means, move the cursor to the beginning of the line.
2. /n denotes new line -> Which means move the cursor to the new line
   1) Both above escape characters are used in terminal like this /r/n
   2) /r/n -> This means move the cursor to the begining with new line also.
3. /t => Which means tab from current cursor.
4. /b => Which means backspace in the text at this point.


## Sockets
⇒ A socket must be created and configured first -> then it must be connected to Host to send/recieve data -> Then if your purpose is done, close the connection.
⇒ Python has socket module which has similar interface as Berkey socketapi
⇒ First import the socket module, and create a object with it, it should contain two parameters -> Socket Family and Socket Type
   • Socket family starts with AF_ prefix and Socket Type starts with SOCK_ prefix
⇒ 

# Codes
## This will import requests library
import requests
import json

## Now we need to define URL and any parameters
URL = "http://ptl-6aac5b2b-38eedaa0.libcurl.so/pentesterlab"

## Now make a get request and save it in any variable, it will be a object
r = requests.get(url = URL)
print(r)

## Now convert to JSON
## Since our response is not JSON, so we need to print response.text
#data = r.json()
data = r.text

print(data)

