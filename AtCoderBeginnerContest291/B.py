N = int(input())
X = sorted(list(map(int, input().split())))
mean = sum(X[N:-N]) / (3*N)
print(mean)
