N = int(input())  
M = int(input())  
arr = [*map(int, input().split())] 

dist = [0] * (M+1)  
dist[0] = arr[0]  
dist[-1] = N - arr[-1]

for i in range(M-1):  
    val = arr[i+1] - arr[i]  
    dist[i+1] = val//2 + (1 if val % 2 else 0)  

print(max(dist))