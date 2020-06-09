a = "Arun Kumar Kantheti"
b = a[0:len(a):2]
print(b)
sub = 'ar'
a = a.casefold()
n = a.count(sub[0])
print(sub, "occurs", n, "number of times")
m = a.find(sub)
print(sub, 'found at location', m)
c = ['1', 'b', 'aaa', '2ak', 'tty']
d = {c[i]: i for i in range(len(c))}
print(d)
