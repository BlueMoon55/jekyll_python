# coding: utf -8
# 個数未定の引数を取る関数
def argtest1( *a ):
    n = len(a)
    for m in range(n):
        print( a[m] )
    return n

# メインルーチン
a = argtest1('a',1,'b',2)
print('引数の個数',a)
