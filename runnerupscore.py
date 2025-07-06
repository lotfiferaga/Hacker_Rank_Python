if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    highest = max(arr)
    arr_without_highest = [x for x in arr if x!= highest]
    print(max(arr_without_highest))
