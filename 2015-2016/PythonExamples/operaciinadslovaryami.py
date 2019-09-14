D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D['food'])
D['quantity'] += 1
print(D)

D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40

print(D)
print(D['name'])

rec  = {'name': {'first': 'Bob', 'last': 'Smith'},
        'job': ['dev', 'mgr'],
        'age': 40.5}

print(rec['name'])
print(rec['name']['last'])
print(rec['job'])
print(rec['job'][1])
rec['job'].append('janitor')
print(rec)
rec = 0
print(rec)

D = {'a': 1, 'b': 2, 'c': 3}
print(D)
Ks = list(D.keys())
print(Ks)
Ks.sort()
print(Ks)

for key in Ks:
    print(key, '=>', D[key])
for key in sorted(D):
    print(key, '=>', D[key])

for c in 'spam':
    print(c.upper())
x = 4
while x > 0:
    print('spam!' * x)
    x -= 1