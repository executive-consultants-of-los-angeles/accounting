import yaml

f = open('/srv/accounting/transaction/yml/transaction.yml', 'r')
d = f.read()
f.close()

print(d)
