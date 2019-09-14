L = [123, 'spam', 1.23]
print(len(L))
print(L[0])
print(L[:1])
print(L + [4, 5 , 6])
print(L)

L.append('Ni')
print(L)
L.pop(2)
print(L)

M = ['bb', 'aa', 'cc']
M.sort()
print(M)

M.reverse()
print(M)

k = []
k.append(1)
print(k)
k = [2,4,7,8,7]
k.pop()
print(k)

L = [1,2,2,2,2, 'kek', 'kek']
L= list(set(L))
print(L)