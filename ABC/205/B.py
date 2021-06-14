n = int(input())
s = set(list(map(int, input().split(' '))))
s1 = set([i for i in range(1, n+1)])
 
if s == s1:
  print('Yes')
else:
  print('No')