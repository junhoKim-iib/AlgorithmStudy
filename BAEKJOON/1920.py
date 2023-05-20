N = int(input())
check_list = list(map(int, input().split()))

M = int(input())
test_list = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    
check_list.sort()

for i in test_list:
    result = binary_search(check_list, i, 0, N-1)
    if result == None:
        print(0)
    else:
        print(1)