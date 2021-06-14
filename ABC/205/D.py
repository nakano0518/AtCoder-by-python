# 下記TLEとなった
# 制約がKが10^8と大きいので、Nが小さくてQが小さかったとしても
# A以外の数の列挙数が膨大になるのでTLEになってしまう。。列挙せずに回答しないといけない。
# N, Q = map(int, input().split(' '))
# A = list(map(int, input().split(' ')))
# B = [int(input()) for _ in range(0, Q)]
# maxInt = max(A+B)
# ans_li = list(set([int(i) for i in range(1, maxInt+N+1)])-set(A))
# for i in range(0, Q):
#   print(ans_li[B[i]-1])


# 上記TLE解消コード
import sys
from bisect import bisect_left # 二分探索 (左側の境目を見つける)
N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
INF = sys.maxsize
for i in range(Q):
    K = int(input())
    left = 0
    right = INF
    while right-left > 1:
        mid = (left+right)/2
        d = bisect_left(A, mid)
        
    