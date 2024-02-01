# 선택 정렬
# 1. 리스트 안에서 최솟값을 찾는다. (목표: 오름차순으로 리스트 정렬)
# 2. 맨 앞자리 수와 교환
# 3. 맨 앞을 제외한 나머지에서 반복


lst = [64, 25, 10, 22, 11]
      # 0  1   2    3   4

def SelectionSort(a,N):
    for i in range(N-1):
        min_idx = i # 최소 인덱스를 임의로 i로 가정 # 처음엔 맨 앞 0 이 됨.
        for j in range(i+1, N): # 최소 인덱스 이후 나머지들. j
            if a[min_idx]>a[j] : # 새로운 최솟값 등장하면
                min_idx = j # 변수 새로 설정
        a[i], a[min_idx] = a[min_idx], a[i] # 자리 바꾸기
        # 처음 지정한 최소 # 새로운 최소
    return a   
print(SelectionSort(lst, len(lst)))
# 오름차순 된 [10, 11, 22, 25, 64] 출력
