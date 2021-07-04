A, B = map(int, input().split())
 
if A > B:
  print('No')
else:
  if 6*A < B:
    print('No')
  elif 6*A == B:
  	print('Yes')
  else:
    if B-6*(A-1) <= 5:
      print('Yes')
    else:
      print('No')