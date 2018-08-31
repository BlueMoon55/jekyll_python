# coding: utf -8
import sys
s = sys.stdin.readline()
print (s)

lst = ['a','b','c','d']
try:
    n = lst.index('d')
    print(n," 番目にあります．")
except ValueError:
    print (" 要素が見つかりません…")

s = {4,1,3,2,1,3,4,2}
print (s)
