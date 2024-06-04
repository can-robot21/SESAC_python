# 이진 탐색 ( binary_search )

def binary_search(list, target):
    left = 0
    right = len(list) - 1
    
    while left <= right:
        mid = (left +right) // 2
        if list[mid] == target:
            return mid  #정답 찾기
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1

