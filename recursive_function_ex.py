v = [3, 6, 5, 4]
n = len(v)
memo = [-1 for i in range(n)]

print(memo)

def max_volume(i):
    if memo[i] != -1:
        return memo[i]
    elif i == 0:
        memo[i] = v[i]
    elif i == 1:
        memo[i] = max(v[i], v[i-i])
    else:
        memo[i] = max(max_volume(i-1), max_volume(i-2) + v[i])

    return memo[i]


print(max_volume(n-1))
print(memo)