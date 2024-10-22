l =[1, 23, 323, 1231, 123]
cl = []
for i in range(len(l)):
  c = l[i]
  d = l[-i]
  x = c*d
  if x%2==0:
    cl.append(x)
