n = 3
w = 4
val = [1, 2, 3]
wt = [4, 5, 1]

def solve(n, cap):
    if n == 0 or cap == 0:
        return 0
    cwt = wt[n - 1]
    cv = val[n - 1]
    if cwt <= cap:
        c1 = cv + solve(n - 1, cap - cwt)  # ✅ fix: use cap - cwt
        c2 = solve(n - 1, cap)
        return max(c1, c2)
    else:
        return solve(n - 1, cap)

print(solve(n, w))  # Output: 3
