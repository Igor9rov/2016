S = 'Spam'
print(len(S))
print(S[0])
print(S[1])
print(S[1:3])
print(S[:-1])
print(S[:])
print((S+'xyz')* 8)
print(S.find('pa'))
print(S.replace('pa', 'XYZ'))

line = 'aa,bbbb,ccc,dd'
print(line.split(','))
s = 'spam'
print(s.upper())
print(s.isalpha(), s.isdigit())
line = 'aa,bbbb,ccc,dd\n'
line = line.rstrip()
print(line)
print('%s, eggs, and %s' % ('spam', 'SPAM!' ))
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))
print(dir(s))
print(help(s.replace))