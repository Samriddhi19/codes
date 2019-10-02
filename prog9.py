if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
z = max(arr)
m=1
while m<n+1:
    if z == max(arr):
        arr.remove(z)
    m=m+1
print(max(arr))