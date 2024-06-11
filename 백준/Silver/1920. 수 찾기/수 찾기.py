n = int(input())
A = sorted(list(map(int, input().split())))
m = int(input())
search_list = list(map(int, input().split()))

def binary_search(array, key, start, end):
    if (start <= end):
        mid = (start + end) // 2
        if key == array[mid]:
            print(1)
            return
        elif key < array[mid]:
            binary_search(array, key, start, mid - 1)
        else:
            binary_search(array, key, mid + 1, end)
    else:
        print(0)

for s in search_list:
    binary_search(A, s, 0, len(A)-1)