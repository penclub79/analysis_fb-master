s = '/usr/local/bin/python'

n = s.strip('/')
n = n.split('/')
print(n)


s = s.rsplit('/', 1)
print(s)

