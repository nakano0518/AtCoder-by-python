import math
P = int(input())
li = [0]
for i in range(1, 11):
  li.append(math.factorial(i))
idx = 0
#print(li)
for i in range(1, 11):
  if li[i] > P:
    idx = i-1
    break
else:
  idx = 10
#print(li[idx])
 
cnt = 0
 
for j in range(idx, 0, -1):
  if li[j]*100 <= P:
    P = P - li[j]*100
    cnt += 100
  else:
    quotient = (P//li[j])
    P = P - li[j]*quotient
    cnt += quotient
  #print('P='+str(P)+'cnt='+str(cnt))
  if P == 0:
    break
print(cnt)