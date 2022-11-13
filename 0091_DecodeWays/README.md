解法1: DP

X X [i X X]
dp[i]表示由i為首的decode way

(連續非0時)
1 => 1
12 => 2
121 => 3 = 1 + 2
1212 => 5 = 2 + 3
dp[i] = dp[i + 1] + dp[i + 2]

由後往前找，
如果s[i]為0無法decode，故dp[i] = 0，
case1: 
s:  ... 1 0 x ...
dp: ... 2 0 2 ...
[1 0]必定在一起不影響答案，
dp[i] = dp[i + 1] + dp[i + 2]
      =     0     + dp[i + 2]

case2: 
s:  ... 2 3 x ...
dp: ... 4 2 2 ...
[3]必定自己一組，

case3: 
s:  ... 3 3 x ...
dp: ... 2 2 2 ...

解法2: DFS
step1: DFS架構
dp: {len(s): 1}

def dfs(i):
    if i in dp:  return dp[i] # 由後往前做
    if s[i] == "0":  return 0

    res = dfs(i + 1) # 從0開始代進dfs，到最後1項

    # 開始執行主要程式 

    return res # 由後往前做

return dfs(0)

從0開始代進dfs，到最後1項時，
開始執行主要程式，
等同於由後往前做，跟解法1相同，

step2: 執行主要程式