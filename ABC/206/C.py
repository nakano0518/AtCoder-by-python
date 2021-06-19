# WA
import collections
N = int(input())
li = list(map(int, input().split()))
c = collections.Counter(li)
overall = 0
for i in range(N):
  overall += i
part = 0
val = list(c.values())
for i in range(0, len(val)):
	part += (val[i]-1)
print(overall-part)