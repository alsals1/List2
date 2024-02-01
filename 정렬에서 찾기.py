a = [2,4,7,9, 11]
#    0 1 2 3  4
key = 9
# ind : 3 찾기
n = len(a)
# 전체 리스트의 길이

def sequentialSearch(a, n, key): # a 리스트, n 길이, key 목표
    i = 0
    while i < n and a[i]<key:
        i = i+1
    if i < n and a[i] == key:
        return i
    else:
        return -1
    
print(sequentialSearch(a,n,key)) # 3 출력
