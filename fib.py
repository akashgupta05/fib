def f(n,c={0:0,1:1}):
	if n not in c:
		c[n]=f(n-1,c)+f(n-2,c)
	return c[n]
for k in range(int(input())):
	L,H=map(int,raw_input().split())
	s=0
	for i in range(L,H+1):
		s+= f(i)#%(10**9+7)
	print s