def knapsack(W, wt, val, n):
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    if n==0 or W==0:
        return 0
    if t[n][W]!=-1:
        return t[n][W]
    if wt[n-1]<=W:
        t[n][W]= max(val[n-1] +knapsack(W-wt[n-1],wt,val,n-1),knapsack(W,wt,val,n-1))
        return t[n][W]
    elif wt[n-1]>W:
        t[n][W]=knapsack(W,wt,val,n-1)
        return t[n][W]

val = [60, 100, 120 ]
wt = [10, 20, 30 ]
W = 50
n = len(val)
print(knapsack(W,wt,val,n))
