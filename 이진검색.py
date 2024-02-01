arr = [2,4,5,6,8,9,13] #9 찾기
N = len(arr)
key = 9
def binarySearch(arr, N, key):
    # <구간 초기화> 인덱스를 의미함.
    start = 0 # left
    end = N-1 # right
    while start <= end: # 이것이 유효한 이내에서 계속 반복
        middle = (start + end)//2
        if arr[middle] == key : # 성공
            return middle # 인덱스
        elif arr[middle] > key:
            end = middle -1
        else:
            start = middle +1
    return -1
print(binarySearch(arr, N, key))