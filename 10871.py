n, x = map(int, input().split())
li = list(map(int, input().split()))

 for i in range(n):
     if li[i] < x:
         print(li[i], end=' ')
     # li의 i 번째와 x를 비교
     # x보다 작은 i를 출력
