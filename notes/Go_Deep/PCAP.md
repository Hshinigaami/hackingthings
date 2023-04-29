1. To check what all protocols are doing over the whole network, just right click on one packet, and Follow -> TCP Stream
2. Telnet connections are insecure since they are not wired over encrypted channel, so password is logged in plain text.
3. Similar to telnet, if ftp is not used over TLS(Transport level security), plain text is visible.
4. If there are multiple tcp connections are made, we can filter them, by tcp.stream eq 0 or tcp.stream eq 1
5. rsh connection stores client IP in rhosts file of server, which can be used to connect to server again without requiring creds.
6. rlogin connection, will store creds in plain text ... insecure.
7. SMTP Connection can store subject,body,sender,reciever,password(base64).
8. While transferring mail/attachements from client to server..it is encoded using uuencode, this text begins with begin key.unzip ... end
   To decode this, copy whole text from begin to end, and decode it using uudecode, to get the zip file/attachements.
9. URI Parameters and post body parameters also stores keys in plain text. 
10. Response containing gzip/deflate values, can be extracted by adding magic bytes of gzip... since even after we save the response containing gzip, it might not be extractable... so try to add magic bytes.
11. If encoding is in form of chunk encoding then, it means some part of chunk is sent before sending whole response. In response you would see, a hexadecimal value(Size of chunk) followed by chunk.
12. DNS Traffic can be passed through TCP Channel as well instead of UDP.
13. If client asks for TXT Record and not for A record, this can still be traced. Asking for records means they are asking for IP from a hostname.
14. When trying to access one IP, it can consist of multiple TLS Servers. So if client is trying to access google.com but TLS Server sends cert of bing.com then client will reject it, This is not handled by TCP Level, so to avoid this issues, client sends the Certificate with a S.N.I(Server Name Indication) Number.