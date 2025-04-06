def fib(n,dp):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        dp[n]=fib(n-1,dp)+fib(n-2,dp)

    return dp[n]

dp=[-1]*(8)
print(fib(7,dp))

# memozition method 
# top down approach

dp2=[0]*101
dp2[0]=0
dp2[1]=1

for i in range(2,101):
    dp2[i]=dp2[i-1]+dp2[i-2]

print(dp2[100])

# bottom-up-approch
# tabular method
